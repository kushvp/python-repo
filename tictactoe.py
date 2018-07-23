from __future__ import print_function
import random
import os

def select_marker():
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

def get_position(board):
    position = ' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not is_empty(board, int(position)):
        position = raw_input('Choose your next position: (1-9) ')
    return int(position)

def set_position(board,marker,position):
    board[position]=marker

def is_empty(board,position):
    return board[position]==' '

def is_full(board):
    if " " in board[1:]:
        return False
    else:
        return True

def random_player():
    return 'Player '+ str(random.randint(0,1)+1)

def replay():
    return raw_input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

def check_win(board,marker):
    return ((board[7]==marker and board[8]==marker and board[9]==marker) or 
    (board[4]==marker and board[5]==marker and board[6]==marker) or 
    (board[1]==marker and board[2]==marker and board[3]==marker) or 
    (board[7]==marker and board[4]==marker and board[1]==marker) or 
    (board[8]==marker and board[5]==marker and board[2]==marker) or 
    (board[9]==marker and board[6]==marker and board[3]==marker) or 
    (board[7]==marker and board[5]==marker and board[3]==marker) or 
    (board[9]==marker and board[5]==marker and board[1]==marker))



print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = select_marker()
    turn = random_player()
    print(turn + ' will go first.')
    game_on = True

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(theBoard)
            position = get_position(theBoard)
            set_position(theBoard, player1_marker, position)

            if check_win(theBoard, player1_marker):
                display_board(theBoard)
                print(player1_marker+' has won!')
                game_on = False
            else:
                if is_full(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = get_position(theBoard)
            set_position(theBoard, player2_marker, position)

            if check_win(theBoard, player2_marker):
                display_board(theBoard)
                print(player2_marker+' has won!')
                game_on = False
            else:
                if is_full(theBoard):
                    display_board(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break        