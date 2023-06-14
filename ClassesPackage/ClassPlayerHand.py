import pyautogui
from .ClassCoordinates import MatrixCoordinates

class MaoJogador:
    def __init__(self):
        self.NumberOfCards = 4
    
    def setNumberOfCards(self, NumberOfCards):
         self.NumberOfCards = NumberOfCards

    def SelectCard(self, PressedKey):
            if int(PressedKey) <= self.NumberOfCards and self.NumberOfCards > 0:
                CardCoordinate = MatrixCoordinates[self.NumberOfCards - 1][int(PressedKey) - 1]
                pyautogui.moveTo(CardCoordinate.X, CardCoordinate.Y)
                pyautogui.mouseDown()
                return True
            else:
                 return False