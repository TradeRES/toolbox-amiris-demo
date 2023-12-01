# Spine Toolbox demo project for AMIRIS
## Requirements
* git
* Python 3.9 or 3.10
* Java SE Runtime Environment 11 (or later); get it, e.g. from https://adoptium.net/
* Spine Toolbox **development** version: version 0.6.1 or later. 
  get it from: https://github.com/Spine-project/Spine-Toolbox (or follow instructions below)

## Preparing the Python environments
AMIRIS and SpineToolbox require separate Python environments due to an incompatible dependency to [protobuf](https://pypi.org/project/protobuf/).

### Using Venv
Create a virtual environment for SpineToolbox: `python -m venv <path to virtual env>`

Activate the environment:
* on Windows: `\path\to\env\Scripts\activate.bat`
* on Linux: `source /path/to/env/bin/activate`

Install SpineToolbox: `pip install git+https://github.com/Spine-project/spinetoolbox-dev`

Create another virtual environment, this time for AMIRIS: `python -m venv <path to virtual env>`

Activate the other environment:
* on Windows: `\path\to\env\Scripts\activate.bat`
* on Linux: `source /path/to/env/bin/activate`

Install amirispy: `pip install amirispy`

### Using conda
Create a conda environment for SpineToolbox: `conda create -n <nameOfSpineEnvironment> python=3.9`

Activate the environment: `conda activate <nameOfSpineEnvironment>`

Install SpineToolbox: `pip install git+https://github.com/Spine-project/spinetoolbox-dev`

Create another environment, this time for AMIRIS: `conda create -n <nameOfAmirisEnvironment> python=3.9`

Activate the other environment: `conda activate <nameOfAmirisEnvironment>`

Install amirispy: `pip install amirispy`

## Get AMIRIS spine-toolbox workflow
Checkout the AMIRIS spine-toolbox workflow: `git clone https://github.com/TradeRES/toolbox-amiris-demo`

## Setup of Toolbox project
If not still active, activate the **SpineToolbox** Python environment created above.
Then, launch Spine Toolbox: `spinetoolbox`

In the toolbox menu, navigate to **File -> Settings -> Tools** and ensure that the "Python (default settings)" points to the Python interpreter of the **other** created Python environment for **AMIRIS**.

Open the "toolbox-amiris-demo" project from the folder you have cloned it into.

### Update Tool Python environments
In the *Design View* window, double click on *make Fame run config*. In the drop-down box *Tool type* switch to tool type **Julia**, then return to tool type **Python**. This will update your interpreter settings to the defaults specified before. Close the tool window and save changes.

Repeat for tools *AMIRIS* and *Combine AMIRIS results*.

### Create local data store files
For this, select the tool *Results Data Store* in the *Design View* window and click **New Spine db**. 

Repeat for tool *Renamed results*.

### Run
You can now execute the whole workflow by clicking the black ‘play’ button on the Toolbar (**Execute project**).

## License and Terms of Use
The Spine Toolbox project example provided here can be used without any limitations.

This excludes:
* "scripts/amiris.jar", for which license of https://gitlab.com/dlr-ve/esy/amiris/amiris applies
* all files below "data/Germany2019", for which licenses of https://gitlab.com/dlr-ve/esy/amiris/examples apply.
