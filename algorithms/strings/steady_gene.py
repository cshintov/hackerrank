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


def candidates(gene, min_len):
    """ generated candidates of min_len """
    for idx in xrange(0, len(gene)-min_len+1):
        yield idx, idx + min_len


def smallest_length(gene, extras, min_len):
    """ finds the min length to be replaced """
    small_length = len(gene)
    cands = list(candidates(gene, min_len))
    for start, end in cands:
        candidate = gene[start:end]
        while (end <= len(gene) 
            and not sub_contains_extras(candidate, extras)):
            candidate = gene[start:end]
            print candidate
            end += 1
        else:
            if sub_contains_extras(candidate, extras):
                small_length = min(len(candidate), small_length)
                if sub_contains_extras(candidate[1:], extras):
                    return small_length - 1
                else:
                    return small_length


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


if __name__ == '__main__':
    LEN = input()
    GENE = raw_input()
    ANS = steady_gene(GENE, LEN)
    print ANS
