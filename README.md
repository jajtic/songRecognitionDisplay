# songRecognitionDisplay
Detect the currently playing song and display some info about it

**Currently works on Windows only**

**Python 3.8 or higher is required.**

## Installation
**Create a venv:** `python -m venv venv`

**Install the requirements:** `pip install -r requirements.txt`

**Download [ffmpeg binaries](https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip) and move _ffmpeg.exe_ and _ffprobe.exe_ to the directory where this project is cloned.**

## Usage
_This usage example uses a smartphone as a secondary display and microphone (completely wireless)_

1. Connect the phone to the computer as a second display using Wi-Fi (you can use the spacedesk app)
2. Connect the phone to the computer as a microphone using Bluetooth (you can use WO Mic)
3. Run main.py
4. Run display.py:
   - you can edit the padding on line 55 if needed
   - you can change which display is used on line 37

This was an example setup. You can obviously use a secondary monitor and a real microphone instead of a phone.

## Future plans
Make it compatible with Linux so it can be run on a Raspberry Pi :)
