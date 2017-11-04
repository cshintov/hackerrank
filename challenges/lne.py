"""
Solves https://www.hackerrank.com/contests/w28/challenges/lucky-number-eight
"""
MOD = 10 ** 9 + 7

def subsequences(string, length = 1):
    """ gives the subsequences of the string """
    size = len(string)
    for length in xrange(1, size+1):
        if length > size:
            raise StopIteration

        for start in xrange(size):
            if start + length <= size:
                yield int(string[start: start+length])


def luckynumbereight(string):
    """ finds the subsequences divisible by 8 """
    return len(filter(lambda x: x % 8 == 0, subsequences(string))) % MOD


if __name__  == '__main__':
    n = int(raw_input().strip())
    number = raw_input().strip()
    print luckynumbereight(number)
