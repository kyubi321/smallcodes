
# using counter and most_common
from collections import Counter
def frequencySort(s) :
    cnt = Counter(s)
    ans = ''
    for k, v in cnt.most_common():
        ans += k * v
    return ans
print(frequencySort("tree"))

# using dictionary and tuple and sorted method
def frequencysorts(s):

    dic = {}
    for i in s:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    so = sorted(dic, key=dic.get, reverse=True)
    output = ''
    for i in so:
        output += i * dic[i]
    return output
print(frequencysorts('meeeshoot'))