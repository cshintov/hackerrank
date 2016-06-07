""" solve https://www.hackerrank.com/challenges/bear-and-steady-gene """
from collections import Counter as ctr
from pdb import set_trace as st

ALPHABET = list('ACTG')
def substrings(string, length):
    """ generates substrings of given length and up """
    if length == len(string):
        yield string
        return
    while length <= len(string):
        for idx in xrange(len(string) - length + 1):
            yield string[idx:idx+length]
        length += 1


def sub_contains_extras(substr, extras):
    """ checks whether if substring contains extras """
    freq = ctr(substr)
    for char, count in extras.items():
        if not count <= freq[char]:
            return False
    return True


def steady_gene(gene, length):
    """ finds the minimum length of substring to be changed """
    steady_count = length / 4
    target_gene_freq = dict(zip(ALPHABET, [steady_count] * 4))
    gene_freq = ctr(gene)
    if gene_freq == target_gene_freq:
        return 0
    diff = {
        char: target_gene_freq[char] - gene_freq[char]
        for char in ALPHABET
    }
    extras = {char: abs(diff[char]) for char in ALPHABET if diff[char] < 0}
    #deficiencies = {char: diff[char] for char in ALPHABET if diff[char] > 0}
    min_len = reduce(lambda x, y: x+y, extras.values())
    for substr in substrings(gene, min_len):
        if sub_contains_extras(substr, extras):
            return len(substr)


if __name__ == '__main__':
    LEN = input()
    GENE = raw_input()
    ANS = steady_gene(GENE, LEN)
    print ANS

