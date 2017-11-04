""" https://www.hackerrank.com/contests/w22/challenges/polygon-making """


def can_make_polygon_out_of(sides):
    """ checks whether a polygon can be made out of sides """
    longest = max(sides)
    return longest < sum(sides) - longest


def cut_largest_into_half(sides):
    """ cuts largest side into half """
    longest = max(sides)
    half = longest / 2.0
    idx = sides.index(longest)
    return sides[:idx] + sides[idx+1:] + [half, half]


def make_polygon(sides, num):
    """ computes minimum number of cuts to make a polygon """
    count = 0
    while not can_make_polygon_out_of(sides):
        sides = cut_largest_into_half(sides)
        count += 1
    return count


if __name__ == '__main__':
    num = int(raw_input().strip())
    sides = map(int, raw_input().strip().split(' '))
    print make_polygon(sides, num)
