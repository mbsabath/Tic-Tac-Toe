__author__ = 'Ben'

from Board import *
import random
Win_List_3 = gen_win_list(3)


def display_moves(board):
    """
    Displays a Board with numbers indicating the space
    indicated by the input
    :board: instance of Board
    :return:none
    """
    size = board.size
    display = Board(size)
    for i in board.free:
        display.moves[i] = i + 1
    print(display)


def input_x(board, n):
    """
    Places an X in the given board at the specified location
    :param board: the Board in use
    :param n: the input location (int)
    :return:none
    """
    board.moves[n - 1] = 'X'
    board.X.append(n - 1)
    board.free.remove(n - 1)
    # print(board.X)


def input_o(board, n):
    """
    Places an O in the given board at the specified location
    :param board: the Board in use
    :param n: the input location (int)
    :return:none
    """
    board.moves[n - 1] = 'O'
    board.O.append(n - 1)
    board.free.remove(n - 1)
    # print(board.X)


def get_move(board, side):
    """
    function for asking for move and displaying relevant information
    :param board: current game board
    :return: int representing move
    """
    print('Moves available:')
    display_moves(board)
    print('\n')
    n = int(input(side + ', Please choose your move: '))
    return n


def x_win(board, lst):
    """
    tests to see if x has won the game
    :param board: a game board
    :param lst: a list of winning combinations
    :return:
    """
    for row in lst:
        test = 0
        for x in board.X:
            if x in row:
                test += 1
        if test == board.size:
            return True
    return False


def o_win(board, lst):
    """
    tests to see if x has won the game
    :param board: a game board
    :param lst: a list of winning combinations
    :return:
    """
    for row in lst:
        test = 0
        for o in board.O:
            if o in row:
                test += 1
        if test == board.size:
            return True
    return False


def winning_move(board, side):
    """
    determines if a winning move in an n = 3 is available for the input side,
    returning the corresponding move. Returns -1 otherwise.
    :param board: a game board
    :param side: X or O
    :return: int
    """
    if side == 'X':
        for row in Win_List_3:
            x_test = 0
            free_test = []
            for num in row:
                if board[num] == 'X':
                    x_test += 1
                if num in board.free:
                    free_test.append(num)
            # print(x_test, len(free_test))
            if x_test == 2 and len(free_test) == 1:
                return free_test[0] + 1
        return -1
    elif side == 'O':
        for row in Win_List_3:
            o_test = 0
            free_test = []
            for num in row:
                if board[num] == 'O':
                    o_test += 1
                if num in board.free:
                    free_test.append(num)
            if o_test == 2 and len(free_test) == 1:
                return free_test[0] + 1
        return -1
    return -1


def choose_move(board, side):
    """Determine the best move for the computer to take in a n = 3 game"""
    if board.empty:
        return random.choice([1, 3, 7, 9])
    can_win = winning_move(board, side)
    if can_win != -1:
        return can_win
    if side == 'X':
        can_lose = winning_move(board, 'O')
        if can_lose != -1:
            return can_lose
        if 4 in board.free: # give the middle priority
            return 5
        good_moves = []
        ok_moves = []
        for free in board.free:
            test = good_move(board, 'X', free + 1)
            if test == 1:
                good_moves.append(free + 1)
            elif test == 0:
                ok_moves.append(free + 1)
        if len(good_moves) != 0:
            return random.choice(good_moves)
        elif len(ok_moves) != 0:
            return random.choice(ok_moves)
        else:
            moves = [x + 1 for x in board.free]
            return random.choice(moves)

    if side == 'O':
        can_lose = winning_move(board, 'X')
        if can_lose != -1:
            return can_lose
        if 4 in board.free:  # Give the middle priority
            return 5
        good_moves = []
        ok_moves = []
        for free in board.free:
            test = good_move(board, 'O', free + 1)
            if test == 1:
                good_moves.append(free + 1)
            elif test == 0:
                ok_moves.append(free + 1)
        if len(good_moves) != 0:
            return random.choice(good_moves)
        elif len(ok_moves) != 0:
            return random.choice(ok_moves)
        else:
            moves = [x + 1 for x in board.free]
            return random.choice(moves)

def good_move(board, side, move):
    """
    Tests a potential move to determine if it generates a desirable outcome
    :param board: the board being tested
    :param side: the point of view the function is looking from
    :param move: the move being tested
    :return: 1 for good, 0 for neutral, -1 for bad
    """
    test_board = Board(3)
    for x in board.X:
        input_x(test_board, x + 1)
    for o in board.O:
        input_o(test_board, o + 1)
    if side == 'X':
        input_x(test_board, move)
        if winning_move(test_board, 'X') != -1:
            return 1
        if len(test_board.free) != 0:
            # print('WE MUST GO DEEPER')
            response = choose_move(test_board, 'O')
            input_o(test_board, response)
            if winning_move(test_board, 'O') != -1:
                return -1
        return 0

    elif side == 'O':
        input_o(test_board, move)
        if winning_move(test_board, 'O') != -1:
            return 1
        if len(test_board.free) != 0:
            # print('WE MUST GO DEEPER')
            response = choose_move(test_board, 'X')
            input_x(test_board, response)
            if winning_move(test_board, 'X') != -1:
                return -1
        return 0





