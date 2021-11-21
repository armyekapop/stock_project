def odd_list(al) :
    odd = [num for num in al if num %2 == 1]
    return odd
list1 = []
print(" ***Function Odd List***")
list1 = [int(e) for e in input("Enter list numbers : ").split()]
print("Input list : ",list1,"\nOutput list : ",odd_list(list1))