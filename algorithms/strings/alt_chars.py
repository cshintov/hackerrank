""" solves https://www.hackerrank.com/challenges/palindrome-index """
def is_palindrome(string):
    """ is a palindrome? """
    if len(string) <= 1:
        return True
    left, right = split(string)
    return left == right


def mismatch(left, right):
    """ find the position of the mismatch """
    return [idx for idx, (a, b) in enumerate(zip(left, right)) if a != b]


def split(string):
    """ splits into left and right """
    length = len(string)
    is_odd = length % 2 != 0
    if is_odd:
        left = string[:length/2]
        right = string[-1:length/2:-1]
    else:
        left = string[:length/2]
        right = string[-1:(length/2) - 1:-1]
    return left, right


def palindrome_index(string):
    """ find the index of the letter that makes the string not a palindrome """
    left, right = split(string)
    if left == right:
        return -1
    else:
        mis_pos = mismatch(left, right)
        for pos in mis_pos:
            cands = pos, len(string) -1 - pos
            for cand in cands:
                if is_palindrome(string[:cand] + string[cand+1:]):
                    return cand
        return -1

TESTS = [
    'bdaab',
    'baadb',
    'bababb',
    'aaab',
    'baa',
    'aaa'
]

TEST = True
#TEST = False
if TEST:
    RESULTS = [palindrome_index(t) for t in TESTS]
    if [palindrome_index(t) for t in TESTS] == [1, 3, 1, 3, 0, -1]:
        print 'OK'
    else:
        print 'shoulda been -- [1, 3, 1, 3, 0, -1]'
        print RESULTS

if not TEST:
    for _ in range(input()):
        print palindrome_index(raw_input())
