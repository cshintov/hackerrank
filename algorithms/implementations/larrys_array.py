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
    return all(array[i] <= array[i+1] for i in xrange(len(array)-1))


def rotate_at(position, array):
    """ rotate a three tuple from position once """
    return (
        array[:position] + rotate(array[position:position+3]) +
        array[position+3:]
    )


def gen_states_helper(array):
    """ generate all possible states in the process of sorting """
    for pos in range(len(array)-2):
        yield rotate_at(pos, array)


class Sortable(Exception):
    """ Sortable exception """
    pass

from pdb import set_trace
def gen_states(array):
    """ generate all possible states in the process of sorting """
    set_trace()
    initial_states = gen_states_helper(array)
    for state in initial_states:
        temp = gen_states_helper(state)
        for tst in temp:
            if is_sorted(tst):
                raise Sortable
            try:
                gen_states(tst)
            except RuntimeError:
                continue


def is_sortable(array):
    """ checks whether the robot can sort the array """
    try:
        gen_states(array)
    except Sortable:
        return True
    except RuntimeError:
        return False


def solve():
    """ solve it """
    tests = int(raw_input())
    for _ in range(tests):
        lines = num_lines(2)
        _ = next(lines)
        print is_sortable(next(lines))


if __name__ == '__main__':
    solve()
