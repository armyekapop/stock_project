def poww(num,pownum):
    if pownum == 0:
        return 1
    if pownum == 1:
        return num
    else:
        return num * poww(num,pownum-1)
A = input("Enter Input a b : ").split()
listA = list(map(int,A))
print(poww(listA[0],listA[-1]))