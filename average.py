def average_in_file():
    with open('text.txt','r') as f:
        data = f.readlines()
    values = [float(i) for i in data]
    total = 0
    for i in values:
        total += i
        average = total / len(values)

    return average
print(average_in_file())