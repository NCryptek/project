from colorama import just_fix_windows_console
import os
from sys import platform

RESETCOLOR = 0
BLACK = 1
RED = 2
GREEN = 3
YELLOW = 4
BLUE = 5
MAGENTA = 6
CYAN = 7
WHITE = 8

CORNER_TL = "┌"
CORNER_TR = "┐"
CORNER_BL = "└"
CORNER_BR = "┘"
INTER_VERT_R = "├"
INTER_VERT_L = "┤"
INTER_HORZ_B = "┬"
INTER_HORZ_T = "┴"
INTER_QUAD = "┼"
LINE_VERT = "│"
LINE_HORZ = "─"

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

def clearScreen():
    if platform == "linux" or platform == "linux2":
        os.system("clear")
    elif platform == "win32":
        os.system("cls")

def setCursorPos(x, y):
    print(f"\033[{y};{x}H", end="")

def resetCursorPos():
    print("\033[0;0H", end="")

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

    def SetCursorPos(self, newX, newY):
        self.cursorX = newX
        self.cursorY = newY
        setCursorPos(newX, newY)

    def FillChar(self, char, x1, y1, x2, y2):
        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                self.textBfr[y * self.sizeX + x] = char

    def FillCharAll(self, char):
        self.textBfr = [char] * (self.sizeX * self.sizeY)

    def InsertText(self, text, x, y, wrapText = False):
        startInd = y * self.sizeX + x
        textLen = len(text)
        if (not wrapText and x + textLen > self.sizeX):
            textLen = self.sizeX - x

        for i in range(textLen):
            self.textBfr[startInd + i] = text[i]

    def InsertTextSpecial(self, text, x1, y1, x2, y2, wrapText = False):
        textInd = 0
        textLen = len(text)
        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                if (textInd >= textLen): #zakończ działanie funkcji jeśli tekst się skończył
                    return
                
                if (text[textInd] == "\n"): #przejście do następnej linii jeśli jest znak \n
                    textInd += 1
                    break
                elif (text[textInd] == "\0"): #zakończenie wpisywania tekstu jeśli jest znak \0
                    return
                else:
                    self.textBfr[y * self.sizeX + x] = text[textInd]
                    textInd += 1
                    if (x == x2 and (not wrapText)):
                        while (text[textInd] != "\n" and text[textInd] != "\0"):
                            textInd += 1
                        #endwhile
                    #endif
                #endif
            #endfor
        #endfor
    #enddef InsertTextSpecial

    def FillColor(self, color, x1, y1, x2, y2):
        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                self.colorBfr[y * self.sizeX + x] = color

    def FillColorAll(self, color):
        self.colorBfr = [color] * (self.sizeX * self.sizeY)

    def GenGrid(self, x1, y1, x2, y2, cellWidth, cellHeight):
        for y in range(y1, y2):
            if (y < 0 or y + 1 > self.sizeY):
                continue
            for x in range(x1, x2):
                if (x < 0 or x + 1 > self.sizeX):
                    continue
                #górna ściana
                if (y == y1):
                    if (x == x1):
                        self.textBfr[y * self.sizeX + x] = CORNER_TL
                    elif (x == x2 - 1):
                        self.textBfr[y * self.sizeX + x] = CORNER_TR
                    elif ((x - x1) % (cellWidth + 1) == 0):
                        self.textBfr[y * self.sizeX + x] = INTER_HORZ_B
                    else:
                        self.textBfr[y * self.sizeX + x] = LINE_HORZ
                #dolna ściana
                elif (y == y2 - 1):
                    if (x == x1):
                        self.textBfr[y * self.sizeX + x] = CORNER_BL
                    elif (x == x2 - 1):
                        self.textBfr[y * self.sizeX + x] = CORNER_BR
                    elif ((x - x1) % (cellWidth + 1) == 0):
                        self.textBfr[y * self.sizeX + x] = INTER_HORZ_T
                    else:
                        self.textBfr[y * self.sizeX + x] = LINE_HORZ
                #środek przecięcia
                elif ((y - y1) % (cellHeight + 1) == 0):
                    if (x == x1):
                        self.textBfr[y * self.sizeX + x] = INTER_VERT_R
                    elif (x == x2 - 1):
                        self.textBfr[y * self.sizeX + x] = INTER_VERT_L
                    elif ((x - x1) % (cellWidth + 1) == 0):
                        self.textBfr[y * self.sizeX + x] = INTER_QUAD
                    else:
                        self.textBfr[y * self.sizeX + x] = LINE_HORZ
                #środek bez przecięć
                else:
                    if ((x - x1) % (cellWidth + 1) == 0):
                        self.textBfr[y * self.sizeX + x] = LINE_VERT
                    else:
                        self.textBfr[y * self.sizeX + x] = " "

    def Print(self):
        temp = ""
        curColor = 0
        for y in range(self.sizeY):
            print(GetColorCodeFromNum(curColor), end="")
            for x in range(self.sizeX):
                if (self.colorBfr[y * self.sizeX + x] != curColor):
                    curColor = self.colorBfr[y * self.sizeX + x]
                    temp += GetColorCodeFromNum(curColor)
                temp += self.textBfr[y * self.sizeX + x]
            #temp = temp.join(self.textBfr[y * self.sizeX:(y + 1) * self.sizeX:])
            print(temp, "\033[49m", end="\n", sep="")
            temp = ""
        self.cursorX = 0
        self.cursorY += self.sizeY
        print("\033[39;49m")

    def Overwrite(self):
        self.cursorX = 0
        self.cursorY = 0
        print("\033[0;0H", end="")
        self.Print()

    def ClearBuffers(self):
        self.textBfr = [' '] * (self.sizeX * self.sizeY)
        self.colorBfr = [0] * (self.sizeX * self.sizeY)

    def ClearScreen(self):
        self.textBfr = [' '] * (self.sizeX * self.sizeY)
        self.colorBfr = [0] * (self.sizeX * self.sizeY)
        self.cursorX = 0
        self.cursorY = 0
        clearScreen()

if (__name__ == "__main__"):
    just_fix_windows_console()
    testRenderer = TextRenderer(41, 21)
    testRenderer.GenGrid(0, 0, 41, 21, 3, 1)
    #testRenderer.FillCharAll("a")
    #testRenderer.InsertText("Hello World!", 2, 0)
    testRenderer.FillColorAll(GetColorNum(RED, GREEN))
    testRenderer.Print()