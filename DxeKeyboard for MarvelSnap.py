import time
import pyautogui
import keyboard
import ClassesPackage
from ClassesPackage import ClassPlayerHand
from ClassesPackage import ClassLocation
import Helpers
from Helpers import CoordinatesConverter as Converter

if (False):
    from Debug import DebugTxt as Debug
else:
    from Helpers.Debug import DebugOff as Debug

cc = Converter.CoordinatesConverter()

LOCATION1_X = cc.ConvertedX(711)
LOCATION2_X = cc.ConvertedX(967)
LOCATION3_X = cc.ConvertedX(1246)
LOCATIONS_Y = cc.ConvertedY(770)
N_INITIAL_CARDS = 4
SelectedCard = False

Location1 = ClassLocation.Location(LOCATION1_X, LOCATIONS_Y, 0)
Location2 = ClassLocation.Location(LOCATION2_X, LOCATIONS_Y, 0)
Location3 = ClassLocation.Location(LOCATION3_X, LOCATIONS_Y, 0)
Hand = ClassPlayerHand.PlayerHand()
TempHand = ClassPlayerHand.PlayerHand()

def ClickRetreat():
    pyautogui.click(cc.ConvertedXY(172, 1105))
    time.sleep(0.2)
    pyautogui.click(cc.ConvertedXY(1086, 890))

def LongClick(X, Y):
    pyautogui.moveTo(X,Y)
    pyautogui.mouseDown()
    pyautogui.click()
    time.sleep(0.2) 
    pyautogui.mouseUp()

def ResetGame():
    global Hand
    global TempHand
    global SelectedCard
    TempHand.setNumberOfCards(N_INITIAL_CARDS)
    Hand.setNumberOfCards(N_INITIAL_CARDS)
    SelectedCard = False
    return Debug("ResetarJogo end\n")

def ClickCancelPlay():
    pyautogui.moveTo(cc.ConvertedXY(1679, 365)) #Move any selected card to an empty space
    pyautogui.mouseUp() #This avoids the mouse being clicked down for the next step
    LongClick(cc.ConvertedX(310),cc.ConvertedY(776)) #Click on your energy
    time.sleep(0.1) #Waits for the menu to open
    pyautogui.click(cc.ConvertedXY(952, 1003)) #Click undo moves
    pyautogui.click(cc.ConvertedXY(1679, 365)) #Click outside menu to return to gameplay
    return

def ResetPlay():
    global Hand
    global TempHand
    global SelectedCard

    TempHand.setNumberOfCards(Hand.NumberOfCards) #Returns hand to its original state
    SelectedCard = False #card not selected
    return Debug("ResetPlay end \n")

def GetLocation(SelectedLocation):
    ReturnLocation = 0

    match SelectedLocation:
        case "1":
            global Location1
            ReturnLocation = Location1
        case "2":
            global Location2
            ReturnLocation = Location2
        case "3":
            global Location3
            ReturnLocation = Location3
        case _:
            ReturnLocation = 0
    Debug("GetLocation end \n")
    return ReturnLocation

def KeyOptions(PressedKey):
    global Hand
    global TempHand
    global SelectedCard

    match PressedKey:
        case "space" | "enter": #End turn
            CardsNumber = TempHand.NumberOfCards + 1
            if(CardsNumber <= 7):
                TempHand.NumberOfCards = CardsNumber
                Hand.setNumberOfCards(TempHand.NumberOfCards)
            pyautogui.click(cc.ConvertedXY(1730, 1105))
            return Debug("enter end")
        case "s": #Snap
            return pyautogui.click(cc.ConvertedXY(1588, 775))
        
        case "esc": #Cancel whole play
            ResetPlay()
            ClickCancelPlay()
            return Debug("esc end \n")
        
        case "e": #Edit number of card in hand
            while True:
                Debug("Waiting number of cards - Editing hand... \n")
                event = keyboard.read_event()

                if event.event_type == keyboard.KEY_UP and event.name.isnumeric():
                    if(int(event.name) <= 7):
                        Debug("Pressed Key: " + event.name + "\n")
                        Hand.NumberOfCards = int(event.name)
                        ResetPlay()
                        break

            return Debug("e end \n")
        
        case "p": #Function to debug variables
            Debug("--------------------------------------------- \n")
            Debug("Hand.NumberOfCards = " + str(Hand.NumberOfCards) + "\n")
            Debug("TempHand.NumberOfCards = " + str(TempHand.NumberOfCards) + "\n")
            Debug("SelectedCard = " + str(SelectedCard) + "\n")
            Debug("--------------------------------------------- \n")
        case "r": #Reset hand, sets number of cards to 4
            ResetGame()

        case "f": #Retreat
            ClickRetreat()

def MovimentOption(PressedKey):
    global Hand
    global SelectedCard

    Debug("Moviment Option start: " + str(SelectedCard) + "\n")

    if not SelectedCard:
        SelectedCard = TempHand.SelectCard(PressedKey)
        Debug("Card selected: " + str(PressedKey) + "\n")
    else:
        SelectedLocation = GetLocation(PressedKey)
        Debug("Selected Location: " + str(PressedKey) + "\n")
        if SelectedLocation != 0:
            Debug("Valid Location \n")
            SelectedLocation.moveTo()
            TempHand.NumberOfCards = TempHand.NumberOfCards - 1
            SelectedCard = False

while True:
    Debug("Waiting initial input... \n")
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_UP:
        Debug("Pressed key: " + event.name + "\n")
        if not event.name.isnumeric():
            Debug("Character \n")
            KeyOptions(event.name)
        else:
            Debug("Number \n")
            MovimentOption(event.name)