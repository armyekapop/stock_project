def printAllSubsetsRec(arr, n, v, sum) :
 
    # If remaining sum is 0, then print all
    # elements of current subset.
    if (sum == 0) :
        for value in v :
            print(value, end=" ")
        print()
        return
     
 
    # If no remaining elements,
    if (n == 0):
        return
 
    # We consider two cases for every element.
    # a) We do not include last element.
    # b) We include last element in current subset.
    printAllSubsetsRec(arr, n - 1, v, sum)
    v1 = [] + v
    v1.append(arr[n - 1])
    printAllSubsetsRec(arr, n - 1, v1, sum - arr[n - 1])
 
 
# Wrapper over printAllSubsetsRec()
def printAllSubsets(arr, n, sum):
 
    v = []
    printAllSubsetsRec(arr, n, v, sum)
 

# arr = [20 ,10 ,5 ,5 ,3 ,2 ,20 ,10]
# num = 20
# res= len(arr)
# printAllSubsets(arr,num,res)

arr = [ 20 ,10 ,5 ,5 ,3 ,2 ,20 ,10 ]
sum = 20
n = len(arr)
printAllSubsets(arr, n, sum)
