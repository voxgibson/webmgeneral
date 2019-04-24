# WEBM GENERAL CONVERTER v1.7 macOS #

# Required Installations:
# python3 - https://www.python.org/downloads/
# /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
# brew install ffmpeg

# Modules
import os
import subprocess
from tkinter import END, Button, Entry, Label, Tk, filedialog, StringVar, OptionMenu

# Window Configuration
window = Tk()
window.title('WEBM GENERAL CONVERTER')
window.resizable(0, 0)
window['bg'] = '#EEF2FF'

# Maximum allowed webm file size in bits.
maxBitSize = 25165824

# Functions
def inputVideo():
    # Opens input video file dialog and fills in the input video entry field. 
    directory = filedialog.askopenfilename(filetypes=[('Video Files',' *.3g2 *.3gp *.asf *.avi *.flv *.m2t *.m2ts *.m4v *.mkv *.mod *.mov *.mp4 *.mpg *.vob *.wmv'),('All', '*.*')])          
    directoryPath = os.path.normpath(directory)
    inputVideo_ent.delete(0, END)
    inputVideo_ent.insert(0, directoryPath)

    # Gets input video path from entry field. 
    videoInput = str(inputVideo_ent.get())

    # Uses ffprobe to get the videos total amount of seconds. 
    videoSeconds = os.popen(f'ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 "{videoInput}"').read()

    # Change bits and seconds to floats prior to bit rate calulation.
    maxBitsFloat = float(maxBitSize)
    secondsFloat = float(videoSeconds)

    # Maximum allowed bit rate formula. The result is rounded.
    bitRate = round(maxBitsFloat/secondsFloat)

    # Fills in 'Calculated Maximum Allowed Bitrate' entry field.
    bitRate_ent.delete(0, END)
    bitRate_ent.insert(0, bitRate)

def outputFolder():
    # Opens output folder selection dialog. 
    directory = filedialog.askdirectory()
    directoryPath = os.path.normpath(directory)

    # Fills in the output folder entry field. 
    outputFolder_ent.delete(0, END)
    outputFolder_ent.insert(0, directoryPath)

def start():
    # Gets previous calculations and file paths.
    bitRate = str(bitRate_ent.get())
    inputVideo = str(inputVideo_ent.get())
    outputFolder = str(outputFolder_ent.get())
    outputName = os.path.splitext(os.path.basename(inputVideo))[0]
    fullPath = str(f'{outputFolder}/{outputName}.webm')
    
    # Gets selected output resolution option. 
    maxHeight = resSelect.get()

    # Starts ffmpeg conversion from video to webm.
    os.system(f'ffmpeg -y -i "{inputVideo}" -threads 0 -sn -an -c:v libvpx -b:v {bitRate} -vf scale=h="min(ih\,{maxHeight})":w=-2 -quality best -cpu-used 0 -slices 8 -auto-alt-ref 1 -f webm -pass 1 nul')
    os.system(f'ffmpeg -y -i "{inputVideo}" -threads 0 -sn -an -c:v libvpx -b:v {bitRate} -vf scale=h="min(ih\,{maxHeight})":w=-2 -quality best -cpu-used 0 -slices 8 -auto-alt-ref 1 -f webm -pass 2 "{fullPath}"')

    #Removes ffmpeg2pass-0.log if it already exist. 
    try:
        os.remove('ffmpeg2pass-0.log')
        os.remove('nul')
    except OSError:
        pass

    # Checks if WebM went over maximum file size. 
    # If so the video is reconverted with a lower bit rate.
    resultBytes = os.path.getsize(fullPath)
    resultBits = resultBytes*8
    print('###############################################')
    print('WEBM FILE SIZE LIMIT (Bits): ' + str(maxBitSize))
    print('WEBM RESULT SIZE     (Bits): ' + str(resultBits))
    print('###############################################')

    if resultBits < maxBitSize:
        print('###############################################')
        print('WEBM OUTPUT RESULT IS BELOW FILE SIZE LIMIT')
        print('FINISHED!')
    else:
        print('###############################################')
        print('WEBM OUTPUT RESULT WENT OVER FILE SIZE LIMIT')
        print('RECONVERTING INPUT VIDEO AT A LOWER BIT RATE')
        print('###############################################')
        newRate = int(bitRate_ent.get())-10000
        bitRate_ent.delete(0, END)
        bitRate_ent.insert(0, newRate)
        start()

# Entry Fields
inputVideo_ent = Entry(fg='#789922', width=35)
inputVideo_ent.grid(row=1, column=2, padx=1, sticky='W', columnspan=3)

outputFolder_ent = Entry(fg='#789922', width=35)
outputFolder_ent.grid(row=2, column=2, padx=1, sticky='W', columnspan=3)

bitRate_ent = Entry(fg='#d00', width=9)
bitRate_ent.grid(row=3, column=5, padx=5, sticky='W')

# Labels
Label(text='WEBM GENERAL', font='Arial 15 bold', fg='#0f0c5d', bg='#EEF2FF').grid(row=0, column=1, sticky='W', columnspan=3)
Label(text='Converter v1.7', font='Arial 14 bold', fg='#789922', bg='#EEF2FF').grid(row=0, column=4, sticky='W')
Label(text='Max Output Resolution >', bg='#EEF2FF').grid(row=0, column=4, sticky='E')
Label(text='Input Video >', bg='#EEF2FF').grid(row=1, column=1, sticky='E')
Label(text='Output Folder >', bg='#EEF2FF').grid(row=2, column=1, sticky='E')
Label(text='Calculated Maximum Allowed Bitrate (Bits/s) >', bg='#EEF2FF').grid(row=3, column=4, sticky='E')

# Options
resList = ["480", "720", "1080"]
resSelect = StringVar()
resSelect.set(resList[1])
outRes_ent = OptionMenu(window, resSelect, *resList)
outRes_ent.grid(row=0, column=5, padx=5, pady=1, sticky='W')

# Buttons
Button(text='Browse', width=10, command=inputVideo).grid(row=1, column=5, padx=5, sticky='W')
Button(text='Browse', width=10, command=outputFolder).grid(row=2, column=5, padx=5, pady=5, sticky='W')
Button(text='Start', width=10, command=start).grid(row=3, column=1, padx=5, pady=5, columnspan=1)

window.mainloop()
