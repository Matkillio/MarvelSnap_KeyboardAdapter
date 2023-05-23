import pyautogui

class Terreno:
    def __init__(self, CoordenadaX, CoordenadaY, NumeroDeCartas):
        self.CoordenadaX = CoordenadaX
        self.CoordenadaY = CoordenadaY
        self.NumeroDeCartas = NumeroDeCartas
    
    def moveTo(self):
        pyautogui.moveTo(self.CoordenadaX, self.CoordenadaY)
        pyautogui.mouseUp()