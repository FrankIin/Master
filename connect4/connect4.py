import numpy as np

#declarations
ROWS = 6
COLUMNS = 7

board = np.zeros([ROWS, COLUMNS])

turn = 0
def check_win(player):
    print(f'player {player} is checked')
    
    # Horizontal
    for i in range(ROWS):
        count = 0
        for j in range(COLUMNS):
            if board[i,j] == player:
                count += 1
                if count == 4:
                    print(f'player {player} won!')
                    return True
            else:
                count = 0
    

    #Vertical
    for i in range(COLUMNS):
        count = 0
        for j in range(ROWS):
            if board[j,i] == player:
                count += 1
                if count == 4:
                    print(f'player {player} won!')
                    return True
            else:
                count = 0

    #positive diagonal
    for i in range(COLUMNS):
        count = 0
        k = i
        for j in range(ROWS):
            if k > COLUMNS - 1:
                break
            if board[j,k] == player:
                count += 1
                if count == 4:
                    print(f'player {player} won!')
                    return True
            else:
                count = 0
            k += 1

    # #negative diagonal
    for i in range(COLUMNS):
        count = 0
        k = i
        for j in range(ROWS):
            if k == -1:
                break
            if board[j,k] == player:
                count += 1
                if count == 4:
                    print(f'player {player} won!')
                    return True
            else:
                count = 0
            k -= 1
    return False

def put_coin(player, column):
    valid_turn = False
    for i in range(ROWS - 1,-1,-1):
        if board[i,column] == 0:
            board[i,column] = player
            valid_turn = True
            break
    if valid_turn == False:
        print("Column is already full! Choose another column")
        put_coin(player,select_coin(player))


def select_coin(player):
    while True:
        try:
            column = int(input(f"Player {player}, select a column 0 - 6 >> "))
        except:
            print("Please enter a valid number")
            continue
        if column < 0 or column > 6:
            print("Please enter a valid number")
            continue
        else:
            return column

        
while True:
    if turn % 2 == 0:
        player = 1        
    else:
        player = 2

    print(board)
    put_coin(player, select_coin(player))
    if check_win(player):
        break
    turn += 1