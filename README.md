# songRecognitionDisplay
Detect the currently playing song and display some info about it

**Python 3.8 or higher is required.**

## Installation
### Windows
**Create a venv:** `python -m venv venv`

**Install the requirements:** `pip install -r requirements.txt`

**Download [ffmpeg binaries](https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip) and move _ffmpeg.exe_ and _ffprobe.exe_ to the directory where this project is cloned.**
### Linux
**Create a venv:** `python3 -m venv venv`

**Install the requirements:** `pip3 install -r requirements.txt`

If you get errors while attempting to install the requirements (especially while installing **pyaudio**), open a terminal and install `python3-dev`, `build-essential` and `portaudio19-dev` using your package manager. (`base-devel` and `portaudio` in Arch linux)

## Usage

1. Connect a microphone if you haven't already
2. Run main.py
3. Run display.py
   - you can edit the padding on line 64 if needed, but it should automatically center
   - you can change which display is used on line 40


### Example setup
_This usage example uses a smartphone as a secondary display and microphone (completely wireless)_

1. Connect the phone to the computer as a second display using Wi-Fi (you can use the spacedesk app)
2. Connect the phone to the computer as a microphone using Bluetooth (you can use WO Mic)
3. Run main.py
4. Run display.py:
   - you can edit the padding on line 64 if needed, but it should automatically center
   - you can change which display is used on line 40

This was an example setup. You can obviously use a secondary monitor and a real microphone instead of a phone.
