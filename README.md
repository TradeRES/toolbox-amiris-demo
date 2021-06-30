Spine Toolbox demo project for AMIRIS ABM
=========================================

## Requirements

* Python 3.8 or later
* Spine Toolbox version 0.6.1 or later. 
  Get it from https://pypi.org/project/spinetoolbox/
* Java SE Runtime Environment 8 (or later)


## Preparing the Python environment

Create a virtual environment to isolate the new packages.

    python -m venv <path to virtual env>

Activate the environment and install required Python packages with (on Windows)
    
    \path\to\env\Scripts\activate.bat
    pip install -r requirements.txt
    
On Linux systems, activation is done with `source /path/to/env/bin/activate`.


## Inserting data

Place AMIRIS Java archive file (amiris-midgard-jar-with-dependencies.jar) 
into folder *scripts*.

Place AMIRIS input data into the folder *data/FameioTest* so that the final folder 
structure is as follows

```
data/FameioTest
|
├───ref_data
│   ├───carbonmarket
│   ├───conventionals
│   ├───demand
│   ...
|
└───yaml
    │   scenario.yaml
    │   schema.yaml
    │
    └───contracts/
```


## Opening the Toolbox project

Launch Spine Toolbox and select the virtual environment Python executable 
(python.exe on Windows) as the Python interpreter from **File -> Settings -> Tools**.

Open the proejct in this folder. You may need to re-create the local data store
files. Select *Results Data Store* and click **New Spine db**. Repeat for 
*Renamed results*.

You can now execute the whole workflow by clicking the black ‘play’ button 
on the Toolbar (**Execute project**).


## License and Terms of Use

The Spine Toolbox project example provided here can be used without any limitations.

