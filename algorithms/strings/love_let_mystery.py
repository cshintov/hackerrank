""" solves https://www.hackerrank.com/challenges/the-love-letter-mystery """
def distance(char1, char2):
    """ calculates the distance between two char """
    return abs(ord(char1) - ord(char2))


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


def lov_let_myst(string):
    """ find the index of the letter that makes the string not a palindrome """
    operations = 0
    left, right = split(string)
    mis_pos = mismatch(left, right)
    for pos in mis_pos:
        operations += distance(left[pos], right[pos])

    return operations

TESTS = [
    'abc',
    'abcba',
    'abcd',
    'cba'
]

TEST = True
#TEST = False
if TEST:
    RESULTS = [lov_let_myst(t) for t in TESTS]
    if RESULTS == [2, 0, 4, 2]:
        print 'OK'
    else:
        print 'shoulda been -- [2, 0, 4, 2]'
        print RESULTS

if not TEST:
    for _ in range(input()):
        print lov_let_myst(raw_input())
