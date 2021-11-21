list1 = []
list1 = [int(e) for e in input("Enter All Bid : ").split()]
list1.sort()
x = list1[0:-1]
if len(list1)>1:
    if list1[-1] in x:
        print("error : have more than one highest bid")
    else:
        print("winner bid is",list1[-1],"need to pay",list1[-2])
else:
    print("not enough bidder")

