# WEBM GENERAL CONVERTER
A video to webm conversion tool used to create high quality webms that stay below 4chan's file size limit.

**Latest release:** https://github.com/voxgibson/webmgeneral/releases/tag/v1.7

![alt text](https://i.imgur.com/fH2DgH0.png)

**Windows Requirements:** 

The portable versions for Windows are standalone applications and do not require any additional installations.

If you want to run the program from source in Windows it requires Python 3, ffmpeg.exe and ffprobe.exe

The ffmpeg and ffprobe exe's need to be in the same folder as the the program.

Link to Python 3 download: https://www.python.org/downloads

Link to ffmpeg and ffprobe for Windows. (The applications are in the bin folder.): https://ffmpeg.zeranoe.com/builds/

Example command to run the program in Windows:

*python3 'C:\Users\chad\Desktop\webmgeneral-master\webmgeneral.py'*

**Linux Requirements:**

The Linux version requires these installs through the terminal (Tested on Ubuntu):

*sudo apt-get install python3*

*sudo apt-get install python3-tk*

*sudo apt-get install ffmpeg*

Example command to run in the program in Linux:

*sudo python3 '/home/chad/Desktop/webmgeneral-master/webmgeneral_linux.py'*

**macOS Requirements:** 

The macOS version requires Python 3, Homebrew and ffmpeg.

Link to Python 3 download: https://www.python.org/downloads

Install Homebrew and ffmpeg through the terminal using these commands:

*/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"*

*brew install ffmpeg*

Example command to run in the program in macOS:

*python3 '/Users/chad/Desktop/webmgeneral-master/webmgeneral_macOS.py'*
