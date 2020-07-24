from selenium import webdriver
from tkinter import *
from time import sleep


def search():
    driver = webdriver.Chrome(executable_path="C:/Users/Pratik Patil/Desktop/chromedriver.exe")
    driver.maximize_window()
    driver.get("https://www.google.com/")

    driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input') \
        .send_keys(enter.get())
    sleep(3)
    driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[2]/div[2]/div[2]/center/input[1]') \
        .click()


Ck = Tk()
Ck.geometry('300x300')
Ck.resizable(width=False, height=False)
Ck.configure(bg='#212121')
enter = StringVar()

enter = Entry(Ck, justify = CENTER)
enter.pack(side = TOP, ipadx = 30, ipady = 6)

butt = Button(text="Search", command=search, relief=FLAT, bg='white')
butt.pack(side = TOP, pady = 10)

Ck.mainloop()
