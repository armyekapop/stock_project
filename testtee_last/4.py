class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
    def __str__(self):
        return str(self.data)
class Stack:
    def __init__(self,li=None):
        if li==None:
            self.items=[]
        else:
            self.items=li
    def __str__(self):
        return ''.join(self.items)
    def isEmpty(self):
        return self.items==[]
    def push(self,data):
        self.items.append(data)
    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
class BST:
    def __init__(self):
        self.root=None
    def insertPostfix(self,inp):
        opreration=Stack()
        for i in inp:
            if i in '+-*/':
                behind=opreration.pop()
                front=opreration.pop()
                opreration.push(Node(i,front,behind))
            else:
                opreration.push(Node(i))
        self.root=opreration.pop()
        return self.root
    def printTree(self,root,level=0):
        if root!=None:
            self.printTree(root.right,level+1)
            print('     '*level,root)
            self.printTree(root.left,level+1)
    def printinfix(self,root,level=0):
        if root!=None:
            if root.left!=None and root.right!=None:
                print('(',end='')
            self.printinfix(root.left,level+1)
            print(root,end='')
            self.printinfix(root.right,level+1)
            if root.left!=None and root.right!=None:
                print(')',end='')
    def printprefix(self,root,level=0):
        if root!=None:
            print(root,end='')
            self.printprefix(root.left,level+1)
            self.printprefix(root.right,level+1)
T=BST()
root=None
inp=input('Enter Input : ')
root=T.insertPostfix(inp)
T.printTree(root)
T.printinfix(root)
print('')
T.printprefix(root)