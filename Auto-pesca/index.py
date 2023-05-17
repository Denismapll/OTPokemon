import pyautogui as py
import time
import keyboard

r1 = 0
g1 = 0
b1 = 0

py.FAILSAFE = False



def autoPesca ():
    i = 1
    
    while True :
        # time.sleep(5)
        # py.click(1896, 1031)
        # time.sleep(0.5)
        # py.click(1140, 523)
        i = i + 1
        print(i)
        time.sleep(0.01)
        r1, g1, b1 = py.pixel(1896, 1031)
        # print(r1, g1, b1)
        if keyboard.is_pressed('esc'):
            print("voce apertou P")
            break

        img = py.locateOnScreen('bubblex.png', region=(1700, 500, 200, 800), confidence=0.8)

        if (img is not None):
            py.moveTo(img)
            time.sleep(0.01)
            py.click(img)
            py.moveTo(943,446)

        img = py.locateOnScreen('pendant.png', region=(1700, 500, 200, 800), confidence=0.8)

        if (img is not None):
            py.moveTo(img)
            time.sleep(0.01)
            py.click(img)
            py.moveTo(943,446)

            if i%2:
                py.sleep(0.015)
                py.press("1")
                py.click(943,446)
            else:
                
                py.moveTo(1035,451)
                py.sleep(0.2)
                py.press("1")
                py.rightClick(1035,451)

        img = py.locateOnScreen('waterstone.png', region=(1700, 500, 200, 800), confidence=0.8)

        if (img is not None):
            py.moveTo(img)
            time.sleep(0.01)
            py.click(img)

        if (r1 == 78) :
            py.moveTo(1896, 1031)
            time.sleep(0.01)
            py.click(1896, 1031)
            time.sleep(0.025)
            py.click(1896, 1031)

            time.sleep(0.013)
            py.moveTo(775, 533)
            time.sleep(0.025)
            py.click(775, 533)

            r1,g1,b1 = py.pixel(1740, 607)

            py.press('f5')
            py.press('f7')
            py.press('f8')
            py.press('f9')
            py.press('f10')


        py.sleep(0.5)
        py.moveTo(943,446)
        py.sleep(0.015)
        py.rightClick(943,446)
        py.press('f2')
        py.press('f3')
        py.press('f4')
        py.press('f10')
        py.moveTo(1035,451)
        py.sleep(0.015)
        py.rightClick(1035,451)
        py.press('f2')
        py.press('f3')
        py.press('f4')
        py.press('f9')


        img = py.locateOnScreen('vara.png', region=(700 ,400, 200, 200), confidence=0.8)

        if (img is None):
            py.press('3')
            time.sleep(0.02)
            py.moveTo(775, 533)
            time.sleep(0.05)
            py.click(775, 533)
        else : 
            print('nao pescar')
        time.sleep(0.2)

# def pegarColar ():
#     while True:
        
autoPesca()