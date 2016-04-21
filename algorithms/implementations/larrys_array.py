""" solves https://www.hackerrank.com/challenges/larrys-array """

def read_strings(num):
    """ strings """
    for _ in range(num):
        yield raw_input()


def num_lines(num):
    """ read lines of numbers """
    for line in read_strings(num):
        yield map(int, line.strip().split())


def rotate(array):
    """ rotate once a three tuple """
    return array[1:] + [array[0]]


def rotate_n_times(array, num):
    """ rotate the three tuple n times """
    num %= 3
    for _ in range(num):
        array = rotate(array)
    return array


def is_sorted(array):
    """ checks whether an array is sorted or not """
    return all(l[i] <= l[i+1] for i in xrange(len(l)-1)) 


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
