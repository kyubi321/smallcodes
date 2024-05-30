def three_way_sort(a):
    low = 0
    mid = 0
    high = len(a) - 1
    while mid <= high:
        if a[mid] == 'R':
            a[low], a[mid] = a[mid], a[low]
            low+=1
            mid+=1
        elif a[mid] == 'B':
            a[mid], a[high] = a[high], a[mid]
            high-=1
        else:
            mid+=1
    return a

a = ['R','G','B','R','G','B','R','G','B','R','G','B']
result = three_way_sort(a)
print(result)



