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

    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

inp = input("Enter numbers : ").split()
ll = SLinkedList()
for el in inp:
    ll.sappend(el)
print("Linkedlist Before Reverse")
print(ll.__str__())
print("Linkedlist After Reverse")
ll.reverse()
print(ll.__str__())