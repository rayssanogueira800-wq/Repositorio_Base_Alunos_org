import pyautogui as at 

at.hotkey("win","r") 
at.write("chorme", 0.2) 
at.press("enter") 
at.sleep(3)
at.mouseDown(0,0)
at.moveTo(500,500)

import pyautogui as at 

at.hotkey("win","r") #Essa função aperta duas teclas ao mesmo tempo.
programa = at.prompt("Digite nome do programa que deseja abrir: ")
at.write(programa, 0.2) #Essa função escreve 
at.press("enter") #Essa função pressiona atecla.