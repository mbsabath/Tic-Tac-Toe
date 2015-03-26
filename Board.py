__author__ = 'Ben'


def gen_win_list(n):
    """
    generates lists of the winning positions
    :param n: size of the board
    :return:list of lists of ints
    """
    win_list = []
    for x in range(n):
        temp_list = []
        for y in range(n*x, n*x+n):  # make horizontal row
            temp_list.append(y)
        win_list.append(temp_list)
        temp_list = []
        for y in range(n):  # make vertical
            temp_list.append(n*y + x)
        win_list.append(temp_list)
    lr_diagonal = []
    rl_diagonal = []
    lr_temp = 0  # accumulator for left to right diagonal value
    rl_temp = n-1  # accumulator for right to left diagonal
    for count in range(n):
        lr_diagonal.append(lr_temp)
        lr_temp += n + 1
        rl_diagonal.append(rl_temp)
        rl_temp += n-1
    win_list.append(lr_diagonal)
    win_list.append(rl_diagonal)
    return win_list


class Board:
    """An object representing the tic tac toe board.
    Stores the relevant moves for each game instance"""

    def __init__(self, n):
        self.size = n
        self.moves = [' '] * n ** 2
        self.X = []
        self.O = []
        self.free = list(range(n**2))

    def __str__(self):
        line_indexes = []
        line_list = []
        n = self.size
        out = {}
        for i in range(0, n + 1):
            line_indexes.append(i * n)

        for i in range(n):
            line_name = "line_" + str(i)
            line_list.append(line_name)
            line = " "
            for j in range(line_indexes[i], line_indexes[i + 1]):
                # print(j)
                line += str(self.moves[j]) + ' '
                if j in range(line_indexes[i], line_indexes[i+1] - 1):
                    line += '| '
            line += ' \n'
            if i < n-1:
                line += '-' * (len(line) - 1) + '\n'
            # print(line)
            out[line_name] = line

        out_str = ''
        for item in line_list:
            out_str += out[item]

        return out_str

    def __getitem__(self, item):
        """
        adds support for indexing operations, into moves for shorthand
        """
        return self.moves[item]

    def __setitem__(self, key, value):
        """
        adds support for item assignment
        """
        self.moves[key] = value

    @property
    def empty(self):
        """returns true if board is empty"""
        return 'X' not in self.moves and 'O' not in self.moves
