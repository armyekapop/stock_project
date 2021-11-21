
class Node:
    def __init__(self, dataval=None):
        self.data = dataval
        self.next = None

    def getNext(self):
        return self.next

    def setNext(self, newnext):
        self.next = newnext 

class SLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def __str__(self):
        str1 = ''
        printval = self.head
        if printval != None:
            str1 += str(printval.data)
            printval = printval.next
            while printval is not None:
                str1 += ' ' + str(printval.data)
                printval = printval.next
        return "Linked data : " + str1

    def sappend(self, item): 
        current = self.head
        if current:
            while current.getNext() is not None:
                current = current.getNext()
            current.setNext(Node(item))
            self.length += 1
        else:
            self.head = Node(item)
            self.length += 1
    def searchByIndex(self, x):
        position = 0
        current = self.head
        while current != None:
            if position == x:
                return current.data
            current = current.next
            position += 1
    
    def contentEquivalence(self,arr):
        arr2 = SLinkedList()
        arr2 = arr
        if arr2.length != self.length:
            return False
        else :
            for i in range(arr2.length):
                if self.searchByIndex(i) != arr2.searchByIndex(i):
                    return False
            return True

def sortlist(arr = []):
    while(True):
        x = 0
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1] and i+1 <= len(arr)-1:
                re = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = re
                x += 1
        if x == 0:
            break
    return arr


list1 , list2 = input("Enter numbers : ").split(',')
list1 = list(list1.split())
list1 = sortlist(list1)
list2 = list(list2.split())
list2 = sortlist(list2)
ll = SLinkedList()
ll2 = SLinkedList()
for el in list1:
     ll.sappend(el)
for el in list2:
     ll2.sappend(el)
print(ll.contentEquivalence(ll2))


            

