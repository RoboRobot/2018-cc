def beg():
    b = int(input('how many integers?\n'))
    if b == 0:
        print("sorry not allowed")
        quit()
    a = [int(x) for x in input('Please enter the values now\n').split(' ')]
    if len(a) == b:
        return a
    else:
        print('incorrect amount of values within sequence')

def groupby(lst):
    temp = list()
    pos = True
    for x in lst:
        if x > -1:
            if pos == False:
                yield temp
                pos = True
                temp = list()
            temp.append(x)
        else:
            if pos == True:
                yield temp
                pos = False
                temp = list()
                temp.append(x)
                yield temp

bacon = beg() #Humor is important
b = list(groupby(bacon))
max_seq = [str(x) for x in max(b, key=lambda x: len(x))]
def search_for_pos(max_seq,lst):
    for x in max_seq:
        for n,y in enumerate(lst):
            if int(y)==int(x):
                yield str(n)

print('maximal sequence: ' + ' '.join(max_seq),'at positions ' + ', '.join(list(search_for_pos(max_seq,bacon))))
