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

    def removebyindex(self, num):
        temp = self.head
        index = 0
        if (temp is not None):
            if (index == num):
                self.head = temp.next
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
    curs = '|'
    list1.addToFirst(curs)
    curr_position = list1.search(curs)
    for i in inp:
        if i[0] == ' ':
            real = i.replace(' ','',1)
            H = list(real.split())
        else:
            H = list(i.split())
        if H[0] == 'I':
            have, curr_position = list1.search(curs)
            list1.insertB(curr_position,H[1])
            # print(list1.__str__())
        elif H[0] == 'L':
            have, curr_position = list1.search(curs)
            if curr_position > 0:
                list1.remove(curs)
                list1.insertB(curr_position-1,curs)
        elif H[0] == 'R':
            have, curr_position = list1.search(curs)
            if curr_position >= 0 and curr_position < list1.size():
                list1.remove(curs)
                list1.insertB(curr_position+1,curs)
        elif H[0] == 'B':
            have, curr_position = list1.search(curs)
            if curr_position > 0:
                list1.removebyindex(curr_position-1)
        elif H[0] == 'D':
            have, curr_position = list1.search(curs)
            if curr_position < list1.size():
                list1.removebyindex(curr_position+1)

    print(list1.__str__())