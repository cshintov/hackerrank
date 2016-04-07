""" read inputs """

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
