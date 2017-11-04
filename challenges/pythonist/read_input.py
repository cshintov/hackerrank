""" read inputs """

def read_line():
    return raw_input().split()


def read_lines():
    try:
        while True:
            yield read_line()
    except EOFError:
        raise StopIteration


def read_row():
    return [int(n) for n in read_line()]


def read_table(rows):
    for row in range(rows):
        yield read_row()


def read_strings(num):
    """ strings """
    for _ in range(num):
        yield raw_input()


def read_nums(num):
    """ read numbers """
    for num_str in read_strings(num):
        yield int(num_str)


def num_lines(num):
    """ read lines of numbers """
    for line in read_strings(num):
        yield map(int, line.strip().split())


def read_matrix(row):
    """ read a matrix of four rows """
    rows = read_strings(row)
    return [[int(c) for c in row_] for row_ in rows]


def transpose(table):
    """
    A table is of the type list of lists
    >>> transform([
            [1, 2, 3, 4, 5],
            [2, 3, 4, 5, 6],
            [3, 4, 5, 6, 7]
        ])
    """

    return [list(e) for e in zip(*table)]

def print_table(table):
    for row in table:
        for col in row:
            print col,

        print
