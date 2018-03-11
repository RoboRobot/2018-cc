import math as m

def match_up(a,b):
    if len(a) > len(b):
        return [a,b + [None]]
    else:
        return [a,b]


def combine(l):
    temp = []
    for x in l:
        temp += x
    return temp

SizeDeck = int(input("input # of integers: "))
Shuffle = int(input("input # of shuffles: "))
Deck = list(range(1, SizeDeck + 1))

def shuffle_once():
    A = len(Deck)
    D1 = Deck[m.floor(A/2):]
    D2 = Deck[:m.ceil(A/2)-1]
    D1,D2 = match_up(D1,D2)
    return list(zip(D1,D2))


for x in range(Shuffle):
    Deck = [x for x in combine(shuffle_once()) if x!=None]
    print('\nShuffle #' + str(x+1) + ':')
    print(Deck)