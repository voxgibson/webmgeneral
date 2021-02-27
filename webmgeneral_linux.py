# WEBM GENERAL CONVERTER v3.0 LINUX #

# Required Installations:
# sudo apt-get install python3 
# sudo apt-get install python3-tk
# sudo apt-get install ffmpeg

# Modules
import os
import threading
import subprocess
from tkinter import END, Button, Entry, Label, Tk, filedialog, StringVar, OptionMenu, messagebox, SUNKEN, W

# Window Configuration
window = Tk()
window.title('WEBM GENERAL CONVERTER')
window.resizable(0, 0)
window['bg'] = '#EEF2FF'

# Functions
def statusUpdate(status):
    # Creates and updates status bar.
    Label(text=status, anchor=W, relief=SUNKEN, width=75).grid(row=6, column=1, columnspan=5)

def bitCalculate(*args):
    # Gets size and sound option and sets max bit size.
    global sizeSound
    global maxBitSize
    global soundSelection
    sizeSound = sizeSoundSelect.get()
    if sizeSound == 'No Limit (Sound)':
        soundSelection = 'on'
        bitRate_ent.delete(0, END)
        bitRate_ent.insert(0, 'No Limit')
        return
    if sizeSound == 'No Limit (No Sound)':
        soundSelection = 'off'
        bitRate_ent.delete(0, END)
        bitRate_ent.insert(0, 'No Limit')
        return
    if inputVideo_ent.get() == "":
        bitRate_ent.delete(0, END)
        return
    if sizeSound == '3MB (Sound)':
        maxBitSize = 25165824
        soundSelection = 'on'
    if sizeSound == '3MB (No Sound)':
        maxBitSize = 25165824
        soundSelection = 'off'
    if sizeSound == '4MB (Sound)':
        maxBitSize = 33165824
        soundSelection = 'on'
    if sizeSound == '4MB (No Sound)':
        maxBitSize = 33165824
        soundSelection = 'off'
    if sizeSound == '6MB (Sound)':
        maxBitSize = 50331648
        soundSelection = 'on'
    if sizeSound == '6MB (No Sound)':
        maxBitSize = 50331648
        soundSelection = 'off'

    # Gets input video path from entry field. 
    inputVideo = inputVideo_ent.get()

    # Uses ffprobe to get the videos total amount of seconds. 
    videoSeconds = os.popen(f'ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 "{inputVideo}"').read()

    # Change bits and seconds to floats prior to bit rate calculation.
    maxBitsFloat = float(maxBitSize)
    secondsFloat = float(videoSeconds)

    # Maximum allowed bit rate formula. The result is rounded.
    bitRate = round(maxBitsFloat/secondsFloat)

    # Fills in 'Calculated Maximum Allowed Bitrate' entry field.
    bitRate_ent.delete(0, END)
    bitRate_ent.insert(0, bitRate)

def inputVideo():
    # Opens input video file dialog and fills in the input video entry field. 
    filename = filedialog.askopenfilename(filetypes=[('Video Files',' *.3g2 *.3gp *.asf *.avi *.flv *.m2t *.m2ts *.m4v *.mkv *.mod *.mov *.mp4 *.mpg *.vob *.wmv'),('All', '*.*')])          
    directoryPath = os.path.normpath(filename)
    inputVideo_ent.delete(0, END)
    inputVideo_ent.insert(0, directoryPath)
    if inputVideo_ent.get() == ".":
        inputVideo_ent.delete(0, END)
        metadata_ent.delete(0, END)
        bitRate_ent.delete(0, END)
    else:
        metadata()
        bitCalculate()

def outputFolder():
    # Opens output folder selection dialog. 
    directory = filedialog.askdirectory()
    directoryPath = os.path.normpath(directory)

    # Fills in the output folder entry field. 
    outputFolder_ent.delete(0, END)
    outputFolder_ent.insert(0, directoryPath)
    if outputFolder_ent.get() == ".":
        outputFolder_ent.delete(0, END)

def metadata():
    # Fills in the Metadata Title entry field.
    inputVideo = inputVideo_ent.get()
    metadata = os.path.splitext(os.path.basename(inputVideo))[0]
    metadata_ent.delete(0, END)
    metadata_ent.insert(0, metadata)

