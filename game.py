import globals
import unit
import textRenderer
from time import sleep
import keyboard
import random
import colorama

prevPosX = []
prevPosY = []
curSelect = 0
curX = 0
curY = 0
gridSizeX = 0
gridSizeY = 0

def CenterCam(unit):
    globals.camOffsetX = max(0, min(unit.posX - int(globals.camSizeX / 2), globals.mapSizeX - globals.camSizeX))
    globals.camOffsetY = max(0, min(unit.posY - int(globals.camSizeY / 2), globals.mapSizeX - globals.camSizeX))

def CenterCamPos(x, y):
    globals.camOffsetX = max(0, min(x - int(globals.camSizeX / 2), globals.mapSizeX - globals.camSizeX))
    globals.camOffsetY = max(0, min(y - int(globals.camSizeY / 2), globals.mapSizeX - globals.camSizeX))

def FillTileColor(x, y, foreground, background):
    if (x < 0 or x >= globals.camSizeX or y < 0 or y >= globals.camSizeY):
        return

    globals.defaultRenderer.FillColor(background, x * 4, y * 2, (x + 1) * 4, (y + 1) * 2)
    globals.defaultRenderer.SetColor((foreground << 4) + background, x * 4 + 2, y * 2 + 1)

def StartGame():
    global gridSizeX, gridSizeY
    gridSizeX = globals.camSizeX * 4 + 1
    gridSizeY = globals.camSizeY * 2 + 1
    
    globals.defaultRenderer.Resize(max(max(27 + globals.longestUnitName, 44), globals.camSizeX * 4 + 1), globals.camSizeY * 2 + 1 + 13) #+13 na dodatkowe informacje
    curX = 0
    curY = 0
    curSelect = 0
    for i in globals.unitList:
        prevPosX.append(i.posX)
        prevPosY.append(i.posY)

    globals.gameState = 1
    globals.gameRunning = True
    
    textRenderer.clearScreen()
    GameLoop()

def GameLoop():
    lastKey = ""
    while (globals.gameRunning == True):
        if (not KeyHandler_Basic(lastKey)): # jeśli naciśnięty klawisz nie jest obsłużony przez podstawową funkcję
            if (globals.gameState == 2):  #ruch
                KeyHandler_Move(lastKey)
            elif (globals.gameState == 3):  #atak
                KeyHandler_Attack(lastKey)
            elif (globals.gameState == 4):  #ruch kamerą
                KeyHandler_Camera(lastKey)
        elif (not globals.gameRunning): # jeśli klawisz został obsłużony przez podstawową funkcję i spowodował on zakończenie gry
            break

        RenderMap()
        newKey = keyboard.read_key()
        if (newKey == lastKey):
            lastKey = ""
        else:
            lastKey = newKey
        sleep(0.016)

def EndTurn():
    for i in globals.unitList:
        i.moveRem = i.speed

        prevPosX.append(i.posX)
        prevPosY.append(i.posY)

def KeyHandler_Basic(key):
    global curX, curY, curSelect
    handled = False
    if (key == "esc"):
        if (globals.gameState != 1):
            CenterCam(globals.unitList[curSelect])
            globals.gameState = 1
        else:
            QuitPrompt()
        handled = True
        pass
    elif (key == "e"):
        EndTurn()
        globals.gameState = 1
        handled = True
        pass
    elif (key == "m"):
        curX = globals.unitList[curSelect].posX
        curY = globals.unitList[curSelect].posY
        globals.gameState = 2
        handled = True
        pass
    elif (key == "a"):
        curX = globals.unitList[curSelect].posX
        curY = globals.unitList[curSelect].posY
        globals.gameState = 3
        handled = True
        pass
    elif (key == "c"):
        globals.gameState = 4
        handled = True
        pass
    elif (globals.gameState == 1):
        if (key == "up"):
            if (curSelect > 0):
                curSelect -= 1
            else:
                curSelect = globals.startUnitAmt - 1

            if (globals.unitList[curSelect].health > 0):
                CenterCam(globals.unitList[curSelect])
            handled = True
        elif (key == "down"):
            if (curSelect < globals.startUnitAmt - 1):
                curSelect += 1
            else:
                curSelect = 0

            if (globals.unitList[curSelect].health > 0):
                CenterCam(globals.unitList[curSelect])
            handled = True
        elif (key == "1"):
            if (globals.unitList[0].health > 0):
                curSelect = 0
                CenterCam(globals.unitList[0])
            handled = True
        elif (key == "2"):
            if (globals.unitList[1].health > 0):
                curSelect = 1
                CenterCam(globals.unitList[1])
            handled = True
        elif (key == "3"):
            if (globals.unitList[2].health > 0):
                curSelect = 2
                CenterCam(globals.unitList[2])
            handled = True
        elif (key == "4"):
            if (globals.unitList[3].health > 0):
                curSelect = 3
                CenterCam(globals.unitList[3])
            handled = True
        elif (key == "5"):
            if (globals.unitList[4].health > 0):
                curSelect = 4
                CenterCam(globals.unitList[4])
            handled = True
    return handled

