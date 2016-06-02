""" solves https://www.hackerrank.com/challenges/alternating-characters """

def distance(char1, char2):
    """ calculates the distance between two char """
    return abs(ord(char1) - ord(char2))


def funny_condition_checks(string):
    """ generator for condition checks """
    reverse = string[::-1]

    def funny_condition(idx):
        """ funny condition """
        lhs = distance(string[idx], string[idx-1])
        rhs = distance(reverse[idx], reverse[idx-1])
        return lhs == rhs

    for idx in range(1, len(string)):
        yield funny_condition(idx)
    

def is_funny_string(string):
    """ finds out the minimum deletions needed to make it alt-char """
    condition_checks = funny_condition_checks(string)
    for result in condition_checks:
        if not result:
            return 'Not Funny'

    return 'Funny'

for _ in range(input()):
    print is_funny_string(raw_input())
