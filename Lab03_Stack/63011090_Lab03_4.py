from os import remove


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
    def peek(self):
        return self.items[-1]

if __name__ == '__main__':
    S = Stack()
    inp = input('Enter Input : ').split(',')
    num = []
    for i in inp:
        H = list(i.split())
        if(H[0] == 'A'):
            if(S.isEmpty()):
                S.push(int(H[-1]))
            else:
                if S.peek() > int(H[-1]):
                    S.push(int(H[-1]))
                else:
                    k =0
                    while(not S.isEmpty()):
                        x = S.peek()
                        if(x < int(H[-1])):
                            S.pop()
                            k +=1
                        if(x > int(H[-1])):
                            S.push(int(H[-1]))
                            break
                        if(x == int(H[-1])):
                            break
                    if(S.isEmpty()):
                        S.push(int(H[-1]))
        if(H[0] == 'B'):
            print(S.size())
            

            
