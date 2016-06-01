""" solves https://www.hackerrank.com/challenges/alternating-characters """


def alt_char(string):
    """ alternating characters """
    print string
    return 0


TESTS = [
    'AAAA',
    'BBBBB',
    'ABABABAB',
    'BABABA',
    'AAABBB'
]

TEST = False
TEST = True

if not TEST:
    for _ in range(input()):
        alt_char(raw_input())
else:
    RESULTS = [alt_char(TEST) for TEST in TESTS]
    if RESULTS == [0] * 5:
        print 'OK'
    else:
        print 'NOT OK'
        print RESULTS
