import pyautogui
from time import time

if __name__=="__main__":
    fish_time=int(input("input a time: ").strip())
    b=time()
    e=time()
    while e-b<fish_time*60:
        pyautogui.click(100, 100)
        e=time()
    print("success!")
