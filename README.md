# Jack - Personal Assistant

### Purpose
To create a voice driven personal assistant focusing primarily on open source technologies (with some 3rd party assistance). Technologies used:
 * pocket_sphinx
 * pico2wave
 * google stt

Refer to the requirements.txt file for additional packages referenced in the project

##

### Installation

1. Download the repo
2. Install python pocketsphinx - **pip install pocketsphinx**
3. Install requirements file - **pip install -r requirements.txt**
4. Setup a settings.py file based on the settings_demo.py example
	- Replace {API_KEY} with your api key provided by the WMATA
	- Replace the default location values based on their corresponding WMATA values
	  - Station_Name examples - *Pentagon City*, *Clarendon*, *Glenmont*
	  - Destination_Name examples - *Largo*, *Glenmont*, *Huntington*


##

### Running Jack

Currently Jack is a one off command script that will listen for a single command. To run the command simply execute `python jarvis.py`. When the console outputs `Say Something` you are able to speak a command.

#### Current Commands
 - **Next Metro** - Lists (or speaks!!) the list of upcoming trains based on the default location (defined in the settings.py file)
 - More commands on the way!
