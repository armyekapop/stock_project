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
        if balance>1 and data<root.left.data: #leftleft
            return self.rightRotate(root)
        if balance<-1 and data>root.right.data: # right right
            return self.leftRotate(root)
        if balance>1 and data>root.left.data: #left right
            root.left=self.leftRotate(root.left)
            return self.rightRotate(root)
        if balance<-1 and data<root.right.data: #right left
            root.right=self.rightRotate(root.right)
            return self.leftRotate(root)
        return root
    def getHeight(self,root):
        if root==None:
            return 0
        return root.height
    def getBalance(self,root):
        if root==None:
            return 0
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
    def printTree(self,root,level=0):
        if root!=None:
            self.printTree(root.right,level+1)
            print('     '*level,root)
            self.printTree(root.left,level+1)
    def minValue(self,root):
        cur=root
        while cur.left!=None:
            cur=cur.left
        return cur
    def deleteNode(self,root,key):
        if root==None:
            return root
        if key<root.data:
            root.left=self.deleteNode(root.left,key)
        elif key>root.data:
            root.right=self.deleteNode(root.right,key)
        else:
            if root.left==None:
                temp=root.right
                root=None
                return temp
            elif root.right==None:
                temp=root.left
                root=None
                return temp
            temp=self.minValue(root.right)
            root.data=temp.data
            root.right=self.deleteNode(root.right,temp.data)
        return root
T=AVL()
root=None
inp=list(map(int,input('Enter Input : ').split()))
for i in inp:
    root=T.insert(root,i)
T.printTree(root)
print('==========')
root=T.deleteNode(root,20)
T.printTree(root)