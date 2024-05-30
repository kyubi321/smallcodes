def update_count(arr, count, start, end) :
    while start < end :
        count[arr[start]] += 1
        start += 1

def mergesort_inversion_count(arr, count) :
    if len(arr) > 1 :
        mid = len(arr) // 2
        sub_array1 = arr[:mid]
        sub_array2 = arr[mid:]

        mergesort_inversion_count(sub_array1, count)
        mergesort_inversion_count(sub_array2, count)

        i = j = k = 0

        while i < len(sub_array1) and j < len(sub_array2) :
            if sub_array1[i] < sub_array2[j] :
                arr[k] = sub_array1[i]
                i += 1
            else :
                arr[k] = sub_array2[j]
                update_count(sub_array1, count, i, len(sub_array1)) # only updating count if right greater than left
                j += 1
            k += 1

        while i < len(sub_array1) :
            arr[k] = sub_array1[i]
            i += 1
            k += 1

        while j < len(sub_array2) :
            arr[k] = sub_array2[j]
            j += 1
            k += 1

arr = [7, 6, 1, 10, 23, 3]
count = {key:0 for key in arr}
print(f"Input array : {arr}")
mergesort_inversion_count(arr, count)
print(f"Inversion Count (Number:Count) : {count}")
