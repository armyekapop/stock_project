class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 

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

def height(obj):
    if obj is None:
        return -1

    if height(obj.left) >= height(obj.right):
        temp = height(obj.left)
    else:
        temp = height(obj.right)
    return temp+1


print(" *** Binary Search Tree Height ***")

tree = BinarySearchTree()

arr = list(map(int, input("Enter Input : ").split()))

for e in arr:

    tree.create(e)



print("Height = ",height(tree.root),end="\n\n")