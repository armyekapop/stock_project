class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
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
                
def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

def findNode(node, key):
 
    if (node == None):
        return False
 
    if (node.data == key):
        return True
 
    res1 = findNode(node.left, key)
    if res1:
        return True
    res2 = findNode(node.right, key)
 
    return res2

def findParent(node : Node,val : int,parent : int) -> None:
    if (node == None):
        return 
 
    if (node.data == val):
        if parent == -1:
            print('None Because',val,'is Root')
            return 1
        print(parent)
        return 1
    else:
        findParent(node.left,val, node.data)
        findParent(node.right,val, node.data)

    
        
tree = BinarySearchTree()
data = input("Enter Input : ").split("/")
for e in data[0].split():
    tree.create(e)
printTree90(tree.root)
if findNode(tree.root,data[1]) == True:
    findParent(tree.root,data[1],-1)
else:
    print('Not Found Data')
        
    