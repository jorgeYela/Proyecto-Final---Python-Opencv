import cv2
import numpy as np
import time
import pyautogui

def funcTRACKBAR(x):
    pass

def calcularTopos(contornos, nombre):
    
    if nombre=="morado": 
    
        for c in contornos:
        
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            print(radius)
            
            if int(radius)>45 and x >200
            
                cv2.circle(screenshot, (int(x), int(y)), 50,(0, 255, 0), 5)
                pyautogui.click(x+2,y+250)
                pyautogui.click(x+2,y+250)
    
    if nombre=="rojo": 
    
        for c in contornos:
        
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            print(radius)
            
            if int(radius)>45 and x >200:
            
                cv2.circle(screenshot, (int(x), int(y)), 50,(0, 255, 0), 5)
                pyautogui.click(x+2,y+250)
                pyautogui.click(x+2,y+250)

    if nombre=="azul": 
        
        for c in contornos:
            
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            print(radius)
            
            if int(radius)>50 and x >200:
            
                cv2.circle(screenshot, (int(x), int(y)), 50,(0, 255, 0), 5)
                pyautogui.click(x+2,y+250)
                pyautogui.click(x+2,y+250)

    if nombre=="plomo": 
    
        for c in contornos:
        
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            print(radius)
            
            if int(radius)>50 and x >200:
            
                cv2.circle(screenshot, (int(x), int(y)), 50,(0, 255, 0), 5)
                pyautogui.click(x+2,y+250)
                pyautogui.click(x+2,y+250)

    if nombre=="cafe": 
    
        for c in contornos:
            
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            print(radius)
            
            if int(radius)>55 and x >200:
            
                cv2.circle(screenshot, (int(x), int(y)), 50,(0, 255, 0), 5)
                pyautogui.click(x+2,y+250)
                pyautogui.click(x+2,y+250)

    if nombre=="amarillo": 
    
        for c in contornos:
        
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            print(radius)
            
            if int(radius)>50 and x >200:
            
                cv2.circle(screenshot, (int(x), int(y)), 50,(0, 255, 0), 5)
                pyautogui.click(x+2,y+250)
                pyautogui.click(x+2,y+250)
                
print('Iniciamos') 
time.sleep(3)

while True:

    screenshot = pyautogui.screenshot(region=(2, 250, 900, 800))
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
    hsv = cv2.cvtColor(screenshot, cv2.COLOR_BGR2HSV) 
    listaNombres = ["morado","rojo","azul","plomo","cafe","amarillo"]
    listaColorOscuro=[[123,132,0],[103,159,152],[0,29,0],[0,0,55],[78,66,7],[84,173,137]]
    lisaColorBrillante=[[180,244,196],[122,255,241],[69,255,255],[180,143,193],[116,255,153],[115,255,255]]
    
    for i in range(len(listaColorOscuro)):
    
        nombre = listaNombres[i]
        
        color_oscuro = np.array(listaColorOscuro[i])
        color_brillante = np.array(lisaColorBrillante[i])
        
        #Umbralizacion
        mascara = cv2.inRange(hsv,color_oscuro,color_brillante)
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
        
        kernel = np.ones((15,15),np.uint8)
        apertura = cv2.morphologyEx(mascara, cv2.MORPH_OPEN, kernel)
        
        contornos, _ = cv2.findContours(apertura,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        
        if len(contornos)>1 :
            calcularTopos(contornos, nombre)
     
    resized = cv2.resize(screenshot, (300,300))
    resized2 = cv2.resize(apertura, (300,300))
    cv2.imshow('CAPTURA', resized)         
    cv2.imshow('HSV', resized2) 

    k = cv2.waitKey(1)
    if k==27:
        cv2.destroyAllWindows()
        break
