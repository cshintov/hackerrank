from pdb import set_trace 

input1 = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0]
]

input2 = [
    [11, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 11, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0]
]

input3 = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 11, 1, 0, 0, 0],
    [0, 0, 22, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0]
]

inputs = [input1, input2]

def test():
    assert max_hour_glass(input1) == 19
    print '*' * 25
    assert max_hour_glass(input2) == 27
    print '*' * 25
    assert max_hour_glass(input3) == 36
    print '*' * 25


def find_the_hour_glasses_in(table):
    """Finds the hour glasses in table""" 
    if not table:
        return [
            [0, 0, 0]
            [0, 0, 0]
            [0, 0, 0]
        ]

    rows, cols = len(table), len(table[0])
    rows_, cols_ = rows - 2, cols - 2
    total = rows_ * cols_
    def get_hour_glass(num):
        row, col = num % 4, num % 3

    hour_glasses = map(get_hour_glass, range(total))


def max_hour_glass(table):
    return 0


if __name__ == '__main__': 
    test()
    
# testS = 2 ** 3232
# print(testS)
# print find_max_ones_in(~testS)
