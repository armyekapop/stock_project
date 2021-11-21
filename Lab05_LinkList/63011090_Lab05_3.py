class node:
    def __init__(self,data,next = None ):
        self.data = data
        if next == None:
            self.next = None
        else:
            self.next = next
            
    def __str__(self):
        s = ""
        while self.next is not None:
            s+=str(self.data)+' '
            self = self.next
        return s

    def __len__(self):
        lenght = 0
        while self.next is not None:
            lenght+=1
            self = self.next
        return lenght

def createList(l=[]):
    head = LL = node(l[0])
    for i in l[1:]:
        LL.next = node(i)
        LL = LL.next
    LL.next = node(l[-1])
    LL = LL.next
    return head

def printList(H):
    print(H)

def mergeOrderesList(p,q):
    size_1 = len(p)
    size_2 = len(q)

    res = []
    i, j = 0, 0
  
    while p.next is not None and q.next is not None:
        if int(p.data) < int(q.data):
            res.append(p.data)
            p = p.next
            i += 1
        else:
            res.append(q.data)
            q = q.next
            j += 1
    
    while p.next!=None:
        res.append(p.data)
        p=p.next
    while q.next!=None:
        res.append(q.data)
        q=q.next
    result = createList(res)
    return result

#################### FIX comand ####################   
L1,L2 = input('Enter 2 Lists : ').split()
L1 = L1.split(',')
L2 = L2.split(',')
LL1 = createList(L1)
LL2 = createList(L2)
print('LL1 : ',end='')
printList(LL1)
print('LL2 : ',end='')
printList(LL2)
m = mergeOrderesList(LL1,LL2)
print('Merge Result : ',end='')
printList(m)