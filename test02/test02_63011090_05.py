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
        return str1
    def __len__(self):
        return self.length
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

    def searchByIndex(self, num):
        temp = self.head
        index = 0
        if (temp is not None):
            if (index == num):
                self.head = temp.next
                self.length -= 1
                temp = None
                return
        while(temp is not None):
            if index == num:
                break
            prev = temp
            temp = temp.next
            index += 1
 
        if(temp == None):
            return
        prev.next = temp.next
        self.length -= 1

    
def findMode(arr):
    arr2 = SLinkedList()
    arr = arr2
    real =[]
    number = []
    for i in range(arr.length):
        number[i] = arr.search()

inputlist = [int(e) for e in input('Enter numbers : ').split()]
l = SLinkedList()
for el in inputlist:
    l.sappend(el)
print("Output :")
print(l)
print('Amount of data =',len(l))
findMode(l)