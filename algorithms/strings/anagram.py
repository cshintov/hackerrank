""" solves https://www.hackerrank.com/challenges/anagram """
from collections import Counter as frequency
from pdb import set_trace as st

def split(string):
    """ splits the string to equal length halves if possible """
    half = len(string) / 2
    return string[:half], string[half:]


def how_to_make_anagrams(string):
    """
    finds out the number of changes needed to make
    the left half the anagram of right half
    """
    st()
    if len(string) % 2 != 0:
        return -1

    changes = 0
    left, right = split(string)
    left_freq, right_freq = frequency(left), frequency(right)
    for char in right_freq:
        changes += right_freq[char] - left_freq.get(char, 0)

    return changes

if __name__ == '__main__':
    RESULTS = [how_to_make_anagrams(raw_input()) for _ in range(input())]


    EXPECTED = [3, 1, -1, 2, 0, 1]
    if RESULTS == EXPECTED:
        print 'OK'
    else:
        print 'answer should be'
        print EXPECTED
        print 'not'
        print RESULTS
