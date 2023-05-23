
def DebugTxt(message):
    with open("Debug.txt", "a") as arquivo:
                arquivo.write(message)

def DebugOff(message):
        return 