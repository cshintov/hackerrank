""" solve https://www.hackerrank.com/challenges/bear-and-steady-gene
    find out the smallest substring with all the extra letters
"""
from collections import Counter as ctr
from pdb import set_trace as st

ALPHABET = list('ACTG')

sub_contains_extras = lambda x, y: x

def is_valid(gene, extras):
    """ checks the validity of the substring """
    def sub_contains_extras(start, end):
        """ checks whether if substring contains extras """
        for char, count in extras.items():
            if gene[start:end].count(char) != count:
                return False
        return True
    return sub_contains_extras 


def candidates(gene, min_len):
    """ generated candidates of min_len """
    for idx in xrange(0, len(gene)-min_len+1):
        yield idx, idx + min_len


def smallest_length(gene, extras, min_len):
    """ finds the min length to be replaced """
    global sub_contains_extras
    small_length = len(gene)
    cands = list(candidates(gene, min_len))
    print cands
    sub_contains_extras = is_valid(gene, extras)
    for start, end in cands:
        candidate = gene[start:end]
        if len(candidate) >= small_length:
            continue
        while not sub_contains_extras(start, end):
            if end <= len(gene): break
            candidate = gene[start:end]
            if len(candidate) >= small_length:
                end += 1
                continue
            print candidate
            end += 1
        else:
            small_length = min(len(candidate), small_length)
            if sub_contains_extras(start+1, end):
                small_length = len(candidate) - 1
            if small_length == min_len:
                return min_len
    return small_length


def centrestrings(gene, min_len, max_len):
    """ generate centrestrings """
    print min_len, max_len
    mid = len(gene) / 2
    for start in range(mid+1-max_len, mid):
        if start < 0:
            continue
        for end in range(mid+1, mid+max_len):
            if (end - start < max_len
                and not end - start < min_len
                and end < len(gene)):
                print start, end
                yield gene[start:end]


def centre_solve(gene, extras, min_len, max_len):
    """ solve the centre strings """
    small_length = len(gene)
    for string in centrestrings(gene, min_len, max_len):
        print string
        if sub_contains_extras(string, extras):
            small_length = min(small_length, len(string))
    return small_length


def divnconq(substr, extras, min_len):
    """ divide and conquer """
    mid = len(substr) / 2
    if mid < min_len:
        return smallest_length(substr, extras, min_len)
    if mid == min_len:
        if (sub_contains_extras(substr[:mid], extras)
                or sub_contains_extras(substr[:mid], extras)): 
            return min_len
        return centre_solve(substr, extras, min_len, mid+mid)
    left = divnconq(substr[:mid], extras, min_len)
    right = divnconq(substr[mid:], extras, min_len)
    small_length = min(left, right)
    if min_len == small_length:
        return min_len
    return min(small_length, centre_solve(substr, extras, min_len, small_length))


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
    print extras
    min_len = reduce(lambda x, y: x+y, extras.values())
    return divnconq(gene, extras, min_len)


if __name__ == '__main__':
    LEN = input()
    GENE = raw_input()
    ANS = steady_gene(GENE, LEN)
    print ANS
