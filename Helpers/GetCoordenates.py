import pyautogui
import keyboard

x, y = 0, 0 
key = 'f'

#Captura x e y
def check_action(event):
        if event == key:
            x = pyautogui.position().x
            y = pyautogui.position().y
            with open("Coordenadas.txt", "a") as arquivo:
                arquivo.write("x = " + str(x) + " y = " + str(y) + "\n")

while True:
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_UP:
        check_action(event.name)
    