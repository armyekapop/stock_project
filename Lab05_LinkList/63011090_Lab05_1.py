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
                str1 += '->' + str(printval.data)
                printval = printval.next
        return str1

    def addToFirst(self,newdata):
        NewNode = Node(newdata)
        NewNode.next = self.head
        self.head = NewNode
        self.length += 1

    def sappend(self, item):  # This is O(n) time complexity
        current = self.head
        if current:
            while current.getNext() is not None:
                current = current.getNext()
            current.setNext(Node(item))
            self.length += 1
        else:
            self.head = Node(item)
            self.length += 1

    def size(self):
        return self.length

    def isEmpty(self):
        return self.head is None

    def insertB(self,index,newdata):
        count = 0
        temp = Node(newdata)
        current = self.head
        previous = None
        found = False
        if index > self.length:
            return print('Data cannot be added')
        if index == 0:
            self.addToFirst(newdata)
            return
        if index == self.length:
            self.sappend(newdata)
            return
        while current is not None and not found:
                if count == index:
                    found = True
                else:
                    previous = current
                    current = current.getNext()
                    count += 1
        if previous is None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)
            self.length += 1

if __name__ == '__main__':
    list1 = SLinkedList()
    inp = input('Enter Input : ').split(',')
    for i in inp:
        if ':' not in i:
            H = i.split()
            for w in H:
                list1.sappend(w)
            if list1.size() == 0:
                print("List is empty")
            else:
                print('link list :',list1.__str__())
        else:
            real = i.replace(" ","")
            H = real.split(':')
            # H[0] index ------- H[1] data
            if list1.size()+1 > int(H[0]) and int(H[0]) >= 0:
                list1.insertB(int(H[0]),H[1])
                print('index =',str(H[0]) ,'and data =',H[1])
                if list1.size() == 0:
                    print("List is empty")
                else:
                    print('link list :',list1.__str__())
            else:
                print('Data cannot be added')
                if list1.size() == 0:
                    print("List is empty")
                else:
                    print('link list :',list1.__str__())
                