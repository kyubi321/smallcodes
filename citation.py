def hIndex(citations):
    citations.sort()
    n = len(citations)
    h = 0  # Initialize h-index to 0

    for i in range(n - 1, -1, -1):
        if citations[i] >= h:
            h += 1
        else:
            break

    return h


citations = [3, 0, 6, 1, 5]
result = hIndex(citations)
print(result)

