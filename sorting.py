def quick_sort(sequence):
    if len(sequence) <= 1:
        # if length of the array becomes less than 1 then return that sequence
        return sequence
    else:
        # taking out the pivot element from the sequence that is the end value
        pivot = sequence.pop()
    smaller_list = []
    largest_list = []
    # here we are comparing the elements in the sequence with the pivot element
    # and partitioning our list into two largest and the smallest
    for i in sequence:
        if i < pivot:
            smaller_list.append(i)
        else:
            largest_list.append(i)
    return quick_sort(smaller_list) + [pivot] + quick_sort(largest_list)


def bubble_sort():
    x = int(input("enter the number of values in the array : "))
    print(f'enter the {x} values in the array : ')
    a = []
    for i in range(x):
        value = int(input(f'{i + 1}::'))
        a.append(value)
    print(f'The unsorted array is :  {a}\n')

    print("bubble sort ")
    # in bubble sort we take two elements and compare it then swaps accordingly
    for i in range(len(a)):

        for j in range(0, len(a) - i - 1):  # here length of a - i - 1 is done to prevent from unnecessary comparisions
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    print(f'the sorted array is : {a}')


def selection_sort():
    x = int(input("enter the number of values in the array : "))
    print(f'enter the {x} values in the array : ')
    a = []
    for i in range(x):
        value = int(input(f'{i + 1}::'))
        a.append(value)
    print(f'The unsorted array is :  {a}\n')

    print('selection sort')
    for i in range(len(a)):
        # we assume the first position is the minimum then we check if there is any bigger value than the minimum then we change teh minimum and swap it
        min = i
        for j in range(i + 1, len(a)):
            if a[min] > a[j]:
                min = j
        temp = a[i]
        a[i] = a[min]
        a[min] = temp
    print(f'The sorted array is : {a}')


def insertion_sort():
    x = int(input("enter the number of values in the array : "))
    print(f'enter the {x} values in the array : ')
    a = []
    for i in range(x):
        value = int(input(f'{i + 1}::'))
        a.append(value)
    print(f'The unsorted array is :  {a}\n')

    print("insertion sort ")
    for i in range(1, len(a)):
        #
        temp = a[i]
        j = i - 1
        while j >= 0 and a[j] > temp:
            a[j + 1], a[j] = a[j], a[j + 1]
            j -= 1
    print(f'The sorted array is : {a}')


a = [1, 3, 2, 6, 9, 0]


def two_symbols():
    x = int(input("enter the number of values in the array : "))
    print("enter the symbol '0' or '+' in any order you want :\n")
    print(f'enter the {x} values in the array : ')
    a = []
    for i in range(x):
        value = input(f'{i + 1}::')
        a.append(value)
    print(f'The unsorted array is :  {a}\n')

    low = 0
    high = len(a) - 1
    while low <= high:
        if a[low] == '0':
            low += 1
        elif a[low] == '+':
            a[low], a[high] = a[high], a[low]
            high -= 1
        else:
            pass
    print(f'The sorted array is : {a}')


def three_way_sort():
    x = int(input("enter the number of values in the array : "))
    print("enter the symbol 'R' or 'G' or 'B 'in any order you want :\n")
    print(f'enter the {x} values in the array : ')
    a = []
    for i in range(x):
        value = input(f'{i + 1}::')
        a.append(value)
    print(f'The unsorted array is :  {a}\n')

    low = 0
    mid = 0
    high = len(a) - 1
    while mid <= high:
        if a[mid] == 'R':
            a[low], a[mid] = a[mid], a[low]
            low += 1
            mid += 1
        elif a[mid] == 'G':
            mid += 1
        else:
            a[mid], a[high] = a[high], a[mid]
            high -= 1

    print(f'The sorted array is : {a}')


choice = input("enter the type of sort you want to do : \n"
               "1.bubble sort \n"
               "2.selection sort\n"
               "3.insertion sort\n"
               "4.two way sort\n"
               "5.three way sort\n"
               "6.quick sort\n"
               "7.exit\n :"
               )
print('\n')
match choice.strip():
    case '1':
        bubble_sort()
    case '2':
        selection_sort()
    case '3':
        insertion_sort()
    case '4':
        two_symbols()
    case '5':
        three_way_sort()
    case '6':
        x = int(input("enter the number of values in the array : "))
        print(f'enter the {x} values in the array : ')
        sequence = []
        for i in range(x):
            value = int(input(f'{i + 1}::'))
            sequence.append(value)
        print(f'The unsorted array is :  {sequence}\n')
        print(quick_sort(sequence))
    case'exit':
        print("you successfully exited ")
