import sys
import os
from pathlib import Path

from fameio.scripts.make_config import run as make_config
from fameio.source.cli import Options

CONFIG = {
    Options.LOG_LEVEL: "info",
    Options.OUTPUT: "fameConfig.pb",
    Options.LOG_FILE: None,
}

# remove previous results
if os.path.exists("fameConfig.pb"):
    os.remove("fameConfig.pb")

# Get scenario file from the command line
scenario_yaml = sys.argv[1]

# `make_config` has to be run from the scenario root dir containing yaml and data folders
curdir = os.getcwd()
try:
    os.chdir(Path(scenario_yaml).parent)
    make_config(scenario_yaml, CONFIG)
    os.replace(CONFIG[Options.OUTPUT], os.path.join(curdir, CONFIG[Options.OUTPUT]))
except:
    raise
finally:
    os.chdir(curdir)
