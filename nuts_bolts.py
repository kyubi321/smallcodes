def partition(arr, low, high, pivot):
    i = low
    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        elif arr[j] == pivot:
            arr[j], arr[high] = arr[high], arr[j]
            j -= 1
    arr[i], arr[high] = arr[high], arr[i]
    return i


def matchPairs(nuts, bolts, low, high):
    if low < high:
        # Choose a random pivot from nuts and use it to partition bolts
        pivot_index = partition(bolts, low, high, nuts[low])

        # Partition nuts using the matching bolt
        partition(nuts, low, high, bolts[pivot_index])

        # Recursively match pairs in the left and right subarrays
        matchPairs(nuts, bolts, low, pivot_index - 1)
        matchPairs(nuts, bolts, pivot_index + 1, high)


# Example usage:
nuts = [4,6,1,7]
bolts = [7,1,6,4]
matchPairs(nuts, bolts, 0, len(nuts) - 1)

# Print the matching pairs
for i in range(len(nuts)):
    print(nuts[i], "matches", bolts[i])

