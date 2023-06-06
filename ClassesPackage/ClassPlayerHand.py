import pyautogui
from .ClassCoordinates import MatrixCoordinates
from Helpers.Debug import DebugTxt as Debug

class MaoJogador:
    def __init__(self):
        self.NumberOfCards = 4
    
    def setNumberOfCards(self, NumberOfCards):
         self.NumberOfCards = NumberOfCards

    def SelectCard(self, PressedKey):
            Debug("Escolher carta start \n")
            if int(PressedKey) <= self.NumberOfCards and self.NumberOfCards > 0:
                Debug("Carta valida")
                CardCoordinate = MatrixCoordinates[self.NumberOfCards - 1][int(PressedKey) - 1]
                Debug("Coordenadas: X = " + str(CardCoordinate.X) + " Y = " + str(CardCoordinate.Y) + "\n")
                pyautogui.moveTo(CardCoordinate.X, CardCoordinate.Y)
                pyautogui.mouseDown()
                return True
            else:
                 Debug("EscolherCarta end \n")
                 return False