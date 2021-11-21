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

    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def search(self, x):
        position = 0
        current = self.head
        while current != None:
            if current.data == x:
                return True,position
            current = current.next
            position += 1
        return False,position
    def remove(self, ele):
        temp = self.head
        if (temp is not None):
            if (temp.data == ele):
                self.head = temp.next
                temp = None
                return
        while(temp is not None):
            if temp.data == ele:
                break
            prev = temp
            temp = temp.next
 
        if(temp == None):
            return
        prev.next = temp.next

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
    inp = input("Enter Input : ").split(",")
    for i in inp:
        if i[0] == ' ':
            real = i.replace(' ','',1)
            H = list(real.split())
        else:
            H = list(i.split())
        if H[0] == 'A':
            list1.sappend(H[1])
            print('linked list :',list1.__str__())
            list1.reverse()
            print('reverse :',list1.__str__())
            list1.reverse()
        elif H[0] == 'Ab':
            list1.addToFirst(H[1])
            print('linked list :',list1.__str__())
            list1.reverse()
            print('reverse :',list1.__str__())
            list1.reverse()
        elif H[0] == 'R':
            status, index = list1.search(H[1])
            if status:
                list1.remove(H[1])
                print('removed :',H[1],'from index :',index)
                print('linked list :',list1.__str__())
                list1.reverse()
                print('reverse :',list1.__str__())
                list1.reverse()
            else:
                print('Not Found!')
                print('linked list :',list1.__str__())
                list1.reverse()
                print('reverse :',list1.__str__())
                list1.reverse()
        elif H[0] == 'I':
            H1 = list(H[1].split(':'))
            if list1.size()+1 > int(H1[0]) and int(H1[0]) >= 0:
                list1.insertB(int(H1[0]),H1[1])
                print('index =',str(H1[0]) ,'and data =',H1[1])
                print('linked list :',list1.__str__())
                list1.reverse()
                print('reverse :',list1.__str__())
                list1.reverse()
            else:
                print('Data cannot be added')
                print('linked list :',list1.__str__())
                list1.reverse()
                print('reverse :',list1.__str__())
                list1.reverse()
        
            