def convert():
    try:
        # Updates status.
        statusUpdate("Converting...")

        # Gets previous calculations and file paths.
        bitRate = bitRate_ent.get()
        metadata = metadata_ent.get()
        inputVideo = inputVideo_ent.get()
        outputFolder = outputFolder_ent.get()
        outputName = os.path.splitext(os.path.basename(inputVideo))[0]
        fullPath = f'{outputFolder}/{outputName}.webm'
        
        # Gets output resolution option. 
        maxHeight = resSelect.get()
        if maxHeight == "Source":
            maxHeight = os.popen(f'ffprobe -v error -select_streams v:0 -show_entries stream=height -of default=nw=1:nk=1 "{inputVideo}"').read()

        if sizeSound == "No Limit (Sound)" or sizeSound == "No Limit (No Sound)":
            
            # Starts ffmpeg conversion from video to webm.
            if soundSelection == 'on':
                os.system(f'ffmpeg -hide_banner -y -i "{inputVideo}" -metadata title="{metadata}" -threads 0 -sn -codec:a libvorbis -qscale:a 2 -c:v libvpx -b:v 0 -crf 10 -vf scale=h="min(ih\,{maxHeight})":w=-2 -quality best -cpu-used 0 -slices 8 -auto-alt-ref 1 -f null -pass 1 -')
                os.system(f'ffmpeg -hide_banner -y -i "{inputVideo}" -metadata title="{metadata}" -threads 0 -sn -codec:a libvorbis -qscale:a 2 -c:v libvpx -b:v 0 -crf 10 -vf scale=h="min(ih\,{maxHeight})":w=-2 -quality best -cpu-used 0 -slices 8 -auto-alt-ref 1 -f webm -pass 2 "{fullPath}"')
            if soundSelection == 'off':
                os.system(f'ffmpeg -hide_banner -y -i "{inputVideo}" -metadata title="{metadata}" -threads 0 -sn -an -c:v libvpx -b:v 0 -crf 10 -vf scale=h="min(ih\,{maxHeight})":w=-2 -quality best -cpu-used 0 -slices 8 -auto-alt-ref 1 -f null -pass 1 -')
                os.system(f'ffmpeg -hide_banner -y -i "{inputVideo}" -metadata title="{metadata}" -threads 0 -sn -an -c:v libvpx -b:v 0 -crf 10 -vf scale=h="min(ih\,{maxHeight})":w=-2 -quality best -cpu-used 0 -slices 8 -auto-alt-ref 1 -f webm -pass 2 "{fullPath}"')
            
            # Removes ffmpeg2pass-0.log if it already exist. 
            try:
                os.remove('ffmpeg2pass-0.log')
            except OSError:
                pass

            resultBytes = os.path.getsize(fullPath)
            resultMB = round(resultBytes/1024/1024, 2)

            statusUpdate('Finished!')
            messagebox.showinfo(title='Finished!', message=f'Conversion Complete\nResult Size: {resultMB}MB')
            return
        
        # Starts ffmpeg conversion from video to webm.
        if soundSelection == 'on':
            os.system(f'ffmpeg -hide_banner -y -i "{inputVideo}" -metadata title="{metadata}" -threads 0 -sn -codec:a libvorbis -qscale:a 2 -c:v libvpx -b:v {bitRate} -vf scale=h="min(ih\,{maxHeight})":w=-2 -quality best -cpu-used 0 -slices 8 -auto-alt-ref 1 -f null -pass 1 -')
            os.system(f'ffmpeg -hide_banner -y -i "{inputVideo}" -metadata title="{metadata}" -threads 0 -sn -codec:a libvorbis -qscale:a 2 -c:v libvpx -b:v {bitRate} -vf scale=h="min(ih\,{maxHeight})":w=-2 -quality best -cpu-used 0 -slices 8 -auto-alt-ref 1 -f webm -pass 2 "{fullPath}"')
        if soundSelection == 'off':
            os.system(f'ffmpeg -hide_banner -y -i "{inputVideo}" -metadata title="{metadata}" -threads 0 -sn -an -c:v libvpx -b:v {bitRate} -vf scale=h="min(ih\,{maxHeight})":w=-2 -quality best -cpu-used 0 -slices 8 -auto-alt-ref 1 -f null -pass 1 -')
            os.system(f'ffmpeg -hide_banner -y -i "{inputVideo}" -metadata title="{metadata}" -threads 0 -sn -an -c:v libvpx -b:v {bitRate} -vf scale=h="min(ih\,{maxHeight})":w=-2 -quality best -cpu-used 0 -slices 8 -auto-alt-ref 1 -f webm -pass 2 "{fullPath}"')

        # Removes ffmpeg2pass-0.log if it already exist. 
        try:
            os.remove('ffmpeg2pass-0.log')
        except OSError:
            pass

        # Checks if webm went over maximum file size. 
        # If so the video is reconverted with a lower bit rate.
        resultBytes = os.path.getsize(fullPath)
        resultBits = resultBytes*8
        resultMB = round(resultBytes/1024/1024, 2)

        if resultBits < maxBitSize:
            statusUpdate('Finished!')
            messagebox.showinfo(title='Finished!', message=f'Conversion Complete\nResult Size: {resultMB}MB')
            return
        if (resultBits - maxBitSize) > 100000:
            oldRate = int(bitRate_ent.get())
            newRate = int(bitRate_ent.get())-50000
            bitRate_ent.delete(0, END)
            bitRate_ent.insert(0, newRate)
            convert()
        else:
            oldRate = int(bitRate_ent.get())
            newRate = int(bitRate_ent.get())-10000
            bitRate_ent.delete(0, END)
            bitRate_ent.insert(0, newRate)
            convert()
    except:
        # Updates status bar if error occurs.
        statusUpdate("Error...")

