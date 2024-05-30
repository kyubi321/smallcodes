def Search(sort,n,element):
    for i in range (0,n):
        if sort[i] == element:
            return 1
    return -1

print("**********************linear search program******************** ")
n=int(input("enter the number of values in the list :"))
sort=[]
for i in range(n):
    value=int(input("enter the number to be inserted in the list : "))
    sort.append(value)
print("the entered list :  ", sort)
element=int(input("enter the number to be searched :"))
result = Search(sort ,n,element)
if result == 1:
    print("the element is found in the list")
else:
    print("the element is not found in the list")






