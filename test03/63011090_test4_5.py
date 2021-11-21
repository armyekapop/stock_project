class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 

class BST:
    def __init__(self): 
        self.root = None

    def insert(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break
    def printTree(self,node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node.data)
            self.printTree(node.left, level + 1)

def findMin(root):
    if root.left is None:
        print("Min :",root.data)
        return
    findMin(root.left)

def findMax(root):
    if root.right is None:
        print("Max :",root.data)
        return
    findMax(root.right)



T = BST()

inp = [int(i) for i in input('Enter Input : ').split()]

for i in inp:

    root = T.insert(i)

T.printTree(T.root)

print('-' * 50)

findMin(T.root)
findMax(T.root)