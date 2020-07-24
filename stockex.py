import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time
from tkinter import *


def stock():
    api_key = 'SLTIHDCE5Z92H0Q8'

    ts = TimeSeries(key=api_key, output_format='pandas')
    data, meta_data = ts.get_intraday(symbol=enter.get(), interval='1min', outputsize='full')
    mytext.set(data)

    i = 1
    # while i==1:
    #    data, meta_data = ts.get_intraday(symbol='MSFT', interval = '1min', outputsize = 'full')
    #    data.to_excel("output.xlsx")
    #    time.sleep(60)

    close_data = data['4. close']
    percentage_change = close_data.pct_change()
    mytext1.set(percentage_change)

    last_change = percentage_change[-1]

    if abs(last_change) > 0.0004:
        p = enter.get() + str(last_change)
        p1.set(p)


Ck = Tk()
mytext = StringVar()
mytext1 = StringVar()
enter = StringVar()
p1 = StringVar()
enter = Entry(Ck)
enter.pack()
butt = Button(Ck, text="SHOW", command=stock)
butt.pack()
lab = Label(Ck, text="", textvariable=mytext)
lab.pack(fill="both", expand="yes")
lab2 = Label(Ck, text="", textvariable=mytext1)
lab2.pack()
l = Label(Ck, text="Alert", textvariable=p1)
l.pack()
Ck.mainloop()
