class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
        self.height=1
    def __str__(self):
        return str(self.data)
class AVL:
    def __init__(self):
        pass
    def insert(self,root,data):
        if root==None:
            root=Node(data)
            return root
        else:
            if data<root.data:
                root.left=self.insert(root.left,data)
            else:
                root.right=self.insert(root.right,data)
        root.height=max(self.getHeight(root.left),self.getHeight(root.right))+1
        balance=self.getBalance(root)
        if balance>1 and data<root.left.data: # left left
            return self.rightRotate(root)
        if balance<-1 and data>root.right.data:  #right right
            return self.leftRotate(root)
        if balance>1 and data>root.left.data: #left right
            root.left=self.leftRotate(root.left)
            return self.rightRotate(root)
        if balance<-1 and data<root.right.data:
            root.right=self.rightRotate(root.right)
            return self.leftRotate(root)
        return root 
    def getHeight(self,root):
        if root==None:
            return 0
        else:
            return root.height
    def getBalance(self,root):
        if root==None:
            return 0
        else:
            return self.getHeight(root.left)-self.getHeight(root.right)
    def leftRotate(self,z):
        y=z.right
        T2=y.left
        y.left=z
        z.right=T2
        z.height=max(self.getHeight(z.left),self.getHeight(z.right))+1
        y.height=max(self.getHeight(y.left),self.getHeight(y.right))+1
        return y
    def rightRotate(self,z):
        y=z.left
        T3=y.right
        y.right=z
        z.left=T3
        z.height=max(self.getHeight(z.left),self.getHeight(z.right))+1
        y.height=max(self.getHeight(y.left),self.getHeight(y.right))+1
        return y
    def print_tree(self,root,level=0):
        if root!=None:
            self.print_tree(root.right,level+1)
            print('     '*level,root)
            self.print_tree(root.left,level+1) 
    def printinorder(self,root):
        if root!=None:
            self.printinorder(root.left)
            print(root,end=' ')
            self.printinorder(root.right)
    def printpreorder(self,root):
        if root!=None:
            print(root,end=' ')
            self.printpreorder(root.left)
            self.printpreorder(root.right)
    def printposorder(self,root):
        if root!=None:
            self.printposorder(root.left)
            self.printposorder(root.right)
            print(root,end=' ')

T=AVL()
root=None
inp=list(map(int,input('Enter some numbers : ').split()))
for i in inp:
    root=T.insert(root,i)
T.print_tree(root)
T.printinorder(root)
print('')
T.printpreorder(root)
print('')
T.printposorder(root)