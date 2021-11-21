
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

    def removebyindex(self, num):
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
class Queue:
    def __init__(self, q = None):
        self.item = SLinkedList()
    def __str__(self) -> str:
        if self.item.__len__() == 0:
            return 'Empty Queue'
        return "Queue data : "+self.item.__str__()

    def enQueue(self, i):
        self.item.sappend(i)

    def deQueue(self):
        self.item.removebyindex(0)

    def isEmpty(self):
        return self.item.__len__() == 0
    def __len__(self):
        return self.item.__len__()
inp = int(input("Enter choice : "))
if inp == 1:
    q1 = Queue()
    q1.enQueue(10)
    q1.enQueue(20)
    q1.enQueue(30)
    print(q1)
    q1.deQueue()
    q1.enQueue(40)
    print("Size of Queue :",len(q1))
    print(q1)
if inp == 2:
    q1 = Queue()
    q1.enQueue(100)
    q1.enQueue(200)
    q1.enQueue(300)
    q1.deQueue()
    print(q1)
    print("Queue is Empty :",q1.isEmpty())
if inp == 3:
    q1 = Queue()
    q1.enQueue(11)
    q1.enQueue(22)
    q1.enQueue(33)
    q1.deQueue()
    q1.deQueue()
    q1.deQueue()
    print(q1)
    print("Size of Queue :",len(q1))
    print("Queue is Empty :",q1.isEmpty())