""" solves https://www.hackerrank.com/challenges/taum-and-bday """

def read_strings(num):
    """ strings """
    for _ in range(num):
        yield raw_input()


def num_lines(num):
    """ read lines of numbers """
    for line in read_strings(num):
        yield map(int, line.strip().split())

def optimum_costs(blk, wht, conv):
    """ finds optimum costs of black and white gifts """
    min_cost = min((blk, wht))
    if min_cost == blk:
        if blk + conv < wht:
            return blk, blk + conv
    else:
        if wht + conv < blk:
            return wht + conv, wht

    return blk, wht


def total_cost(n_blk, n_wht, costs):
    """ calculate the minimum cost of gifts """
    blk_cst, wht_cst = optimum_costs(*costs)
    return n_blk * blk_cst + n_wht * wht_cst


def solve():
    """ solve it """
    tests = input()
    for test in range(tests):
        lines = num_lines(2)
        blk, wht = next(lines)
        print total_cost(blk, wht, next(lines))

solve()
