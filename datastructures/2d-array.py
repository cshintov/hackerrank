"""
Solves https://www.hackerrank.com/challenges/2d-array
""" 
from pprint import pprint

def read_strings(num):
    """ strings """
    for _ in range(num):
        yield raw_input()


def num_lines(num):
    """ read lines of numbers """
    for line in read_strings(num):
        yield map(int, line.strip().split())


def read_matrix(row):
    """ read a matrix of four rows """
    rows = num_lines(row)
    return [[int(c) for c in row_] for row_ in rows]


def get_hour_glasses(matx):
    """ yields hour glasses from a 6 x 6 matrix """
    for i in range(6):
        for j in range(6):

prob = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0]
]

def solve(matx):
    """ solves it """
    pprint(matx)

test = True
if __name__ == '__main__' and not test:
    prob = read_matrix(6)

solve(prob)

