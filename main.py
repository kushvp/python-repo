from __future__ import print_function
import os

def select_marker():
    '''
    Parameters --> null
    Return --> Tuple
    
    '''
    marker=''
    while not (marker=='O' or marker=='X'):
        marker = raw_input('Player 1: Choose your marker from O or X.').upper()
    if marker=='O':
        return ('O','X')
    else:
        return ('X','O')

def display_board(board):
    os.system('cls')
    print('   |   |   ')
    print(' '+board[7]+' | '+board[8]+' | '+board[9]+' ')
    print('___|___|___')
    print('   |   |   ')
    print(' '+board[4]+' | '+board[5]+' | '+board[6]+' ')
    print('___|___|___')
    print('   |   |   ')
    print(' '+board[1]+' | '+board[2]+' | '+board[3]+' ')
    print('   |   |   ')

def get_position(player):
    pass

def set_position(board,position,marker):
    board[position]=marker
    display_board(board)

def is_empty(board,position):
    if board[position]==' ':
        return True
    return False

def is_full():
    for i in range(1,10):
        if not board[i]=='O'or board[i]=='X'
            return False
    return True

def random_player():
    return random.randint(0,2)

def replay():
    board=' '*10

def check_win(board,marker):
    return (board[7]==marker and board[8]==marker and board[9]==marker) or (board[4]==marker and board[5]==marker and board[6]==marker) or (board[1]==marker and board[2]==marker and board[3]==marker) or (board[7]==marker and board[4]==marker and board[1]==marker) or (board[8]==marker and board[5]==marker and board[2]==marker) or (board[9]==marker and board[6]==marker and board[3]==marker) or (board[7]==marker and board[5]==marker and board[3]==marker) or (board[9]==marker and board[5]==marker and board[1]==marker)



game_on=True
while game_on:
    marker = select_marker()
    board=' '*10
    while not is_full:
        
    
