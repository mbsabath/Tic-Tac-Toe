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


def best_response(board, side):
    """determine the best response for a given side to a board using backward induction"""
    can_win = winning_move(board, side)
    if can_win != -1:
        return can_win
    if len(board.free) == 1:
        return board.free[0] + 1
    if side == 'X':
        can_lose = winning_move(board, 'O')
        if can_lose != -1:
            return can_lose
        else:
            move_results = [[outcome(board, 'X', i+1), i + 1] \
                for i in board.free]
            best_move = max(move_results)
            return best_move[1]
    if side == 'O':
        can_lose = winning_move(board, 'X')
        if can_lose != -1:
            return can_lose
        else:
            move_results = [[outcome(board, 'O', i+1), i + 1] \
                for i in board.free]
            best_move = max(move_results)
            return best_move[1]


def outcome(board, side, move):
    """
    Determines the quality  of the ultimate outcome of a move for a given side
    :param board: game board
    :param side: X or O
    :param move: move to be evaluated
    :return: 1, 0 or -1
    """

    if len(board.free) == 0:
        if not x_win(board, Win_List_3) and not o_win(board, Win_List_3):
            # print('Returned!')
            return 0
    if side == 'X':
        if x_win(board, Win_List_3):
            # print('Returned!')
            return 1
        elif o_win(board, Win_List_3):
            # print('Returned!')
            return -1
        test_board = Board(3)
        for x in board.X:
            input_x(test_board, x + 1)
        for o in board.O:
            input_o(test_board, o + 1)
        input_x(test_board, move)
        if len(test_board.free) > 0:
            reply = best_response(test_board, 'O')
            result = -1 * outcome(test_board, 'O', reply)
            return result
        else:
            return 0
    if side == 'O':
        if x_win(board, Win_List_3):
            # print('Returned!')
            return -1
        elif o_win(board, Win_List_3):
            # print('Returned!')
            return 1
        test_board = Board(3)
        for x in board.X:
            input_x(test_board, x + 1)
        for o in board.O:
            input_o(test_board, o + 1)
        input_o(test_board, move)
        if len(test_board.free) > 0:
            reply = best_response(test_board, 'X')
            result = -1 * outcome(test_board, 'X', reply)
            return result
        else:
            return 0





