import random

lotto = open('lottery.txt', 'r')
lotto_read = [x.replace('\n', '') for x in lotto.readlines()]
lotto.close()
lotto_list = []


def split_by(read):
    temp = list()
    for x in read:
        if len(x) != 1:
            temp.append(x)
        else:
            lotto_list.append(temp)
            temp = list()
    return lotto_list[1:]


final = split_by(lotto_read)

following_lines = int(lotto_read[0])
n = lotto_read[1:following_lines + 1]

checking = list()

for n in final:
    checking = list()
    for x in n:
        for y in x.split(' '):
            checking.append(int(y))

    checking = sorted(checking)
    print(checking)
    no = 0
    for x in range(1,31):
        if x in checking and not x > 30:
            pass
        else:
            no += 1
    if no >= 1:
        print("No")
    else:
        print("Yes")