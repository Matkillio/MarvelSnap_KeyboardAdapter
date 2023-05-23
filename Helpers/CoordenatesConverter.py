import pyautogui

class CoordenatesConverter:
    def __init__(self):
        self.OriginalWidth = 1900
        self.OriginalHeight = 1200
        self.ResolutionWidth = pyautogui.size()[0]
        self.ResolutionHeight = pyautogui.size()[1]
        
    def ConvertCoordenate(self, x, y):

        ConvertedX = (x * self.ResolutionWidth) / self.OriginalWidth
        ConvertedY = (y * self.ResolutionHeight) / self.OriginalHeight
        
        return ConvertedX, ConvertedY