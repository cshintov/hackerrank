""" solves https://www.hackerrank.com/challenges/game-of-thrones """
from collections import Counter

def even(num):
    """ num is even or not """
    return num % 2 == 0


def can_find_a_key(string):
    """checks whether any anagram can be a palindrome """
    frequency = dict(Counter(string)).values()
    odds = [freq for freq in frequency if not even(freq)]
    if len(odds) > 1:
        print 'NO'
    else:
        print 'YES'
    
if __name__ == '__main__':
    string = raw_input()
    can_find_a_key(string)
