import pyautogui as py
import time






def clicarImg(url):
    img = py.locateCenterOnScreen(url,confidence=0.9)
    print(img)


    
    while img is None:
        print('não encontrado')
        img = py.locateCenterOnScreen(url,confidence=0.9)
        print(img)
    
    py.click(img.x, img.y)
    print('Encontrado com Sucesso!!!')
    




clicarImg('ytb.png')