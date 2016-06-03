""" solves https://www.hackerrank.com/challenges/anagram """
from collections import Counter as frequency

def split(string):
    """ splits the string to equal length halves if possible """
    half = len(string) / 2
    return string[:half], string[half:]


def how_to_make_anagrams(string):
    """
    finds out the number of changes needed to make
    the left half the anagram of right half
    """
    if len(string) % 2 != 0:
        return -1

    left, right = split(string)
    left, right = ''.join(sorted(left)), ''.join(sorted(right))
    lfr, rfr = frequency(left), frequency(right)
    diffs = []

    for char in rfr:
        rct, lct = rfr[char], lfr.get(char, 0)
        diffs.append(lct - rct)

    for char in lfr:
        if not char in rfr:
            rct, lct = 0, lfr[char]
            diffs.append(lct - rct)

    ext, defc = 0, 0
    for diff in diffs:
        if diff > 0:
            ext += diff
        else:
            defc += abs(diff)

    if ext == defc:
        return ext
    else:
        return -1


if __name__ == '__main__':
    RESULTS = [how_to_make_anagrams(raw_input()) for _ in range(input())]
    for res in RESULTS:
        print res
