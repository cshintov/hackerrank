""" solves https://www.hackerrank.com/challenges/alternating-characters """


def alt_char(string):
    """ finds out the minimum deletions needed to make it alt-char """
    curr = ''
    deletions = 0
    for char in string:
        if char == curr:
            deletions += 1
        else:
            curr = char
    return deletions


TESTS = [
    'AAAA',
    'BBBBB',
    'ABABABAB',
    'BABABA',
    'AAABBB'
]

TEST = False
#TEST = True

if not TEST:
    for _ in range(input()):
        print alt_char(raw_input())
else:
    RESULTS = [alt_char(TEST) for TEST in TESTS]
    if RESULTS == [3, 4, 0, 0, 4]:
        print 'OK'
    else:
        print 'NOT OK'
        print RESULTS
