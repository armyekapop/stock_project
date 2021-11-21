def sortArray(a, n):
 
    ans=[]
    for i in range(n):
        if (a[i] >= 0):
            ans.append(a[i])
 
    ans = sorted(ans)
 
    j = 0
    for i in range(n):

        if (a[i] >= 0):
            a[i] = ans[j]
            j += 1
 
    for i in range(n):
        print(a[i],end = " ")
 
 
arr = list(map(int, input("Enter Input : ").split()))
 
n = len(arr)
 
sortArray(arr, n)