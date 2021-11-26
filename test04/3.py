def bubble_sort(blist):
    cmpcount, swapcount = 0, 0
    while True:
        swapped = False
        for i in range(1, len(blist)):
            cmpcount += 1
            if blist[i-1] > blist[i]:
                swapcount += 1
                blist[i-1], blist[i] = blist[i], blist[i-1]
                swapped = True
        if not swapped:
            break
    return cmpcount, swapcount
print(" *** Bubble sort ***")    
input_string = input("Enter some numbers : ")
A=[]
for n in input_string.split():
	A.append(int(n))
bubble_sort(A)
count = bubble_sort(A)
print()
print(A)
print("Data comparison =", count)