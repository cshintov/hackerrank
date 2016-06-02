""" solves https://www.hackerrank.com/challenges/gem-stones """

def count_of_gemelements(rocks):
    """ find the index of the letter that makes the string not a palindrome """

    elements = map(set, rocks)
    gemelemts = reduce(lambda x,y: x.intersection(y), elements)
    return len(gemelemts)



ROCKS = [raw_input() for _ in range(input())]
print count_of_gemelements(ROCKS)
