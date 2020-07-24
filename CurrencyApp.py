from tkinter import *
from currency_converter import CurrencyConverter

Ck = Tk()


def currency():
    C = CurrencyConverter()

    convertion = C.convert(int(ent1.get(), base=16), ent2.get(), ent3.get())
    myText.set(convertion)


Ck.geometry('200x200+500+250')
ent2 = StringVar()
ent3 = StringVar()
myText = StringVar()
lab = Label(Ck, text="Enter Number: ")
lab.pack()


ent1 = Entry(Ck)
ent1.pack()
lab1 = Label(Ck, text="Enter Country1:")
lab1.pack()

ent2 = Entry(Ck)
ent2.pack()
lab2=Label(Ck, text="Enter Country2:")
lab2.pack()
ent3 = Entry(Ck)
ent3.pack()
lab = Label(Ck, text="", textvariable=myText)
lab.pack(side=BOTTOM)
bat = Button(Ck, text="Convert", command=currency)
bat.pack()


Ck.mainloop()
