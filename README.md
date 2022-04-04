# Spine Toolbox demo project for AMIRIS
## Requirements
* git
* Python 3.8
* Java SE Runtime Environment 8 (or later); get it, e.g. from https://adoptium.net/
* Spine Toolbox **development** version: version 0.6.1 or later. 
  get it from: https://github.com/Spine-project/Spine-Toolbox (or follow instructions below)

## Preparing the Python environment

### Using Venv
Create a virtual environment to isolate the new packages.
    
	python -m venv <path to virtual env>

Activate the environment (on Windows): `\path\to\env\Scripts\activate.bat`
Activate the environment (on Linux): `source /path/to/env/bin/activate`
	
Then, install required Python packages with
	
    pip install -r requirements.txt
	pip install git+https://github.com/Spine-project/spinetoolbox-dev
    
### Using conda
Create a conda environment to isolate the new packages.

    conda create -n <nameOfEnvironment> python=3.8

Activate the environment: `conda activate <nameOfEnvironment>`
Then, install required Python packages with
	pip install -r requirements.txt
	pip install git+https://github.com/Spine-project/spinetoolbox-dev

## Get AMIRIS spine-toolbox workflow
Checkout the AMIRIS spine-toolbox workflow using

    git clone https://github.com/TradeRES/toolbox-amiris-demo

## Opening the Toolbox project
If not still active, activate the Python environment created above. Then, launch Spine Toolbox:

On Windows: `spinetoolbox.exe`
On Linux: `spinetoolbox`

In the toolbox menu, navigate to **File -> Settings -> Tools** and ensure that the "Python (default settings)" 
points to the python interpreter of the currently active Python environment.

Open the "toolbox-amiris-demo" project from the folder you have cloned it into. 
You may need to re-create the local data store files. Select *Results Data Store* and click **New Spine db**. Repeat for 
*Renamed results*.

You can now execute the whole workflow by clicking the black ‘play’ button on the Toolbar (**Execute project**).


## License and Terms of Use
The Spine Toolbox project example provided here can be used without any limitations.

This excludes:
* "scripts/amiris.jar", for which license of https://gitlab.com/dlr-ve/esy/amiris/amiris applies
* all files below "data/Germany2019", for which licenses of https://gitlab.com/dlr-ve/esy/amiris/examples apply.


