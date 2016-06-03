""" solves https://www.hackerrank.com/challenges/anagram """
from collections import Counter as frequency
from pdb import set_trace as st

def split(string):
    """ splits the string to equal length halves if possible """
    half = len(string) / 2
    return string[:half], string[half:]


def how_to_make_anagrams(string):
    """
    finds out the number of changes needed to make
    the left half the anagram of right half
    """
    if len(string) % 2 != 0:
        return -1

    changes = 0
    left, right = split(string)
    left, right = ''.join(sorted(left)), ''.join(sorted(right))
    lf = frequency(left)
    rf =  frequency(right)
    for c in rf:
        print c, rf[c], lf.get(c, 0)
    for c in lf:
        if not c in rf:
            print 0, lf[c]

    for lchar, rchar in zip(left, right):
        if lchar != rchar:
            changes += 1

    return changes

if __name__ == '__main__':

    test = 'leuqciermgjtxlcgnefmlrypvstbdcaoiuekckbosmhpxmxlsczevytqsmuvqulyorktdnjvbtkyfjlxmldjlwcfkwaasnaiembhzneagoblxoklzovmmzrxvtzpgcxmobtqoxqunthnitajhxywwpvtluiryiepjzfzzxtorcdbvgkfdidcayvlsgetoiizknyjmtzdvdgsjrzobcqbaomvwrombylnnjyzcyfzblrmetagvtjyjyvfrltsjeiwngxreeqhqjvwcwcaroycmvjdgcxpgfnvmkmsrcahnvfqtksmysoknxntzkifqxacjouaswjgupypzqcxiqjxqwqpgaxyxzciqxjivuoplohkejjobslrqdjxdivcjalzxwiuqymcptotcakfsxzlbiiesfhbfudeqlbilnkaibwmbgrvdqgeaqluwuwdozkemnmzczakaywbgpylifsivdftxbznclrqyfpaerkgrijxzijhndskgxgfafscqluqslqxdcfumpulzftoilyqkevklpodcitutltynzvbqpnpwifetfufkrpxidbknweiiyhvzexrtmgrunvpsruekjcsofcdbiljiuhhygytsgkovfdoyxsiiwaybebfpooxjxhhdfdxonljvoztnsexqgxslazcpnzalgjqomoeaznxqnqfhwfxderqfqswgrytahjowxsyzhvrwnyfkdfniyfprxlzqjsqsdgodamckhvixtohxvwhtbwmajlsudlmhrdkupoezjmwccfbxdktgifgrraluladffpzwdfvmttrwauvdfolnwthnuujfunmzelwiqtwkppirkdxpuieqcldwgodcdqcidaqwvoimeqeovdfpljhnvmlbbrdejhomjeihtqtxizngcsxqbffwrtzukdbvmphwwsfrkaqtadzexwwydcxxvwthbucqmlokdtbottjvykaviwvoaslxreeubiknuyzzrapnvaitkkovhljjewhxanrdwcsscrruthhohphuaxpjjaupwdmyrdcphuhkoyghhnwreflgfcroeofcrrakwezebgophuyqjuhpcuyhwrxafccztfjrljvmrldafcrqyagavghrxeudgyebfntrwqdqcjqjljajkimfotynyssgtwiykdpitvyvephryhcirophkouiipoblycxbrgvoesuvzlwiqgbgwiqmfauupyhpcfrtnoktiepksnsituqrehdjhafyanocuhxhxjcfotpggkqcggtmnzwxbdvbqlfmsevpoyxerokyycagivtyurvvusynefzymvocvngmbqkcumkcidaewxarqaewifuuckwxxekbwwdqjnsttvxpsziicogmubgwleuligmecpwneoizjipejzolovxkwfgjlcutkgzpxvcemndxvubeussknpujxcuifperxdgxblbpygovbqzxirhxjbigdcoktucrykobvrstxgoayqxijefshnalqrxjlbclmsohlgdlptlnjjwvpdnxtoklhhwsjzextsefzjqodbdombjefzdypnlwwhohgsecllhmuxczafopjztoawoplzlhgcrpuvrhgavdzzczfsqouleuhukuvxcdzvuwqlfznbemagohbexxqdrzxduubyyatsylgemthqihzwracozuuqutuqoxqmzjgywocjkjzssyolascznwshpmzdlprkaaiwomhyxhsshgdkbflobdxtrwwcnqnnqxlgmvfjczdlihxjojxsmuleqjifzxsrvfyjafueeysmfpvvysnnoytgibljzfbwlzhngbukzmxgbuccpppdqikalvjmbmionpbtrvesjdznzbposgsiqekbzwociyqyqurjrxbbcaqcdhqwnkgdotgopuszvjxldruuoxxryntdulbhwimkbtasptrkerxhitdwrbppoiuluwusghcjcfbtasgejdntzqqqtfhkqbvmxpedyimcnnwpiettjgnizfyskfechzogrumpdyssoqiyudtfmiolnofawkcfltlcnxusyolmevmayffmovxdmfdirincbyhqybjwpwkvtwvtbcgrafvmkyubihglhncfqnbfllaejxxlzdezjzlvahxiofuwsybilfpwspccmzpndtpotajtkidynxwhxarkfggxxiblkqbnkqdfsmycvddkbzuazllgutgtchfoygdkygpquptrswcvxwwxjhddalxetestmvdkduayjvpbttxrpvqzcteehbjahdvtbyfgsgeddwexpdqfyggabkhioqkvvfpydufxcjaifhhxkxcjdkleuspikzeifvgkrliwxkeetl'

    #RESULTS = [how_to_make_anagrams(raw_input()) for _ in range(input())]
    #EXPECTED = [-1,238,-1,-1,116,188,-1,214,164,181,-1,-1,-1,114,126,-1,207,167,120,-1,150,157,-1,-1,-1,104,-1,-1,-1,-1,-1,-1,-1,128,151,70,-1,124,116,-1,-1,-1,121,125,76,-1,87,-1,104,-1,-1,191,-1,-1,-1,164,-1,134,-1,145,205,115,-1,-1,-1,195,161,-1,135,196,217,-1,158,-1,-1,122,-1,-1,-1,109,169,98,-1,-1,-1,-1,-1,71,-1,166,109,-1,-1,-1,-1,-1,-1,101,63,147]
    RESULTS = how_to_make_anagrams(test)
    EXPECTED = 76
    if RESULTS == EXPECTED:
        print 'OK'
    else:
        print RESULTS
        """
	for idx, (res, exp) in enumerate(zip(RESULTS, EXPECTED)):
            if res != exp:
                print idx, res, exp
        """
