def shell_sort(l, dIncrements):
    cc = 0
    for inc in dIncrements:
        for i in range(inc, len(l)):
            iEle = l[i]
            for j in range(i, -1, -inc):
                if iEle<l[j-inc] and j >= inc:
                    cc +=1
                    l[j] = l[j-inc]
                else:
                    cc +=1
                    l[j] = iEle
                    break
            cc +=1
            
    return cc
input_string = input("Enter some numbers : ")
A=[]
for n in input_string.split():
	A.append(int(n))
dIncrements = [3,1]
shell_sort(A, dIncrements)
print(A)
print("Data comparison = ",shell_sort(A, dIncrements))