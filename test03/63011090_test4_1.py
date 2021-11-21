def hanoi(num,a = [],b = [],c = []):
    if num == 0 and a == [] and b == []:
        return
    if a != [] and b == [] and c == []:
        b.append(a.pop())
        print(a,b,c)
        print('a to b')
    elif len(a) != 0 and c == []:
        c.append(a.pop())
        print(a,b,c)
        print('a to c')
    elif c[-1] < b[-1] :
        b.append(c.pop())
        print(a,b,c)
        print('c to b')
    elif len(a) == 0:
        a.append(b.pop())
        print(a,b,c)
        print('b to a')
    elif c[-1] > b[-1]:
        c.append(b.pop())
        print(a,b,c)
        print('b to c')
    elif a != [] and b == []:
        b.append(a.pop())
        print(a,b,c)
        print('a to b')
    hanoi(num-1,a,b,c)



hanoi(16,[4,3,2,1])

