""" https://www.hackerrank.com/contests/w22/challenges/cookie-party """
 
def how_many_cookies(people, cookies):
    """ to get equal number of whole cookies """
    rem = -1
    ans = 0
    if cookies > people:
        ans = people - (cookies % people)
    elif cookies < people:
        ans = people - cookies
    else:
        ans = 0

    return ans

people = 3
cookies = 2
people = 3
cookies = 14
if __name__ == '__main__':
    print how_many_cookies(people, cookies)

