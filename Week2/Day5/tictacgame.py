


print('Welcome to TicTacToe!')
sqr = [
    1,2,3,
    4,5,6,
    7,8,9
]

def display_board():
    print('*********')
    print('*' + ' ' + str(sqr[0]) + '|' + str(sqr[1]) + '|' + str(sqr[2]) + ' ' + '*')
    print('---------')
    print('*' + ' ' + str(sqr[3]) + '|' + str(sqr[4]) + '|' + str(sqr[5]) + ' ' + '*')
    print('---------')
    print('*' + ' ' + str(sqr[6]) + '|' + str(sqr[7]) + '|' + str(sqr[8]) + ' ' + '*')
    print('*********')
display_board()

def check_win(): # check winner
    if sqr[0] == sqr[1] == sqr[2] == ('X'): # for row X
        print((f'Player X -victory!'))
        return True
    elif sqr[3] == sqr[4] == sqr[5] == ('X'):
        print((f'Player X -victory!'))
        return True
    elif sqr[6] == sqr[7] == sqr[8] == ('X'):
        print((f'Player X -victory!'))
        return True
    elif sqr[0] == sqr[1] == sqr[2] == ('O'): # for row O
        print((f'Player O -victory!'))
        return True
    elif sqr[3] == sqr[4] == sqr[5] == ('O'):
        print((f'Player O -victory!'))
        return True
    elif sqr[6] == sqr[7] == sqr[8] == ('O'):
        print((f'Player O -victory!'))
        return True
    elif sqr[0] == sqr[3] == sqr[6] == ('X'): # for column X
        print((f'Player X -victory!'))
        return True
    elif sqr[1] == sqr[4] == sqr[7] == ('X'):
        print((f'Player X -victory!'))
        return True
    elif sqr[2] == sqr[5] == sqr[8] == ('X'):
        print((f'Player X -victory!'))
        return True
    elif sqr[0] == sqr[3] == sqr[6] == ('O'): # for column O
            print((f'Player O -victory!'))
            return True
    elif sqr[1] == sqr[4] == sqr[7] == ('O'):
        print((f'Player O -victory!'))
        return True
    elif sqr[2] == sqr[5] == sqr[8] == ('O'):
        print((f'Player O -victory!'))
        return True
    elif sqr[0] == sqr[4] == sqr[8] == ('X'): # for diagonal X
        print((f'Player X -victory!'))
        return True
    elif sqr[2] == sqr[4] == sqr[6] == ('X'):
        print((f'Player X -victory!'))
        return True
    elif sqr[0] == sqr[4] == sqr[8] == ('O'): # for diagonal O
        print((f'Player O -victory!'))
        return True
    elif sqr[2] == sqr[4] == sqr[6] == ('O'):
        print((f'Player O -victory!'))
        return True
    elif  all([sqr[i] in ('X','O') for i in range(9)]):
        print((f'Tie!'))
        return True
    return False
print(check_win())

# To get the position from the player
def player_input():
    display_board()

while True:
    player_1 = input(f'player X, please type cell number to put figure X inside: ')
    sqr[int(player_1) - 1] = ('X') # cell step == index
    display_board()
    if check_win(): # check winner
        break

    player_2 = input(f'player O, please type cell number to put figure O inside: ')
    sqr[int(player_2) - 1] = ('O')
    display_board()
    if check_win():
        break


def play():
    while True:
        player_input()
        display_board
        if check_win(): # end of the loop
            break