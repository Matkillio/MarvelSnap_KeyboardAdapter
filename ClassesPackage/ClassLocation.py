import pyautogui

class Location:
    def __init__(self, CoordinateX, CoordinateY, NumberOfCards):
        self.CoordinateX = CoordinateX
        self.CoordinateY = CoordinateY
        self.NumberOfCards = NumberOfCards
    
    def moveTo(self):
        pyautogui.moveTo(self.CoordinateX, self.CoordinateY)
        pyautogui.mouseUp()