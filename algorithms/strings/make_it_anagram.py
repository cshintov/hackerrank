""" solves https://www.hackerrank.com/challenges/make-it-anagram """
from collections import Counter

def is_anagram(string1, string2):
    """ anagram or not? """
    if string1 == string2:
        return True
    frequency1 = dict(Counter(string1))
    frequency2 = dict(Counter(string2))
    return frequency1 == frequency2


def difference(string1, string2):
    """ find out the difference """
    set1, set2 = set(string1), set(string2)
    diff = list((set1 - set2)) + list((set2 - set1))
    return diff


def common(str1, str2):
    """ find out the common character string """
    diff = difference(str1, str2)
    for char in diff:
        str1 = str1.replace(char, '')
        str2 = str2.replace(char, '')
    return str1, str2


def make_anagrams(str1, str2):
    """ make two strings anagrams """
    tot_len = len(str1) + len(str2)
    str1, str2 = common(str1, str2)
    deletions = tot_len - (len(str1) + len(str2))
    frq1, frq2 = dict(Counter(str1)), dict(Counter(str2))
    deletions += sum([abs(a-b) for a, b in zip(frq1.values(), frq2.values())])
    print deletions


if __name__ == '__main__':
    str1, str2 = raw_input(), raw_input()
    make_anagrams(str1, str2)
