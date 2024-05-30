import re
import numpy as np
text = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
text2 = "Card   2:  1 45 93 96 65 88 78 15 27 26 |  5 84 62 63 45 61  1 80 88 77 40 51 73 21 32 98 74 59 97  9 15 71 25 43 23"
text3= "Card   3:  9 99 34 44 37 16 67 43 41 83 | 43 41  5 69 90 50 34 94 86 59 98 16 99 28 44 37 47 57  7 14 83 67 76  9 77"
text4 = "Card   4: 45 99 64 82 57  9 56 17 78  7 | 75 56 30 88 64  1 98 27  9 57  7  6 77 44 17 78 82 99 16 91 76 94 63 87 45"
text5 = "Card   5: 76 80 42 88 26 56 79 63  6 37 | 16  4 40 34 46 76 67 69  1 54  5 55 59 24 78 29 26  9 51 44 92 41 63 88 65"
total = []
def cardsvalue(input_text):

    card,subsets = input_text.split(":")
    win_val, your_val = map(lambda x: np.array(list(map(int, x.split()))), subsets.split("|"))
    c = np.intersect1d(win_val,your_val)
    #print(c)
    count = len(c)
    if count == 1:
        val = 1
        total.append(val)
    elif count == 0:
        val=0
        total.append(val)

    else:
        val = 1
        for i in range(len(c) - 1):
            val = val * 2
        total.append(val)


#cardsvalue(text)
#print(total)

with open("text.txt","r") as file:
    for line in file:

        cardsvalue(line)
        #print(total)

print(sum(total))
