import time
import pyautogui
import keyboard
import ClassesPackage
from ClassesPackage import ClassPlayerHand
from ClassesPackage import ClassLocation

if (False):
    from Debug import DebugTxt as Debug
else:
    from Helpers.Debug import DebugOff as Debug

LOCATION1_X = 746
LOCATION2_X = 965
LOCATION3_X = 1178
LOCATIONS_Y = 770
N_INITIAL_CARDS = 4
SelectedCard = False

Location1 = ClassLocation.Location(LOCATION1_X, LOCATIONS_Y, 0)
Location2 = ClassLocation.Location(LOCATION2_X, LOCATIONS_Y, 0)
Location3 = ClassLocation.Location(LOCATION3_X, LOCATIONS_Y, 0)
Hand = ClassPlayerHand.MaoJogador()
TempHand = ClassPlayerHand.MaoJogador()

def ClickRetreat():
    pyautogui.click(587, 1117)
    time.sleep(0.2)
    pyautogui.click(829, 885)

def LongClick(X, Y):
    pyautogui.moveTo(X,Y)
    pyautogui.mouseDown()
    pyautogui.click()
    time.sleep(0.2) 
    pyautogui.mouseUp()

def ResetGame():
    Debug("ResetarJogo start\n")
    global Hand
    global TempHand
    global SelectedCard
    TempHand.setNumberOfCards(N_INITIAL_CARDS)
    Hand.setNumberOfCards(N_INITIAL_CARDS)
    SelectedCard = False
    return Debug("ResetarJogo end\n")

def ClickCancelPlay():
    pyautogui.moveTo(1128, 133) #Move para area vazia
    pyautogui.mouseUp() #Solta o mouse, fazer isso evita que o mouse ja esteja clicado para o proximo passo
    LongClick(961, 1115) #Clica na mana
    time.sleep(0.2) #Aguarda menu da mana abrir
    pyautogui.click(958, 996) #Clica em desfazer todos os movimentos
    return

def ResetPlay():
    Debug("entrou na funcao ResetarJogada\n")
    global Hand
    global TempHand
    global SelectedCard

    TempHand.setNumberOfCards(Hand.NumberOfCards) #Volta mao para estado original
    SelectedCard = False #Seta booleado de carta selecionada para falso
    return Debug("ResetarJogada end \n")

def GetLocation(SelectedLocation):
    Debug("GetTerreno start \n")
    ReturnLocation = 0

    #Só existem 3 terrenos
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
    Debug("GetTerreno end \n")
    return ReturnLocation

def KeyOptions(PressedKey):
    global Hand
    global TempHand
    global SelectedCard

    match PressedKey:
        case "space": #Passar a jogada
            Debug("entrou na funcao space\n")
            TempHand.NumberOfCards = TempHand.NumberOfCards + 1
            Hand.setNumberOfCards(TempHand.NumberOfCards)
            pyautogui.click(1300, 1100)
            return Debug("space end")
        
        case "s": #Dar Snap
            return pyautogui.click(961, 115)
        
        case "esc": #Cancelar toda a jogada
            Debug("entrou na funcao esc\n")
            ResetPlay()
            ClickCancelPlay()
            return Debug("esc end \n")
        
        case "e": #Editar numero de cartas na mao
            Debug("entrou na funcao e \n")
            #ClicarCancelarJogada()

            while True:
                Debug("Aguardando tecla para editar a mao... \n")
                event = keyboard.read_event()

                if event.event_type == keyboard.KEY_UP and event.name.isnumeric():
                    if(int(event.name) <= 7):
                        Debug("Tecla pressionada: " + event.name + "\n")
                        Hand.NumberOfCards = int(event.name)
                        ResetPlay()
                        break

            return Debug("e end \n")
        
        case "p": #Funcao debug para Debugar variaveis
            Debug("--------------------------------------------- \n")
            Debug("Hand.NumberOfCards = " + str(Hand.NumberOfCards) + "\n")
            Debug("TempHand.NumberOfCards = " + str(TempHand.NumberOfCards) + "\n")
            Debug("SelectedCard = " + str(SelectedCard) + "\n")
            Debug("--------------------------------------------- \n")
        case "r":
            ResetGame()

        case "f":
            ClickRetreat()

def MovimentOption(TeclaPressionada):
    global Hand
    global SelectedCard

    Debug("Moviment Option start: " + str(SelectedCard) + "\n")

    if not SelectedCard:
        SelectedCard = TempHand.SelectCard(TeclaPressionada)
        Debug("Escolheu a carta: " + str(TeclaPressionada) + "\n")
    else:
        TerrenoSelecionado = GetLocation(TeclaPressionada)
        Debug("Escolheu o Terreno: " + str(TeclaPressionada) + "\n")
        if TerrenoSelecionado != 0:
            Debug("Terreno Valido \n")
            TerrenoSelecionado.moveTo()
            TempHand.NumberOfCards = TempHand.NumberOfCards - 1
            SelectedCard = False

while True:
    Debug("Aguardando tecla inicial... \n")
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_UP:
        Debug("Tecla pressionada: " + event.name + "\n")
        if not event.name.isnumeric():
            Debug("Caracteres \n")
            KeyOptions(event.name)
        else:
            Debug("Numerico \n")
            MovimentOption(event.name)