""" solve https://www.hackerrank.com/challenges/bear-and-steady-gene
    find out the smallest substring with all the extra letters
"""
from collections import Counter as ctr
from pdb import set_trace as st

ALPHABET = list('ACTG')

def sub_contains_extras(substr, extras):
    """ checks whether if substring contains extras """
    freq = ctr(substr)
    for char, count in extras.items():
        if not count <= freq[char]:
            return False
    return True


def candidates(posits, min_len):
    """ candidate beginning and end indices """
    for idx in range(len(posits)):
        for jdx in range(idx+1, len(posits)):
            if jdx - idx + 1 >= min_len:
                yield idx, jdx


def find(s, ch):
    return (i for i, ltr in enumerate(s) if ltr == ch)


def smallest_length(gene, extras, min_len):
    """ finds the min length to be replaced """
    for char in extras:
        indices = find(gene, char)

    

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
    min_len = reduce(lambda x, y: x+y, extras.values())
    return smallest_length(gene, extras, min_len)


import sys
if __name__ == '__main__':
    LEN = input()
    GENE = raw_input()
    ANS = steady_gene(GENE, LEN)
    print ANS

    LEN = input()
    GENE = raw_input()
    ANS = steady_gene(GENE, LEN)
    print ANS
