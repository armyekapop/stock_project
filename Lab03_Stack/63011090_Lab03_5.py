class Stack:
    def __init__(self,list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
    def push(self,i):
        self.items.append(i)
    def pop(self):
        return self.items.pop()
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)

if __name__ == '__main__':
    print("******** Parking Lot ********")
    S = Stack()
    m,s,o,n = input("Enter max of car,car in soi,operation : ").split()
    m,n = int(m),int(n)
    H = list(s.split(","))
    Rlist = []
    if(o == 'arrive'):
        if(len(H)+1 <= m and str(n) not in H and s != '0'):
            H.append(n)
            w = len(H)
            print("car",n,"arrive! : Add Car",n)
            while(w>0):
                S.push(int(H[w-1]))
                w -= 1
        elif(len(H)+1 > m ):
            print("car",n,"cannot arrive : Soi Full")
            w = len(H)
            while(w>0):
                S.push(int(H[w-1]))
                w -= 1
        elif(len(H)+1 <= m and str(n) in H and s != '0'):
            print("car",n,"already in soi")
            w = len(H)
            while(w>0):
                S.push(int(H[w-1]))
                w -= 1
        elif(s == '0'):
            print("car",n,"arrive! : Add Car",n)
            S.push(int(n))
        while(not S.isEmpty()):
            x = S.pop()
            Rlist.append(x)
    if(o == 'depart'):
        w = len(H)
        while(w>0):
            S.push(int(H[w-1]))
            w -= 1
        if(s == '0'):
            print("car",n,"cannot depart : Soi Empty")
        elif(str(n) in H):
            print("car",n,"depart ! : Car",n,"was remove")
            while(not S.isEmpty()):
                x = S.pop()
                if(x != n):
                    Rlist.append(x)
        elif(str(n) not in H):
            print("car",n,"cannot depart : Dont Have Car",n)
            while(not S.isEmpty()):
                x = S.pop()
                Rlist.append(x)
    print(Rlist)
