__author__ = 'Ben'

from Moves import *


def play_x():
    """
    begin the game, with the player as X
    :return:none
    """
    board = Board(3)
    moves = 0
    print('Current Board:')
    print(board)
    while True:
        if moves % 2 == 0:
            user = get_move(board, 'X')
            input_x(board, user)
        else:
            cpu = choose_move(board, 'O')
            input_o(board, cpu)
        print('Current Board:')
        print(board)
        if o_win(board, Win_List_3):
            print('You Lost')
            break
        elif x_win(board, Win_List_3):
            print('You Won!')
            break
        moves += 1
        if moves >= 9:
            print('Cats Game')
            break


def play_together():
    """
    play tic-tac-toe with two players
    :return:none
    """
    while True:
        try:
            n = int(input('What would you like the board dimensions to be: '))
            break
        except:
            print('Please enter an integer value')
    win_list = gen_win_list(n)
    board = Board(n)
    moves = 0
    print('Current Board:')
    print(board)
    while True:
        if moves % 2 == 0:
            user_1 = get_move(board, 'X')
            input_x(board, user_1)
        else:
            user_2 = get_move(board, 'O')
            input_o(board, user_2)
        print('Current Board:')
        print(board)
        if o_win(board, win_list):
            print('O Wins!')
            break
        elif x_win(board, win_list):
            print('X Wins!')
            break
        moves += 1
        if moves >= n**2:
            print('Cats Game')
            break


def play_o():
    """
    begin the game, with the player as O
    :return:none
    """
    board = Board(3)
    moves = 0
    print('Current Board:')
    print(board)
    while True:
        if moves % 2 == 1:
            user = get_move(board, 'O')
            input_o(board, user)
        else:
            cpu = choose_move(board, 'X')
            input_x(board, cpu)
        print('Current Board:')
        print(board)
        if x_win(board, Win_List_3):
            print('You Lost')
            break
        elif o_win(board, Win_List_3):
            print('You Won!')
            break
        moves += 1
        if moves >= 9:
            print('Cats Game')
            break


play_x()