def runStart():
    # Runs conversion process separate from main window.
    threading.Thread(target=convert).start()

# Size and sound options.
sizeSoundList = ["3MB (Sound)", "3MB (No Sound)", "4MB (Sound)", "4MB (No Sound)", "6MB (Sound)", "6MB (No Sound)", "No Limit (Sound)", "No Limit (No Sound)"]
sizeSoundSelect = StringVar()
sizeSoundSelect.set(sizeSoundList[1])
sizeSoundSelect.trace("w", bitCalculate)
outSizeSound_ent = OptionMenu(window, sizeSoundSelect, *sizeSoundList)
outSizeSound_ent.grid(row=1, column=4, pady=1, sticky='E')

# Max output resolution options.
resList = ["480", "720", "1080", "Source"]
resSelect = StringVar()
resSelect.set(resList[3])
outRes_ent = OptionMenu(window, resSelect, *resList)
outRes_ent.grid(row=1, column=5, padx=5, pady=1, sticky='W')

# Labels
Label(text='WEBM GENERAL', font='Arial 14 bold', fg='#0f0c5d', bg='#EEF2FF').grid(row=1, column=1, sticky='E', columnspan=2)
Label(text='Converter v3.0', font='Arial 13 bold', fg='#789922', bg='#EEF2FF').grid(row=1, column=3, sticky='W', columnspan=2)
Label(text='Input Video >', bg='#EEF2FF').grid(row=2, column=1, sticky='E')
Label(text='Output Folder >', bg='#EEF2FF').grid(row=3, column=1, sticky='E')
Label(text='Metadata Title >', bg='#EEF2FF').grid(row=4, column=1, sticky='E')
Label(text='Calculated Maximum Allowed Bitrate (Bits/s) >', bg='#EEF2FF').grid(row=5, column=4, sticky='E')

# Entry Fields
inputVideo_ent = Entry(fg='#789922', width=45)
inputVideo_ent.grid(row=2, column=2, padx=1, sticky='W', columnspan=3)
outputFolder_ent = Entry(fg='#789922', width=45)
outputFolder_ent.grid(row=3, column=2, padx=1, sticky='W', columnspan=3)
metadata_ent = Entry(fg='#0f0c5d', width=60)
metadata_ent.grid(row=4, column=2, padx=1, sticky='W', columnspan=4)
bitRate_ent = Entry(fg='#d00', width=13)
bitRate_ent.grid(row=5, column=5, padx=6)

# Buttons
Button(text='Browse', width=10, command=inputVideo).grid(row=2, column=5, padx=5)
Button(text='Browse', width=10, command=outputFolder).grid(row=3, column=5, padx=5, pady=5)
Button(text='Start', width=10, command=runStart).grid(row=5, column=1, padx=5, pady=5)

window.mainloop()
