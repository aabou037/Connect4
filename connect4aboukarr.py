import random

def who_goes_first():
	randinteger= random.randint(1,10)
	print("In order to decide who starts this game. We will calculate a random number and see who can come closest to guessing it.")
	player0_number = int(input("Player 0, Please select a number from 1 to 10:"))
	player1_number = int(input("Player 1, Please select a number from 1 to 10:"))
	player0_diff = abs(player0_number - randinteger)
	player1_diff = abs(player1_number - randinteger)

	if (player0_diff < player1_diff): 
		return 0

	else:
		return 1



def player0_coord(Board):
    player0_coord = int (input("Player 0, which column would you like to choose?"))
    print(Board)
    return player0_coord


def player1_coord(Board):
    player1_coord = int(input("Player 1, which column would you like to choose?"))
    print(Board)
    return player1_coord

def put_on_board(turn, col,Board):
    depth = 0
    while is_taken(depth, col, Board):
        depth = depth + 1

    Board[col][depth] = turn
    return Board


def is_taken(x,y, Board):
    if Board [x][y] == 0:
        return True
    elif Board[x][y] == 1:
        return True
    else: 
        return False

def Switch_Player():
    if Current_Player == 0: 
        Current_Player = 1
    else: Current_Player = 0

def Done (turn):
    Game_Over = True
    Print ("The Winner is Player" + turn)

def Is_Game_Over():
    for y in range (0,6):
        for x in range (0,4):
            Window = Board [x: x+3][y]
            if window_is_true(Window):
                return True

    for x in range (0,7):
        for y in range (0,3):
            Window = Board [x][y: y+3]
            if window_is_true(Window):
                return True
        
def window_is_true(window):
    if sum (window) == 0 or sum (window) == 4:
        return True

Board = [[2,2,2,2,2,2],[3,3,3,3,3,3],[4,4,4,4,4,4],[5,5,5,5,5,5],[6,6,6,6,6,6],[7,7,7,7,7,7],[8,8,8,8,8,8]]


Game_Over = False
Current_Player = who_goes_first()

while not Game_Over:
    if Current_Player == 0:
        player0_coords = player0_coord(Board)
        Board = put_on_board(0,player0_coords,Board)
        if Is_Game_Over ():
            Done ()
        else: Switch_Player()
    if Current_Player == 1:
        player1_coords = player1_coord(Board)
        Board = put_on_board(1,player1_coords,Board)
        if Is_Game_Over ():
            Done ()
        else: Switch_Player()
