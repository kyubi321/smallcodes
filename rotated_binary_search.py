def rotated_binary_search(a, search):
    low = 0
    high = len(a)-1
    while low <= high:
        mid = (low + high) // 2
        if a[mid] == search:
            return mid
        # left is sorted
        if a[low] <= a[mid]:
            # print(low, mid, high)
            if search >= a[low] and search < a[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if search > a[mid] and search <= a[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1

a = [4,5,6,7,0,1,2]
target = 5
result = rotated_binary_search(a, target)
if result == -1:
    print("the element is not found ")
else:
    print("the element is  present")






