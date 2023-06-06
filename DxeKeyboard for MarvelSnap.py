import time
import pyautogui
import keyboard
import ClassesPackage
from ClassesPackage import ClassMaoJogador
from ClassesPackage import ClassTerreno

if (False):
    from Debug import DebugTxt as Debug
else:
    from Helpers.Debug import DebugOff as Debug

TERRENO1_X = 746
TERRENO2_X = 965
TERRENO3_X = 1178
TERRENOS_Y = 770
N_CARTAS_INICIAIS = 4
CartaEscolhida = False

Terreno1 = ClassTerreno.Terreno(TERRENO1_X, TERRENOS_Y, 0)
Terreno2 = ClassTerreno.Terreno(TERRENO2_X, TERRENOS_Y, 0)
Terreno3 = ClassTerreno.Terreno(TERRENO3_X, TERRENOS_Y, 0)
Mao = ClassMaoJogador.MaoJogador()
MaoTemporaria = ClassMaoJogador.MaoJogador()

def ClicarFugir():
    pyautogui.click(587, 1117)
    time.sleep(0.2)
    pyautogui.click(829, 885)

def LongClick(X, Y):
    pyautogui.moveTo(X,Y)
    pyautogui.mouseDown()
    pyautogui.click()
    time.sleep(0.2) 
    pyautogui.mouseUp()

def ResetarJogo():
    Debug("ResetarJogo start\n")
    global Mao
    global MaoTemporaria
    global CartaEscolhida
    MaoTemporaria.setNumeroDeCartas(N_CARTAS_INICIAIS)
    Mao.setNumeroDeCartas(N_CARTAS_INICIAIS)
    CartaEscolhida = False
    return Debug("ResetarJogo end\n")

def ClicarCancelarJogada():
    pyautogui.moveTo(1128, 133) #Move para area vazia
    pyautogui.mouseUp() #Solta o mouse, fazer isso evita que o mouse ja esteja clicado para o proximo passo
    LongClick(961, 1115) #Clica na mana
    time.sleep(0.2) #Aguarda menu da mana abrir
    pyautogui.click(958, 996) #Clica em desfazer todos os movimentos
    return

def ResetarJogada():
    Debug("entrou na funcao ResetarJogada\n")
    global Mao
    global MaoTemporaria
    global CartaEscolhida

    MaoTemporaria.setNumeroDeCartas(Mao.NumeroDeCartas) #Volta mao para estado original
    CartaEscolhida = False #Seta booleado de carta selecionada para falso
    return Debug("ResetarJogada end \n")

def GetTerreno(TerrenoSelecionado):
    Debug("GetTerreno start \n")
    TerrenoRetorno = 0

    #Só existem 3 terrenos
    match TerrenoSelecionado:
        case "1":
            global Terreno1
            TerrenoRetorno = Terreno1
        case "2":
            global Terreno2
            TerrenoRetorno = Terreno2
        case "3":
            global Terreno3
            TerrenoRetorno = Terreno3
        case _:
            TerrenoRetorno = 0
    Debug("GetTerreno end \n")
    return TerrenoRetorno

def KeyOptions(TeclaPressionada):
    global Mao
    global MaoTemporaria
    global CartaEscolhida

    match TeclaPressionada:
        case "space": #Passar a jogada
            Debug("entrou na funcao space\n")
            MaoTemporaria.NumeroDeCartas = MaoTemporaria.NumeroDeCartas + 1
            Mao.setNumeroDeCartas(MaoTemporaria.NumeroDeCartas)
            pyautogui.click(1300, 1100)
            return Debug("space end")
        
        case "s": #Dar Snap
            return pyautogui.click(961, 115)
        
        case "esc": #Cancelar toda a jogada
            Debug("entrou na funcao esc\n")
            ResetarJogada()
            ClicarCancelarJogada()
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
                        Mao.NumeroDeCartas = int(event.name)
                        ResetarJogada()
                        break

            return Debug("e end \n")
        
        case "p": #Funcao debug para Debugar variaveis
            Debug("--------------------------------------------- \n")
            Debug("Mao.NumeroDeCartas = " + str(Mao.NumeroDeCartas) + "\n")
            Debug("MaoTemporaria.NumeroDeCartas = " + str(MaoTemporaria.NumeroDeCartas) + "\n")
            Debug("CartaEscolhida = " + str(CartaEscolhida) + "\n")
            Debug("--------------------------------------------- \n")
        case "r":
            ResetarJogo()

        case "f":
            ClicarFugir()




def MovimentOption(TeclaPressionada):
    global Mao
    global CartaEscolhida

    Debug("Moviment Option start: " + str(CartaEscolhida) + "\n")

    if not CartaEscolhida:
        CartaEscolhida = MaoTemporaria.EscolherCarta(TeclaPressionada)
        Debug("Escolheu a carta: " + str(TeclaPressionada) + "\n")
    else:
        TerrenoSelecionado = GetTerreno(TeclaPressionada)
        Debug("Escolheu o Terreno: " + str(TeclaPressionada) + "\n")
        if TerrenoSelecionado != 0:
            Debug("Terreno Valido \n")
            TerrenoSelecionado.moveTo()
            MaoTemporaria.NumeroDeCartas = MaoTemporaria.NumeroDeCartas - 1
            CartaEscolhida = False

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
    
            
            