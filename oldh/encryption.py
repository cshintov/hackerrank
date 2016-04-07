""" solving encryption problem"""
from math import sqrt, ceil, floor

def find_range(length):
    """ find the range of rows and columns """
    sqrt_of_length = sqrt(length)
    return int(floor(sqrt_of_length)), int(ceil(sqrt_of_length))


def find_candidate_grid_sizes(length):
    """ finds candidate grid sizes """
    low_limit, up_limit = find_range(length)

    def conditions(rows, columns):
        """ check conditions for being the size of the grid """
        if (low_limit <= rows <= columns <= up_limit
                and rows * columns >= length):
            return True
        return False

    for rows in range(low_limit, up_limit + 1):
        for columns in range(rows, up_limit + 1):
            if conditions(rows, columns):
                yield rows, columns


def find_grid_size(length):
    """ find the gird size of the encryption """
    candidate_grid_sizes = find_candidate_grid_sizes(length)
    return min(candidate_grid_sizes, key=lambda tup: tup[0] * tup[1])


def encryption(message):
    """ encrypt the message """
    _, columns = find_grid_size(len(message))
    encrypted = []
    for column in range(columns):
        for pos in range(column, len(message), columns):
            if pos < len(message):
                encrypted.append(message[pos])
        encrypted.append(' ')

    return ''.join(encrypted).strip()

def solve():
    """ solves the problem """
    print encryption(raw_input().strip())


if __name__ == '__main__':
    solve()
