def findMax(list1):
    if len(list1) == 1:
        return list1[0]
    else:
        return findMax(list1[1:]) if findMax(list1[1:]) > list1[0] else list1[0]

A = input("Enter Input : ").split()
listA = list(map(int,A))
print('Max :',findMax(listA))