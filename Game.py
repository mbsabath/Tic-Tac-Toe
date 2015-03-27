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
            cpu = best_response(board, 'O')
            input_o(board, cpu)
        print('Current Board:')
        print(board)
        if o_win(board, WIN_LIST_3):
            print('You Lost')
            break
        elif x_win(board, WIN_LIST_3):
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
            assert 3 <= n <= 7
            break
        except ValueError or AssertionError:
            print('Please enter an integer value between 3 and 7')
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
        if moves >= n ** 2:
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
            cpu = best_response(board, 'X')
            input_x(board, cpu)
        print('Current Board:')
        print(board)
        if x_win(board, WIN_LIST_3):
            print('You Lost')
            break
        elif o_win(board, WIN_LIST_3):
            print('You Won!')
            break
        moves += 1
        if moves >= 9:
            print('Cats Game')
            break


def main():
    """initiate the game states"""
    while True:
        person_choice = input("Would you like to play against another person? (y/n)  ").lower()
        print(person_choice)
        while True:
            if person_choice in 'ynyesno':
                break
            else:
                person_choice = input('Please input yes or no  ').lower()
        if person_choice in 'nno':
            game_choice = input('Would you like to go first? (y/n)  ')
            while True:
                if game_choice in 'yyesnno':
                    break
                else:
                    game_choice = input('Please input yes or no  ').lower()
            if game_choice in 'yyes':
                play_x()
            elif game_choice in 'nno':
                play_o()
        if person_choice in 'yyes':
            print('I am funking up')
            play_together()
        again = input('Would you like to play again? (y/n)  ')
        while True:
            if again in 'yyesnno':
                break
            else:
                again = input('Please input yes or no  ').lower()
        if again in 'nno':
            break


if __name__ == "__main__": main()





