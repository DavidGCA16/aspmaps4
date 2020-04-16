#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pyautogui
import time
import nombres
correo="prueba@test.com"
passwd="123456789"
i=0
def prueba(data1,data2,num):
    correo=data1
    passwd=data2
    numero=num
    pyautogui.click(50,80)
    time.sleep(1)
    pyautogui.write("nordvpn connect us")
    pyautogui.press("enter")
    time.sleep(10)

    #pyautogui.moveTo(1900,110, duration=1)
    pyautogui.click(1900,110)
    time.sleep(1)
    pyautogui.click(1900,250)
    time.sleep(2)
    pyautogui.click(1000,110)

    pyautogui.write("store.playstation.com")
    pyautogui.press("enter")
    time.sleep(22)
    pyautogui.click(1700,185)
    #pyautogui.moveTo(1000,590)

    time.sleep(10)
    pyautogui.click(1000,590)
    pyautogui.hotkey('altright','2')
    pyautogui.write(correo)
    #pyautogui.moveTo(1000,610)
    time.sleep(2)
    pyautogui.click(1000,610)
    pyautogui.write(passwd)
    time.sleep(1)
    pyautogui.click(1000,700)
    time.sleep(10)
    pyautogui.screenshot()
    im1 = pyautogui.screenshot()
    kk=str(numero)
    dire="/recoleccion/"+kk+".png"
    im1.save(r"/home/dav/Documentos/popo.png")
    nombres.cambiar(numero)
    pyautogui.click(1900,50)
    time.sleep(2)

    
def datos():
    i=0
    f = open("xay.txt", "r")
    while(True):
        i=i+1
        linea = f.readline()
        #print(linea)
        data=linea.split(":")
        print(data[0])
        print(data[1])
        prueba(data[0],data[1],i)
        if not linea:
            break
    f.close()

datos()
