""" solving manas and stones problem """

def read_strings(num):
    """ read lines of input """
    for _ in range(num):
        yield raw_input()


def read_nums(num):
    """ read single numbers from each line """
    for num in read_strings(num):
        yield int(num)


def frequencies(num):
    """ generate the frequency of a and b in each step """
    a_freq = num - 1
    for b_freq in range(num):
        yield a_freq, b_freq
        a_freq -= 1


def find_last_stones(num, numa, numb):
    """ finds the value of the last stones """
    last_stones = []
    for freqa, freqb in frequencies(num):
        last_stones.append(freqa * numa + freqb * numb)
    return sorted(list(set(last_stones)))


def solve():
    """ solves the problem """
    tests = int(raw_input())
    for _ in range(tests):
        num, numa, numb = read_nums(3)
        last_stones = find_last_stones(num, numa, numb)
        for stone in last_stones:
            print stone,
        print


if __name__ == '__main__':
    solve()
