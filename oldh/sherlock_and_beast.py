""" find the largest decent number with n digits
    a decent number has following properties
    1. it must contain only 3 and 5
    2. number of 5 is divisible by 3
    3. number of 3 is divisible by 5
"""

def is_valid(num_str):
    """ checks whether given string is a decent number """
    num_5 = num_str.count('5')
    num_3 = num_str.count('3')
    if (num_5 + num_3 == len(num_str) and
        num_5 % 3 == 0 and num_3 % 5 == 0):
        return True
    return False

def number(size):
    """ generator for a candidate decent number string """
    num_5 = size
    num_3 = 0
    while(num_5 >= 0):
        yield '5' * num_5 + '3' * num_3
        num_5 -= 1
        num_3 += 1
    yield -1

def largest_decent(size):
    """ returns the largest decent number or -1 if empty list """
    itr = 0
    for num in number(size):
        itr += 1
        print itr
        if num == -1 or is_valid(num):
            return num

from time import time
num_test = input()
for num in range(num_test):
    size = input()
    start = time()
    largest_decent(size)
    print 'took', time()-start, ' seconds'
