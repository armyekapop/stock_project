from itertools import combinations
def rSubset(arr, r):
    return list(combinations(arr, r)) 
list1 = input("Enter Your List : ")
r_arr = list(list1.split(" "))
list_unsort = [int(i) for i in r_arr]
new = sorted(list_unsort)
if len(new)<3:
    print("Array Input Length Must More Than",len(new))
else:
    combi = rSubset(new,3)
    en = []
    for i in range(len(combi)):
        if sum(combi[i]) == 5 and combi[i] not in en :
            en.append(combi[i])
    list2 = str(en)
    print(list2.replace("(","[").replace(")","]"))
