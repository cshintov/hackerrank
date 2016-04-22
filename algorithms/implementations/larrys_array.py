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

class NotSortable(Exception):
    """ Not Sortable exception """
    pass
    


from functools import partial
from pdb import set_trace
def _gen_states(array, starting_states):
    """ generate all possible states in the process of sorting """
    initial_states = gen_states_helper(array)
    for state in initial_states:
        starting_states.append(state)
        temp = gen_states_helper(state)
        for tst in temp:
            if tst in starting_states:
                raise NotSortable
            if is_sorted(tst):
                raise Sortable
            try:
                starting_states.append(tst)
                _gen_states(tst, starting_states)
            except NotSortable:
                continue

    raise NotSortable


def is_sortable(array, parents=[]):
    """ checks whether the robot can sort the array """
    if is_sorted(array):
        return 'YES'
    children = gen_states_helper(array)
    for child in children:
        if is_sorted(child):
            return 'YES'
        if child in parents:
            continue
        parents.append(array)
        return is_sortable(child, parents) 
    return 'NO'
    

def solve():
    """ solve it """
    tests = int(raw_input())
    for _ in range(tests):
        lines = num_lines(2)
        _ = next(lines)
        print is_sortable(next(lines))


if __name__ == '__main__':
    #solve()
    #is_sortable([3,1,2])
    #raw_input()
    #is_sortable([1,3,2])
    #raw_input()
    #is_sortable([1,3, 4, 2])
    #raw_input()
    #is_sortable([1,2,3,5,4])
    set_trace()
    print is_sortable([1,6,4,2,3,5,3,6,4])
