def insertion_sort(data):
    for i in range(1, len(data)):
        iEle = data[i]
        for j in range(i, -1, -1):
            if iEle < data[j-1] and j > 0:
                data[j] = data[j-1]
            else:
                data[j] = iEle
                break

inp = [int(e) for e in input("Enter Input: ").split()]
insertion_sort(inp)
print(inp)