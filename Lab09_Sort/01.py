def bubble_sort(ar):
   
    if len(ar) <= 1:
        return ar
       
    if len(ar) == 2:
        return ar if ar[0] < ar[1] else [ar[1], ar[0]]
 
    a, b = ar[0], ar[1]
 
    bs = ar[2:]

    res = []
     
    if a < b:
        res = [a] + bubble_sort([b] + bs)

    else:
        res = [b] + bubble_sort([a] + bs)
         
    return bubble_sort(res[:-1]) + res[-1:]
 
arr = list(map(int, input("Enter Input : ").split()))
res = bubble_sort(arr)
print([*res])