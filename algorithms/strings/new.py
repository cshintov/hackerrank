""" solve https://www.hackerrank.com/challenges/bear-and-steady-gene
    find out the smallest substring with all the extra letters
"""
from time import sleep, time
from collections import Counter as Ctr
from pdb import set_trace as st
ALPHABET = list('ACTG')

def validity_check(extras, substr):
    """ checks the validity of the substring """
    class Validity(object): val = False
    validity = Validity()
    freq = Ctr(substr)
    defchars = []
    for char, count in extras.items():
        if freq[char] < count:
            defchars.append(char)
    if defchars:
        validity.val = False
    else:
        validity.val = True

    def is_valid(addchar=''):
        """ checks whether if substring contains extras """
        if not addchar:
            return validity.val
        freq[addchar] = freq.setdefault(addchar, 0) + 1
        if not addchar in defchars:
            return validity.val
        for char in defchars[:]:
            if addchar in extras:
                if freq[char] >= extras[char]:
                    defchars.remove(char)
        if not defchars:
            validity.val = True
        return validity.val

    return is_valid


def extra_chars(gene, length):
    """ finds the counts of the extra characters """
    steady_count = length / 4
    target_gene_freq = dict(zip(ALPHABET, [steady_count] * 4))
    gene_freq = Ctr(gene)
    if gene_freq == target_gene_freq:
        return {}
    diff = {
        char: target_gene_freq[char] - gene_freq[char]
        for char in ALPHABET
    }
    return {char: abs(diff[char]) for char in ALPHABET if diff[char] < 0}


def steady_gene(gene, length):
    """ finds the smallest substring to replace """
    ans = length
    extras = extra_chars(gene, length)
    print extras
    if not extras:
        return 0

    minlen = sum(extras.values())
    if minlen == length - length / 4:
        return minlen

    for start in range(length-minlen):
        end = minlen + start
        is_valid = validity_check(extras, gene[start:end])
        if is_valid():
            return minlen
        else:
            end += 1
            if end - start >= ans:
                break
            
        while end < length:
            addchar = gene[end-1]
            if length - start < minlen:
                return ans

            substr = gene[start:end]

            if is_valid(addchar):
                ans = min(ans, len(substr))
                break
            else:
                end += 1
                if end - start >= ans:
                    break
    return ans


if __name__ == '__main__':
    LEN = input()
    GENE = raw_input().upper()
    s = time()
    ANS = steady_gene(GENE, LEN)
    print ANS