def KeyHandler_Move(key):
    handled = False
    global curX, curY, curSelect
    if (key == "up"):
        if (curY > 0):
            curY -= 1
        CenterCamPos(curX, curY)
        handled = True
    elif(key == "down"):
        if (curY < globals.mapSizeY):
            curY += 1
        CenterCamPos(curX, curY)
        handled = True
    elif(key == "right"):
        if (curX < globals.mapSizeX):
            curX += 1
        CenterCamPos(curX, curY)
        handled = True
    elif(key == "left"):
        if (curX > 0):
            curX -= 1
        CenterCamPos(curX, curY)
        handled = True
    elif (key == "1"):
        if (globals.unitList[0].health > 0):
            CenterCam(globals.unitList[0])
            curX = globals.unitList[0].posX
            curY = globals.unitList[0].posY
            curSelect = 0
        handled = True
        pass
    elif (key == "2"):
        if (globals.unitList[1].health > 0):
            CenterCam(globals.unitList[1])
            curX = globals.unitList[1].posX
            curY = globals.unitList[1].posY
            curSelect = 1
        handled = True
        pass
    elif (key == "3"):
        if (globals.unitList[2].health > 0):
            CenterCam(globals.unitList[2])
            curX = globals.unitList[2].posX
            curY = globals.unitList[2].posY
            curSelect = 2
        handled = True
        pass
    elif (key == "4"):
        if (globals.unitList[3].health > 0):
            CenterCam(globals.unitList[3])
            curX = globals.unitList[3].posX
            curY = globals.unitList[3].posY
            curSelect = 3
        handled = True
        pass
    elif (key == "5"):
        if (globals.unitList[4].health > 0):
            CenterCam(globals.unitList[4])
            curX = globals.unitList[4].posX
            curY = globals.unitList[4].posY
            curSelect = 4
        handled = True
    elif (key == "enter"):
        curUnit = globals.unitList[curSelect]
        unitPath = curUnit.pathTo(curX, curY)
        if (len(unitPath) != 0 and len(unitPath) <= curUnit.moveRem):
            curUnit.moveTo(curX, curY)
    
    return handled

def KeyHandler_Attack(key):
    handled = False
    global curX, curY, curSelect
    if (key == "up"):
        if (curY > 0):
            curY -= 1
        CenterCamPos(curX, curY)
        handled = True
    elif(key == "down"):
        if (curY < globals.mapSizeY):
            curY += 1
        CenterCamPos(curX, curY)
        handled = True
    elif(key == "right"):
        if (curX < globals.mapSizeX):
            curX += 1
        CenterCamPos(curX, curY)
        handled = True
    elif(key == "left"):
        if (curX > 0):
            curX -= 1
        CenterCamPos(curX, curY)
        handled = True
    elif (key == "enter"):
        curUnit = globals.unitList[curSelect]
        if (curUnit.health > 0):
            unitAtTarget = globals.GetUnitAt(curX, curY)
            dist = globals.Dist(curUnit.posX, curUnit.posY, unitAtTarget.posX, unitAtTarget.posY)

            if (unitAtTarget != None and unitAtTarget.ownerId != 0 and dist <= curUnit.range): #atak
                unitAtTarget.takeDamage(curUnit.damage, curUnit.damageType)
                if (unitAtTarget.health > 0 and dist <= unitAtTarget.range): #atak odwetowy
                    curUnit.takeDamage(unitAtTarget.damage * 0.5, unitAtTarget.damageType)

        handled = True
    elif (key == "1"):
        pass

    return handled

def KeyHandler_Camera(key):
    global curX, curY, curSelect
    handled = False
    if (key == "left"):
        if (curX > 0):
            curX -= 1
        CenterCamPos(curX, curY)
        handled = True
    elif (key == "up"):
        if (curY > 0):
            curY -= 1
        CenterCamPos(curX, curY)
        handled = True
    elif (key == "right"):
        if (curX < globals.mapSizeX - 1):
            curX += 1
        CenterCamPos(curX, curY)
        handled = True
    elif (key == "down"):
        if (curY < globals.mapSizeY - 1):
            curY += 1
        CenterCamPos(curX, curY)
        handled = True
    elif (key == "1"):
        if (globals.unitList[0].health > 0):
            CenterCam(globals.unitList[0])
        handled = True
        pass
    elif (key == "2"):
        if (globals.unitList[1].health > 0):
            CenterCam(globals.unitList[1])
        handled = True
        pass
    elif (key == "3"):
        if (globals.unitList[2].health > 0):
            CenterCam(globals.unitList[2])
        handled = True
        pass
    elif (key == "4"):
        if (globals.unitList[3].health > 0):
            CenterCam(globals.unitList[3])
        handled = True
        pass
    elif (key == "5"):
        if (globals.unitList[4].health > 0):
            CenterCam(globals.unitList[4])
        handled = True
    
    return handled

