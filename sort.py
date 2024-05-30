
def quick_sort(sequence):
    sequence2 = [2,4,6,1,8,9]
    if len(sequence2) <= 1:
        # if length of the array becomes less than 1 then return that sequence
        return sequence
    else:
        # taking out the pivot element from the sequence that is the end value
        pivot = sequence.pop()
    smaller_list = []
    largest_list = []
    # here we are comparing the elements in the sequence with the pivot element
    # and partitioning our list into two largest and the smallest
    for i in sequence2:
        if i <= pivot:
            smaller_list.append(i)
        else:
            largest_list.append(i)
    return quick_sort(smaller_list) + [pivot] + quick_sort(largest_list)

sequence =[6,9,8,2,1,4]
print(quick_sort(sequence))

def merge_sort(sequence):
    # if only lenght of the array is greater than 1 then only division is possible
    if len(sequence) > 1:
        left_array = sequence[:len(sequence)//2]
        right_array = sequence[len(sequence)//2:]
        # recursivily calling the function so that only one element is available
        merge_sort(left_array)
        merge_sort(right_array)
        # initializing variable sfor i,j,k
        count = 0
        i = 0
        j = 0
        k = 0
        # comparing elements and appending
        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                sequence[k] = left_array[i]
                i += 1

            else:
                sequence[k] = right_array[j]
                j += 1
            k += 1
            # adding remaing elents in array
        while i < len(left_array):
            sequence[k] = left_array[i]
            i += 1
            k += 1
        while j < len(right_array):
            sequence[k] = right_array[j]
            j += 1
            k += 1

        return sequence

sequence=[4,2,6,1,8,5,9,6]
print(merge_sort(sequence))


