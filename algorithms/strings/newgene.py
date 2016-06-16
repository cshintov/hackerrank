""" solve https://www.hackerrank.com/challenges/bear-and-steady-gene
    find out the smallest substring with all the extra letters
"""
from collections import Counter as Ctr
from pdb import set_trace as st
ALPHABET = list('ACTG')

def is_valid(extras):
    """ checks the validity of the substring """
    def sub_contains_extras(substr):
        """ checks whether if substring contains extras """
        freq = Ctr(substr)
        for char, count in extras.items():
            assert(count <= freq[char])
    return sub_contains_extras 


def steady_gene(gene, length):
    """ finds the smallest substring to replace """
    ans = length
    steady_count = length / 4
    target_gene_freq = dict(zip(ALPHABET, [steady_count] * 4))
    gene_freq = Ctr(gene)
    if gene_freq == target_gene_freq:
        return 0
    diff = {
        char: target_gene_freq[char] - gene_freq[char]
        for char in ALPHABET
    }
    extras = {char: abs(diff[char]) for char in ALPHABET if diff[char] < 0}
    validity_check = is_valid(extras)
    start, end = 0, 0
    while end < length:
        substr = gene[start:end]
        print substr
        try:
            validity_check(substr)
            ans = min(ans, len(substr))
            start += 1
            continue
        except:
            end += 1
    return ans


if __name__ == '__main__':
    LEN = input()
    GENE = raw_input()
    ANS = steady_gene(GENE, LEN)
    print ANS