def QuitPrompt():
    textRenderer.clearScreen()
    print("\033[1m")
    print(textRenderer.GetColorCode(textRenderer.RED, textRenderer.RESETCOLOR), "Czy napewno chcesz wyjść? Naciśnij enter aby potwierdzić, inny klawisz spowoduje powrót do gry", sep="")
    sleep(0.25)
    key = keyboard.read_key()
    if (key == "enter"):
        globals.gameRunning = False
    textRenderer.clearScreen()

def RenderMap():
    global curX, curY, curSelect, gridSizeX, gridSizeY
    curUnit = globals.unitList[curSelect]
    curTemplate = globals.unitTemplates[curUnit.typeId]
    renderCursorX = (curX - globals.camOffsetX) * 4 + 2
    renderCursorY = (curY - globals.camOffsetY) * 2 + 1

    globals.defaultRenderer.ClearBuffers()
    globals.defaultRenderer.GenGrid(0, 0, gridSizeX, gridSizeY, 3, 1)
    if (globals.camOffsetY > 0):
        globals.defaultRenderer.FillChar("↑", 0, 0, gridSizeX, 0)

    if (globals.camOffsetX + globals.camSizeX < globals.mapSizeX):
        globals.defaultRenderer.FillChar("→", gridSizeX - 1, 0, gridSizeX - 1, gridSizeY - 2)

    if (globals.camOffsetY + globals.camSizeY < globals.mapSizeY):
        globals.defaultRenderer.FillChar("↓", 0, gridSizeY - 1, gridSizeX - 2, gridSizeY - 1)

    if (globals.camOffsetX > 0):
        globals.defaultRenderer.FillChar("←", 0, 0, 0, gridSizeY - 2)

    for i in globals.unitList:
        if (i.health == 0):
            continue
        elif (i.posX < globals.camOffsetX or i.posX >= globals.camOffsetX + globals.camSizeX):
            continue
        elif (i.posY < globals.camOffsetY or i.posY >= globals.camOffsetY + globals.camSizeY):
            continue

        globals.defaultRenderer.SetChar("O", (i.posX - globals.camOffsetX) * 4 + 2, (i.posY - globals.camOffsetY) * 2 + 1)
        if (i.ownerId == 0):
            globals.defaultRenderer.SetColor(textRenderer.GREEN << 4, (i.posX - globals.camOffsetX) * 4 + 2, (i.posY - globals.camOffsetY) * 2 + 1)
        else:
            globals.defaultRenderer.SetColor(textRenderer.RED << 4, (i.posX - globals.camOffsetX) * 4 + 2, (i.posY - globals.camOffsetY) * 2 + 1)

    if (globals.gameState == 1): #domyślny stan
        globals.defaultRenderer.InsertTextSpecial("Escape - wyjście z gry\nE - zakończ turę\nC - ruch kamerą\nM - ruch jednostką\nA - atak jednostką\n1-5 - szybki wybór jednostki", 1, gridSizeY + 1, globals.defaultRenderer.sizeX, gridSizeY + 6)
        if (curUnit.moveRem == 0 or curUnit.health == 0):
            globals.defaultRenderer.FillColor(textRenderer.RED << 4, 1, gridSizeY + 4, globals.defaultRenderer.sizeX, gridSizeY + 5)

        for i in range(globals.startUnitAmt):
            globals.defaultRenderer.InsertText(f"U{i + 1}: {globals.unitTemplates[globals.unitList[i].typeId].displayName}", 1, gridSizeY + 8 + i)
            if (globals.unitList[i].health <= 0):
                globals.defaultRenderer.FillColor(textRenderer.RED, 0, gridSizeY + 7 + i, 5 + globals.longestUnitName, gridSizeY + 7 + i)

        globals.defaultRenderer.SetChar(">", 0, gridSizeY + 8 + curSelect)
        if (curUnit.health > 0):
            globals.defaultRenderer.InsertTextSpecial("Życie:\nAtak:\nZasięg\nRuchy:\nTyp broni:\nTyp pancerza:", 7 + globals.longestUnitName, gridSizeY + 7, globals.defaultRenderer.sizeX, gridSizeY + 13)
            globals.defaultRenderer.InsertTextSpecial(f"{curUnit.health}/{curTemplate.maxHealth}\n{curTemplate.damage}\n{curTemplate.range}\n{curUnit.moveRem}/{curTemplate.speed}\n{unit.warheads[curTemplate.damageType]}\n{unit.armors[curTemplate.armorType]}", 21 + globals.longestUnitName, gridSizeY + 7, globals.defaultRenderer.sizeX, gridSizeY + 13)
            FillTileColor(curUnit.posX - globals.camOffsetX, curUnit.posY - globals.camOffsetY, textRenderer.RESETCOLOR, textRenderer.GREEN)

    elif (globals.gameState == 2): #ruch jednostką
        renderPath = curUnit.pathTo(curX, curY)
        for i in renderPath:
            if (i.cost > curUnit.moveRem): #zaznacza pola przez które przemieści się jednostka na żółto, te które są poza zasięgiem są oznaczone na czerwono
                FillTileColor(i.srcX - globals.camOffsetX, i.srcY - globals.camOffsetY, textRenderer.RESETCOLOR, textRenderer.RED)
            else:
                FillTileColor(i.srcX - globals.camOffsetX, i.srcY - globals.camOffsetY, textRenderer.RESETCOLOR, textRenderer.YELLOW)

        globals.defaultRenderer.SetChar("V", renderCursorX, renderCursorY)
        if (len(renderPath) > curUnit.moveRem or not globals.IsFreeFor(curUnit, curX, curY)): #jeśli możliwe jest przemieszczenie się do pola docelowego
            FillTileColor(curX - globals.camOffsetX, curY - globals.camOffsetY, textRenderer.RED, textRenderer.RED)
        else: #jeśli nie jest to możliwe
            FillTileColor(curX - globals.camOffsetX, curY - globals.camOffsetY, textRenderer.YELLOW, textRenderer.GREEN)

        globals.defaultRenderer.InsertTextSpecial(f"Escape - cofnij\n1-5 - szybki wybór jednostki\nEnter - zatwierdź\n\nRuch jednostką U{curSelect + 1}\nPozostałe ruchy: {curUnit.moveRem}/{curUnit.speed} (-{len(renderPath)})", 1, gridSizeY + 1, globals.defaultRenderer.sizeX, gridSizeY + 6)
    elif (globals.gameState == 3): #atak jednostką
        globals.defaultRenderer.InsertTextSpecial(f"Escape - cofnij\n1-5 - szybki wybór jednostki\nEnter - zatwierdź\n\n", 1, gridSizeY + 1, globals.defaultRenderer.sizeX, gridSizeY + 3)


        globals.defaultRenderer.SetChar("V", renderCursorX, renderCursorY)
        targetDist = abs(curY - curUnit.posY) + abs(curX - curUnit.posX)
        unitAtTarget = globals.GetUnitAt(curX, curY)
        for y in range(max(0, curUnit.posY - curUnit.range), min(curUnit.posY + curUnit.range + 1, globals.mapSizeX - 1)):
            for x in range(max(0, curUnit.posX - curUnit.range), min(curUnit.posX + curUnit.range + 1, globals.mapSizeY - 1)):
                if (abs(y - curUnit.posY) + abs(x - curUnit.posX) <= curUnit.range):
                    unitAtTemp = globals.GetUnitAt(x, y)
                    if (unitAtTemp == None):
                        FillTileColor(x - globals.camOffsetX, y - globals.camOffsetY, textRenderer.RESETCOLOR, textRenderer.YELLOW)
                    elif (unitAtTemp.ownerId != 0):
                        FillTileColor(x - globals.camOffsetX, y - globals.camOffsetY, textRenderer.RED, textRenderer.CYAN)

        FillTileColor(curUnit.posX - globals.camOffsetX, curUnit.posY - globals.camOffsetY, textRenderer.YELLOW, textRenderer.BLUE)
        if (targetDist > curUnit.range or (unitAtTarget != None and unitAtTarget.ownerId == 0)):
            FillTileColor(curX - globals.camOffsetX, curY - globals.camOffsetY, textRenderer.RED, textRenderer.RED)
        elif (unitAtTarget != None):
            FillTileColor(curX - globals.camOffsetX, curY - globals.camOffsetY, textRenderer.GREEN, textRenderer.GREEN)

    elif (globals.gameState == 4): #sterowanie kamerą
        globals.defaultRenderer.InsertTextSpecial(f"Escape - powrót\n\nRuch kamerą\nKursor: ({curX}, {curY})", 1, gridSizeY + 1, globals.defaultRenderer.sizeX - 1, gridSizeY + 4)
        pass
    
    globals.defaultRenderer.Overwrite()

