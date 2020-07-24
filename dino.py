import pyautogui
from PIL import Image,ImageGrab,ImageOps
from selenium import webdriver
from time import sleep
from pynput.keyboard import Key, Controller
from numpy import asarray
import time
driver = webdriver.Chrome(executable_path="C:/Users\/Pratik Patil/Desktop/chromedriver.exe")
driver.get("chrome://dino/")
sleep(3)


def keys():
    keyboard = Controller()
    keyboard.press(Key.space)
    keyboard.release(Key.space)
keys()
sleep(3 )

def hit(key):
    pyautogui.keyDown(key)
    return

def isCollide(data):
    # Draw the rectangle for birds
    for i in range(260, 310):
        for j in range(266, 363):
            if data[i, j] < 100:
                hit("down")
                return

    for i in range(99,120 ):
        for j in range(421, 514):
            if data[i, j] < 100:
                hit("up")
                return
    return

if __name__ == "__main__":
    print("Hey.. Dino game about to start in 3 seconds")
    time.sleep(2)
    # hit('up') 

    while True:
    
        image = ImageGrab.grab().convert('L')  
        data = image.load()
        isCollide(data)
   
        # print(asarray(image))
    
        #Draw the rectangle for cactus
        for i in range(174, 206):
            for j in range(417, 503):
                data[i, j] = 0
        
        # Draw the rectangle for birds
        for i in range(270, 335):
            for j in range(241, 329):
                data[i, j] = 171

        image.save('googel.jpg')
        break
      