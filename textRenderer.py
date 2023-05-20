from colorama import just_fix_windows_console

RESETCOLOR = 0
BLACK = 1
RED = 2
GREEN = 3
YELLOW = 4
BLUE = 5
MAGENTA = 6
CYAN = 7
WHITE = 8

def GetColorCode(foreground, background):
    foreColor = 0
    backColor = 0
    if (foreground == 0 or foreground > 8):
        foreColor = 39
    else:
        foreColor = 29 + foreground

    if (background == 0 or background > 8):
        backColor = 49
    else:
        backColor = 39 + background

    return f"\033[{foreColor};{backColor}m"

def GetColorCodeFromNum(colorNum):
    return GetColorCode((colorNum & 240) >> 4, colorNum & 15)

def GetColorNum(foreground, background):
    if (foreground < 0 or foreground > 8):
        foreground = 0

    if (background < 0 or background > 8):
        background = 0

    return (foreground << 4) + background

class TextRenderer:
    def __init__(self, sizeX, sizeY):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.cursorX = 0
        self.cursorY = 0
        self.textBfr = [' '] * (sizeX * sizeY)
        self.colorBfr = [0] * (sizeX * sizeY)
        
    def Resize(self, newX, newY):
        self.sizeX = newX
        self.sizeY = newY
        self.textBfr = [' '] * (newX * newY)
        self.colorBfr = [0] * (newX * newY)

    def FillChar(self, char, x1, y1, x2, y2):
        for y in range(y1, y2):
            for x in range(x1, x2):
                self.textBfr[y * self.sizeX + x] = char

    def FillCharAll(self, char):
        self.textBfr = [char] * (self.sizeX * self.sizeY)

    def FillColor(self, color, x1, y1, x2, y2):
        for y in range(y1, y2):
            for x in range(x1, x2):
                self.colorBfr[y * self.sizeX + x] = color

    def FillColorAll(self, color):
        self.colorBfr = [color] * (self.sizeX * self.sizeY)

    def Print(self):
        temp = ""
        curColor = 0
        for y in range(self.sizeY):
            for x in range(self.sizeX):
                if (self.colorBfr[y * self.sizeX + x] != curColor):
                    curColor = self.colorBfr[y * self.sizeX + x]
                    temp += GetColorCodeFromNum(curColor)
                    print("zmiana koloru")
                temp += self.textBfr[y * self.sizeX + x]
            #temp = temp.join(self.textBfr[y * self.sizeX:(y + 1) * self.sizeX:])
            print(temp, end="\n")
            temp = ""
        print("\033[0m")

if (__name__ == "__main__"):
    just_fix_windows_console()
    testRenderer = TextRenderer(10, 3)
    testRenderer.FillCharAll("a")
    testRenderer.FillColorAll(GetColorNum(RED, RESETCOLOR))
    print(testRenderer.textBfr)
    testRenderer.Print()