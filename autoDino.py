''' Code by Prashik Gavali and suitable for his desktop only. But if you have to try it on yours then change the draw rectangle feature according to your PC '''
import pyautogui
from PIL import Image, ImageGrab  # used to take screenshot
import time

def hit(key):
    pyautogui.keyDown(key)

def isCollide(data):
    # draw rectangle for birds
    for i in range(180, 215):
        for j in range(300, 350):
            if data[i, j] > 100:
                hit('down')
                return 
    # draw rectangle for cactus
    for i in range(180, 215):
        for j in range(415, 450):
            if data[i, j] > 100:
                hit('up')
                return 
    return 

def takeScreenShot():
    img = ImageGrab.grab().convert('L')  # convert it into gray scale image
    return img

# main function :
if __name__ == "__main__":
    print("Dino game is about to start in 3 seconds...")
    time.sleep(3)
    hit('up')
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)
