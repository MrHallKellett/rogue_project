from random import randint
# import curses

# def main(scr):
#     scr.clear()
#     while True:
#         key = scr.getch ()
#         scr.addstr(0, 0, chr(key))  #print characters, with the coordinates

# curses.wrapper(main)

Width = 0
Height = 0

class Coordinates:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0

Player = Coordinates()
Player.x = Width // 2
Player.y = Height // 2

def MovePlayer(Player, Direction):
    if Direction == 'UP':
        Player.y += 1
    if Direction == 'DOWN':
        Player.y -= 1
    if Direction == 'LEFT':
        Player.x -= 1
    if Direction == 'RIGHT':
        Player.x += 1
    if 0 < Player.x <= Width and 0 < Player.y <= Height:
        ReturnStatement = f'The player moved to x: {Player.x}, y: {Player.y}'
    else:
        ReturnStatement = 'You hit a wall!'
    return ReturnStatement, Player

# print(MovePlayer(Player, 'LEFT'))

def MakeGrid():
    Grid = []
    
    for i in range(Height):
        Row = []
        Grid.append(Row)
        for i in range(Width):
            Row.append(' ')
    
    GoldcoinX = randint(0, Width)
    GoldcoinY = randint(0, Height)
    Grid[GoldcoinY][GoldcoinX] += "G"

    return Grid

# print(MakeGrid())

def DisplayGrid(Player, Grid):
    for Row in Grid:
        for Cell in Row:
            print(Cell)

def main():
    global Width, Height

    Width = int(input('Enter the width of the grid: '))
    Height = int(input('Enter the height of the grid: '))
    print('The player starts at x: {}, y: {}'.format(Player.x, Player.y))

    Grid = MakeGrid() 
    DisplayGrid(Player, Grid)

main()

#