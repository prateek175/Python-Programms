import pytube
import pytube.streams
from tkinter import *   
from tkinter import ttk   #not required line.......


def youtube():                          #define function for download the youtube video through video link(URL)...........
    link = url.get()                     #url.get()->>> Help to retrive Url Content 
    yt = pytube.YouTube(link)            #creating a variable ' yt ' which help to store         
    stream = yt.streams.first()       
    stream.download('C:/Users/Pratik Patil/Desktop/gallery') #location where you want to store.......
    
    f = stream.filesize                              """ .........................use show size and percentage when  video fully download.................................."""
    MaxFileSize = int(f / 1024000)     
    MB = str(MaxFileSize) + " MB"
    lab_mb.set(MB)

    percent = int((101 * (f - MaxFileSize)) / f)
    per=str(percent)+"%"
    lab_percent.set(per)

def audio():                     #def foe to get Audio File ....
    link = url.get()
    yt = pytube.YouTube(link)
    stream=yt.streams.get_audio_only('webm')    #get_audio_only method use for the  get the audio ... 
    stream.download('C:/Users/Pratik Patil/Desktop/gallery')
    f = stream.filesize
    MaxFileSize = int(f / 1024000)
    MB = str(MaxFileSize) + " MB"
    lab_mb.set(MB)

    percent = int((101 * (f - MaxFileSize)) / f)
    per=str(percent)+"%"
    lab_percent.set(per)



Ck = Tk()                                 #TKINTER 
url = StringVar()
lab_percent = StringVar()
lab_mb = StringVar()
url = Entry(Ck)
url.pack()
butt = Button(Ck, text="Download Now", command=youtube)
butt.pack()
lab1 = Label(Ck, text="", textvariable=lab_mb)
lab1.pack()
butt = Button(Ck, text="Download MP3 Now", command=audio)
butt.pack()
lab = Label(Ck, text="", textvariable=lab_percent)
lab.pack()

Ck.mainloop()
