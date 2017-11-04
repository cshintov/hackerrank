from pdb import set_trace 

def maximum_ones(digits, minn=0, maxx=None):
    if not maxx:
        maxx = len(digits)

    guess_len = (minn + maxx) / 2

    if guess_len == 0 and maxx == 1:
        if '1' not in digits:
            return 0
        else:
            return 1

    if '1' * guess_len in digits:
        if '1' * (guess_len + 1) not in digits:
            return guess_len

        return maximum_ones(digits, guess_len + 1, maxx)
    else:
        return maximum_ones(digits, minn, guess_len - 1)


def find_max_ones_in(num):
    return maximum_ones(format(num, 'b'))


def test():
    assert find_max_ones_in(10) == 1
    print '*' * 25
    assert find_max_ones_in(15) == 4
    print '*' * 25
    assert find_max_ones_in(13) == 2
    print '*' * 25
    assert find_max_ones_in(368) == 3
    print '*' * 25
    assert find_max_ones_in(7) == 3
    print '*' * 25
    assert find_max_ones_in(0) == 0
    print '*' * 25
    assert find_max_ones_in(36800000000000000000000000) == 10

test()
    
# testS = 2 ** 3232
# print(testS)
# print find_max_ones_in(~testS)
