def selection_sort(data):
    for last in range(len(data)-1, -1, -1):
        biggest = data[0]
        biggest_i = 0
        for i in range(1, last+1):
            if data[i] > biggest:
                biggest = data[i]
                biggest_i = i
        data[last], data[biggest_i] = data[biggest_i], data[last]

inp = [int(e) for e in input("Enter Input: ").split()]
selection_sort(inp)
print(inp)