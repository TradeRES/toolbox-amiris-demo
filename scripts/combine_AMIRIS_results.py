import sys
import os
from pathlib import Path
from glob import glob
import shutil

import pandas as pd
from fameio.scripts.convert_results import run as convert_results
from fameio.source.cli import Options, ResolveOptions
from fameio.source.time import FameTime

CONFIG = {
    Options.LOG_LEVEL: "info",
    Options.LOG_FILE: None,
    Options.AGENT_LIST: ["EnergyExchange"],
    Options.OUTPUT: "FameResults_converted",
    Options.SINGLE_AGENT_EXPORT: False,
	Options.RESOLVE_COMPLEX_FIELD: ResolveOptions.IGNORE,
}


def process_file(filepath: str) -> pd.DataFrame:
    """Process single AMIRIS csv file"""
    df = pd.read_csv(filepath, sep=";")
    object_class = Path(filepath).stem
    assert df.columns[0] == "AgentId"
    assert df.columns[1] == "TimeStep"
    # Convert times steps
    df["TimeStamp"] = df["TimeStep"].apply(FameTime.convert_fame_time_step_to_datetime)
    # Hack to replace non-standard separator '_' with 'T'
    df["TimeStamp"] = df["TimeStamp"].str.replace("_", "T")
    df["ObjectClass"] = object_class
    return df.drop("TimeStep", axis=1).melt(["ObjectClass", "AgentId", "TimeStamp"])


# Remove previous results
if os.path.exists(CONFIG[Options.OUTPUT]):
    shutil.rmtree(CONFIG[Options.OUTPUT])
if os.path.exists("AMIRIS_combined.csv"):
    os.remove("AMIRIS_combined.csv")


# Get input file from cmd line arguments
input_pb_file = sys.argv[1]

# Convert Proto Buffer file to csv's
convert_results(input_pb_file, CONFIG)

# Combine csv files into one data frame
csv_files = glob(f"{CONFIG[Options.OUTPUT]}/*.csv")
data = pd.concat(map(process_file, csv_files))

# Drop empty rows
data.dropna(axis=0, how="any", subset=["value"], inplace=True)

# Write results
data.to_csv("AMIRIS_combined.csv", index=False)
