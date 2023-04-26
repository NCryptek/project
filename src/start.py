class Player:
    def __init__(self):
        while (True):
            print("X, czy O?")
            PlayerChar = input()
            if (PlayerChar == 'X' or PlayerChar == 'O'):
                break
            print("źle, daj dobry znak")
        self.char = PlayerChar

    def __str__(self):
        return f"{self.char}"


class Maps:
    corners = {
        "upperLeft":     "┌",  # 218 np. chr(218)
        "upperRight":    "┐",  # 191
        "mediumLeft":    "├",  # 195
        "mediumRight":   "┤",  # 180
        "bottomLeft":    "└",  # 192
        "bottomRight":   "┘",  # 217
        "upperMid":      "┬",  # 194
        "midiumMid":     "┼",  # 197
        "bottomMid":     "┴"  # 193
    }
    lines = {
        "vertical": "│",  # 179
        "horizontal": "─"  # 196
    }
    map = []

    def __init__(self, size):
        self.size = size

        for i in range(self.size):
            col = [0 for i in range(self.size)]
            self.map.append(col)

    def __str__(self):
        line = ''
        for i in range(self.size):
            for j in range(self.size):
                if i == 0:
                    if j%2 == 0:
                        if j == 0:
                            line += self.corners["upperLeft"]
                        elif j == self.size
                            
        return line

def main():
    size = 10
    GameMap = Maps(size)
    GamePlayer = Player()
    print(GameMap)
    return


def Feedback():
    return


def AiTurn():
    return


main()
