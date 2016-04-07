""" modified kaprekar number challenge """

def read_lines(num):
    """ read lines of input """
    for _ in range(num):
        yield raw_input()


def read_nums(num):
    """ read single numbers from each line """
    for num in read_lines(num):
        yield int(num)

def is_kaprekar(num):
    """ tests whether a number is kaprekar number """
    numlen = len(str(num))
    sqr = str(num * num)
    right, left = sqr[-numlen:] or 0, sqr[:-numlen] or 0
    return num == int(right) + int(left)



def kaprekars(start, end):
    """ generate kaprekar numbers in the range """
    for num in range(start, end+1):
        if is_kaprekar(num):
            yield num


def print_kaprekars(start, end):
    """ print kaprekar numbers in the range """
    kapr_nums = kaprekars(start, end)
    for num in kapr_nums:
        print num,
    try:
        num
    except UnboundLocalError:
        print 'INVAVLID RANGE'

inputs = read_nums(2)
print_kaprekars(*inputs)
