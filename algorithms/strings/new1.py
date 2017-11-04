""" """
from time import sleep, time
from collections import Counter as Ctr
from pdb import set_trace as st
ALPHABET = list('ACTG')

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

def is_valid(extras, histo):
    """ check validity """
    validity = True
    for char in extras:
        if extras[char] <= histo.get(char, 0):
            continue
        else:
            validity = False
            break
    return validity

def steady_gene(gene, length):
    """ finds the smallest substring to replace """
    #st()
    ans = len(gene)
    extras = extra_chars(gene, length)
    if extras == {}:
        return 0
    #print extras
    for idx, char in enumerate(gene):
        #print idx
        if not char in extras:
            continue
        substring = ""
        substr_histo = {}
        for indx, char in enumerate(gene[idx:]):
            substring += char
            if char in extras:
                substr_histo[char] = substr_histo.get(char, 0) + 1
            if is_valid(extras, substr_histo):
                #print substring
                ans = len(substring)
                break
            if len(substring) >= ans:
                break
        if ans == sum(extras.values()):
            break
    return ans

#in1 = 'gaaattta'
#in1 = 'gaaatata'
#in1 = 'gaaataaa'
#in1 = 'gatacacagttt'
#in1 = 'gatacaca'
#in1 = 'ggttcaca'
from inputs import test as in1
if __name__ == '__main__':
    LEN = input()
    GENE = raw_input().upper()
    #GENE = in1.upper()
    ANS = steady_gene(GENE, LEN)
    #ANS = steady_gene(GENE, len(GENE))
    print ANS

