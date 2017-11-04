""" https://www.hackerrank.com/contests/w22/challenges/box-moving """
from pdb import set_trace as st

def find_j(setx, sety, idx):
    """ find j """
    #diffs = []
    #for idxj in range(idx+1, len(setx)):
    #   diff = setx[idxj] - sety[idxj]
    #   diffs.append((idxj, diff))
    diffs = [(idxj, setx[idxj]-sety[idxj])
            for idxj  in range(idx+1, len(setx))
            if setx[idxj] - sety[idxj] != 0]
    diffs.sort(key=lambda tup: tup[1])
    #print diffs
    if not diffs:
        return -1

    return diffs[0][0]


def move_boxes(setx, sety, num):
    """ solves it """
    ans = 0
    for idx in range(num):
        #do_operation(idx, setx, sety)
        diff = setx[idx] - sety[idx]
        ans += abs(diff)
        try:
            if diff < 0:
                # x is less
                return -1
            elif diff > 0:
                # x is greater
                setx[idx] = setx[idx] - abs(diff)
                idxj = find_j(setx, sety, idx)
                if idxj == -1:
                    return ans
                setx[idxj] = setx[idxj] + abs(diff)
        except IndexError as err:
            return -1

    return ans

def take_out_common(setx, sety):
    """ """
    for elm in setx:
        if elm in sety:
            setx.remove(elm)
            sety.remove(elm)


if __name__ == '__main__':
    num = int(raw_input().strip())
    setx = map(int, raw_input().strip().split(' '))
    sety = map(int, raw_input().strip().split(' '))
    take_out_common(setx, sety)
    #setx, sety = [1, 2, 3], [2, 3, 2]
    #setx, sety = [1, 2, 3], [1, 2, 3]
    #setx, sety = [1, 3, 2], [-1, 3, 4]
    #setx, sety = [1, 2, 3], [-1, 4, 3]
    print move_boxes(setx, sety, len(setx))
    #print setx
    #print sety
