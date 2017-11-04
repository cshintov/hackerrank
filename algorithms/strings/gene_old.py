""" solve https://www.hackerrank.com/challenges/bear-and-steady-gene
    find out the smallest substring with all the extra letters
"""
from collections import Counter as ctr
from pdb import set_trace as st
from time import time

ALPHABET = list('ACTG')

def occurrences(string, char):
    """ returns all the positions where the character occurs """
    return [idx for idx, letr in enumerate(string) if letr == char]

valdity_check = lambda x: x


def subrange(seq, length):
    """ generates substrings of length """
    for idx in xrange(len(seq) - length + 1):
        yield idx, idx+length


def is_valid(gene, extras):
    """ checks the validity of the substring """
    def sub_contains_extras(start, end):
        """ checks whether if substring contains extras """
        for char, count in extras.items():
            if gene[start:end].count(char) < count:
                return False
        return True
    return sub_contains_extras 


def check(gene, length):
    """ checks substrings of the given length """
    print length
    for start, end in subrange(gene, length):
        if validity_check(start, end):
            #print gene[start:end]
            #print ctr(gene[start:end])
            print(end-start+1)
            return True
    return False


def divnconq(gene, start, end):
    """ div and conq the substring length """
    ans = end
    while True:
        print start, end
        mid = (start + end) / 2
        if check(gene, mid):
            ans = min(ans, mid)
            end = mid
            if start == mid:
                break
        else:
            start = mid+1
            if start > end:
                break
    return ans


def steady_gene(gene, length):
    """ finds the minimum length of substring to be changed """
    global validity_check
    steady_count = length / 4
    target_gene_freq = dict(zip(ALPHABET, [steady_count] * 4))
    #print target_gene_freq
    gene_freq = ctr(gene)
    #print gene_freq
    if gene_freq == target_gene_freq:
        return 0
    diff = {
        char: target_gene_freq[char] - gene_freq[char]
        for char in ALPHABET
    }
    extras = {char: abs(diff[char]) for char in ALPHABET if diff[char] < 0}
    print extras
    validity_check = is_valid(gene, extras)
    min_len = reduce(lambda x, y: x+y, extras.values())
    print min_len, length, '555555555555'
    return divnconq(gene, min_len, length)


if __name__ == '__main__':
    LEN = input()
    GENE = raw_input()
    start = time()
    ANS = steady_gene(GENE, LEN)
    print 'took ', time() - start, ' seconds' 
    print ANS
