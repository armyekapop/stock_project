class Stack:
    def __init__(self,list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
    def __str__(self):
        s = ''
        for ele in self.items:
          s += str(ele)+' '
        return 'Data in Stack is : '+s
    def push(self,i):
        self.items.append(i)
    def pop(self):
        return self.items.pop()
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)
    def peek(self):
        return self.items[len(self.items)-1]
    def bottom(self):
        return self.items[0]
inp = int(input("Enter choice : "))
if(inp == 1):
    s1 = Stack()
    s1.push(10)
    s1.push(20)
    print(s1.__str__())
    s1.pop()
    s1.push(30)
    print("Peek of stack :",s1.peek())
    print("Bottom of stack :",s1.bottom())
if(inp == 2):
    s1 = Stack()
    s1.push(100)
    s1.push(200)
    s1.push(300)
    s1.pop()
    print(s1.__str__())
    print("Stack is Empty :",s1.isEmpty())
if(inp == 3):
    s1 = Stack()
    s1.push(11)
    s1.push(22)
    s1.push(33)
    s1.pop()
    print(s1)
    print("Stack size :",s1.size())

