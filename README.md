# WEBM GENERAL CONVERTER
A video to webm conversion tool used to create high quality webms that stay below 4chan's file size limit.

**Latest release:** https://github.com/scrodo/webmgeneral/releases/tag/v2.0

![alt text](https://i.imgur.com/m1Qv8Ly.jpg)

**Windows Requirements:** 

The portable versions for Windows are standalone applications and do not require any additional installations.

* Windows x64 Portable: https://github.com/scrodo/webmgeneral/releases/download/v2.0/WEBM_GENERAL__Portable___Windows_x64_v2.0.zip

* Windows x86 Portable: https://github.com/scrodo/webmgeneral/releases/download/v2.0/WEBM_GENERAL__Portable___Windows_x86_v2.0.zip

If you want to run the program from source in Windows it requires Python 3, ffmpeg, and ffprobe.

Link to Python 3 download: https://www.python.org/downloads

(Check 'Add Python to PATH' at the install screen.)

Download link for Windows ffmpeg: https://ffmpeg.zeranoe.com/builds/

(ffmpeg.exe and ffprobe.exe will be in the bin folder.)

The ffmpeg.exe and ffprobe.exe need to be put in the same folder as webmgeneral.py

Example commands for changing to the programs directory and running it:
```
cd "C:\Users\chad\Desktop\webmgeneral-master"

python "webmgeneral.py"
```
**Linux Requirements:**

The Linux version requires these installs through the terminal (Tested on Ubuntu):
```
sudo apt-get install python3

sudo apt-get install python3-tk

sudo apt-get install ffmpeg
```
Example command to run in the program in Linux:
```
sudo python3 '/home/chad/Desktop/webmgeneral-master/webmgeneral_linux.py'
```
**macOS Requirements:** 

The macOS version requires Python 3, Homebrew and ffmpeg.

Link to Python 3 download: https://www.python.org/downloads

Install Homebrew and ffmpeg through the terminal using these commands:
```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

brew install ffmpeg
```
Example command to run in the program in macOS:
```
python3 '/Users/chad/Desktop/webmgeneral-master/webmgeneral_macOS.py'
```
