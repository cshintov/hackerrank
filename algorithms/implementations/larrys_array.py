""" solves https://www.hackerrank.com/challenges/larrys-array """

def read_strings(num):
    """ strings """
    for _ in range(num):
        yield raw_input()


def num_lines(num):
    """ read lines of numbers """
    for line in read_strings(num):
        yield map(int, line.strip().split())


def rotate(a, b, c):
    """ rotate once a three tuple """
    return [b, c, a]


def rotate_n_times(three_tup, n):
    """ rotate the three tuple n times """
    for _ in range(n):
        three_tup = rotate(*three_tup)
    return list(three_tup)


def is_sortable(array):
    """ checks whether the robot can sort the array """
    return array


def solve():
    """ solve it """
    tests = input()
    for test in range(tests):
        lines = num_lines(2)
        size = next(lines)
        print is_sortable(next(lines))


if __name__ == '__main__':
    solve()

12435
14325
14253
