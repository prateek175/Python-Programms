import pytube
import pytube.streams
from tkinter import *
from tkinter import ttk


def youtube():
    link = url.get()
    yt = pytube.YouTube(link)
    stream = yt.streams.first()
    stream.download('C:/Users/Pratik Patil/Desktop/gallery')
    f = stream.filesize
    MaxFileSize = int(f / 1024000)
    MB = str(MaxFileSize) + " MB"
    lab_mb.set(MB)

    percent = int((101 * (f - MaxFileSize)) / f)
    per=str(percent)+"%"
    lab_percent.set(per)
def audio():
    link=url.get()
    yt=pytube.YouTube(link)
    stream=yt.streams.filter(only_audio=True)
    stream[1].download('C:/Users/Pratik Patil/Desktop/gallery')
    f = stream.filesize
    MaxFileSize = int(f / 1024000)
    MB = str(MaxFileSize) + " MB"
    lab_mb.set(MB)
    percent = int((101 * (f - MaxFileSize)) / f)
    per=str(percent)+"%"
    lab_percent.set(per)


Ck = Tk()
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
