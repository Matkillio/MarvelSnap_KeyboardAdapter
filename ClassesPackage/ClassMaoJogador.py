import pyautogui
from .ClassCoordenadas import MatrizCoordenadas
from Helpers.Debug import DebugTxt as Debug

class MaoJogador:
    def __init__(self):
        self.NumeroDeCartas = 4
    
    def setNumeroDeCartas(self, NumeroDeCartas):
         self.NumeroDeCartas = NumeroDeCartas

    def EscolherCarta(self, TeclaPressionada):
            Debug("Escolher carta start \n")
            if int(TeclaPressionada) <= self.NumeroDeCartas and self.NumeroDeCartas > 0:
                Debug("Carta valida")
                CoordenadaCarta = MatrizCoordenadas[self.NumeroDeCartas - 1][int(TeclaPressionada) - 1]
                Debug("Coordenadas: X = " + str(CoordenadaCarta.X) + " Y = " + str(CoordenadaCarta.Y) + "\n")
                pyautogui.moveTo(CoordenadaCarta.X, CoordenadaCarta.Y)
                pyautogui.mouseDown()
                return True
            else:
                 Debug("EscolherCarta end \n")
                 return False