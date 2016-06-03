""" solves https://www.hackerrank.com/challenges/two-strings """
def is_substring(str1, str2):
    """
    finds out whether they have a common substring
    """
    alpha1, alpha2 = set(str1), set(str2)
    inter = alpha1.intersection(alpha2)
    if len(inter) > 0:
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    RESULTS = [is_substring(raw_input(), raw_input()) for _ in range(input())]
    for res in RESULTS:
        print res
"""
if __name__ == '__main__':
    RESULTS = [is_substring(raw_input(), raw_input()) for _ in range(input())]
    EXPECTED = ['YES', 'NO']
    if RESULTS == EXPECTED:
        print 'OK'
    else:
        print 'answer should be'
        print EXPECTED
        print 'not'
        print RESULTS
"""
