def binary_ser(sort, element, high, low):
    mid = low + (high - low )//2
    if sort[mid] == element:
        return 1
    elif element > sort[mid]:
        binary_ser(sort, element,high, mid + 1)
    else:
        binary_ser(sort, element,mid-1, low)

    return -1


print("********************** binary search program ******************** ")
high = int(input("enter the number of values in the list :"))
sort = []
low = 0
for i in range(high):
    value = int(input("enter the number to be inserted in the list : "))
    sort.append(value)
sort.sort()
print("the entered list :  ", sort)
element = int(input("enter the number to be searched :"))
result = binary_ser(sort, element, high, low)
if result == 1:
    print("the element is in the list ")
else:
    print("the element is not in the list ")
