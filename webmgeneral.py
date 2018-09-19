# Modules
from tkinter import Tk, filedialog, Entry, Label, Button, END
import os
import subprocess

# Window Configuraton
window = Tk()
window.title('WEBM GENERAL CONVERTER')
window.resizable(0, 0)
window.iconbitmap('icon.ico')
window['bg'] = '#EEF2FF'

# Functions
def inputVideo():
    # Opens input video file dialog.
    directory = filedialog.askopenfilename(filetypes=[('Video Files', '*.3gp *.avi *.flv *.mp4 *.mpeg *.mov *.wmv')])
    directoryPath = os.path.normpath(directory)
    inputVideo_ent.delete(0, END)
    inputVideo_ent.insert(0, directoryPath)

    # Calculates Maximum Allowed Bitrate.
    inputVideo = str(inputVideo_ent.get())
    duration = os.popen('ffprobe "' + inputVideo + '" -show_entries format=duration -of compact=p=0:nk=1 -v 0').read()
    calculation = ((2.985 / float(duration))*8)
    bitRate = round(calculation, 3)
    bitRate_ent.delete(0, END)
    bitRate_ent.insert(0, bitRate)

def outputFolder():
    # Opens ouput folder selection dialog. 
    directory = filedialog.askdirectory()
    directoryPath = os.path.normpath(directory)
    outputFolder_ent.delete(0, END)
    outputFolder_ent.insert(0, directoryPath)

def start():
    # Starts conversion.
    inputVideo = str(inputVideo_ent.get())
    bitRate = str(bitRate_ent.get())
    outputName = os.path.splitext(os.path.basename(inputVideo))[0]
    outputFolder = str(outputFolder_ent.get())
    fullPath = str(outputFolder + '\\' + outputName + '.webm')
    subprocess.Popen('ffmpeg -y -i "' + inputVideo + '" -c:v libvpx -b:v "' + str(bitRate) + '"M -c:a libvorbis -an "' + fullPath)

# Entry Fields
inputVideo_ent = Entry(fg='#789922', width=45)
inputVideo_ent.grid(row=1, column=2, padx=1, sticky='W', columnspan=3)

outputFolder_ent = Entry(fg='#789922', width=45)
outputFolder_ent.grid(row=2, column=2, padx=1, sticky='W', columnspan=3)

bitRate_ent = Entry(fg='#d00', width=13)
bitRate_ent.grid(row=3, column=5, padx=5, sticky='W')

# Labels
Label(text='WEBM GENERAL', font='Arial 11 bold', fg='#0f0c5d', bg='#EEF2FF').grid(row=0, column=1, sticky='W', columnspan=3)
Label(text='Converter v1.0', font='Arial 10 bold', fg='#789922', bg='#EEF2FF').grid(row=0, column=4, sticky='W')
Label(text='Input Video >', bg='#EEF2FF').grid(row=1, column=1, sticky='E')
Label(text='Output Folder >', bg='#EEF2FF').grid(row=2, column=1, sticky='E')
Label(text='Calculated Maximum Allowed Bitrate (Mb/s) >', bg='#EEF2FF').grid(row=3, column=4, sticky='E')

# Buttons
Button(text='Browse', width=10, command=inputVideo).grid(row=1, column=5, padx=5, sticky='W')
Button(text='Browse', width=10, command=outputFolder).grid(row=2, column=5, padx=5, pady=5, sticky='W')
Button(text='Start', width=10, command=start).grid(row=3, column=1, padx=5, pady=5, columnspan=1)

window.mainloop()