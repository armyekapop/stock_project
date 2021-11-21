# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
    
#     def __str__(self):
#         return str(self.data)

# class BinarySearchTree():
#     def __init__(self):
#         self.root = None

#     def insert(self,data):
#         if self.root == None:
#             self.root = Node(data)
#         else:
#             currentNode = self.root
#             while True:
#                 if data < currentNode.data:
#                     if currentNode.left:
#                         currentNode = currentNode.left
#                     else:
#                         currentNode.left = Node(data)
#                         break
#                 elif data > currentNode.data:
#                     if currentNode.right:
#                         currentNode = currentNode.right
#                     else:
#                         currentNode.right = Node(data)
#                         break
#                 else:
#                     break
#         return self.root

#     def deleteNode(self, node, data):
#         if node is None:
#             return node
        
#         if data < node.data:
#             node.left = self.deleteNode(node.left, data)
#             return node
#         elif data > node.data:
#             node.right = self.deleteNode(node.right, data)
#             return node

#         if node.left is None and node.right is None:
#             return None
#         if node.left is None:
#             temp = node.right
#             node = None
#             return temp
#         elif node.right is None:
#             temp = node.left
#             node = None
#             return temp
        
#         succParent = node
#         succ = node.right
#         while succ.left!=None:
#             succParent = succ
#             succ = succ.left
#         if succParent!=node:
#             succParent.left = succ.right
#         else:
#             succParent.right = succ.left

#         node.data = succ.data
        
#         return node

# def findMax(a, b):
#     if a >= b:
#       return a
#     else:
#       return b
# def findHeight(root):
#     if root is None:
#       return 0

#     return findMax(findHeight(root.left),findHeight(root.right))+1

# def findNode(node, key):
 
#     if (node == None):
#         return False
 
#     if (node.data == key):
#         return True
 
#     res1 = findNode(node.left, key)
#     if res1:
#         return True
#     res2 = findNode(node.right, key)
 
#     return res2

# def printTree90(node, level = 0):
#     if node != None:
#         printTree90(node.right, level + 1)
#         print('     ' * level, node)
#         printTree90(node.left, level + 1)


# tree = BinarySearchTree()
# root = None
# data = input("Enter Input : ").split(",")
# for el in data:
#     el = el.split()
#     el[1] = int(el[1])
#     if el[0] == 'i':
#         print('insert',el[1])
#         root = tree.insert(el[1])
#         printTree90(tree.root)
#     elif el[0] == 'd':
#         print('delete',el[1])
#         if findNode(tree.root,el[1]) == True:
#             if findHeight(tree.root) == 1:
#                 tree.root = None
#             elif not tree.root.left and tree.root.data == el[1]:
#                 tree.root = tree.root.right
#                 printTree90(tree.root)
#             elif not tree.root.right and tree.root.data == el[1]:
#                 tree.root = tree.root.left
#                 printTree90(tree.root)
#             else:
#                 tree.deleteNode(root,el[1])
#                 printTree90(tree.root)
#         else:
#             print('Error! Not Found DATA')
#             printTree90(tree.root)
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
    def findmin(self, root):
        current = root
        while current.left:
            current = current.left
        return current
    
    def deleteNode(self, root: Node, key: int) -> Node:
        if not root:
            return root
        elif key < root.data:
            root.left = self.deleteNode(root.left, key)
        
        elif key > root.data:
            root.right = self.deleteNode(root.right, key)
        
        else:
            #leaf
            if not root.left and not root.right:
                root = None
            
            # 1 child
            elif not root.left:
                root = root.right

            elif not root.right:
                root = root.left
            
            else:
                temp = self.findmin(root.right)
                root.data = temp.data
                root.right = self.deleteNode(root.right, temp.data)
        return root

def findMax(a, b):
    if a >= b:
      return a
    else:
      return b
def findHeight(root):
    if root is None:
      return 0

    return findMax(findHeight(root.left),findHeight(root.right))+1;
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

def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)


tree = BinarySearchTree()
data = input("Enter Input : ").split(",")
for el in data:
    el = el.split()
    el[1] = int(el[1])
    if el[0] == 'i':
        print('insert',el[1])
        tree.insert(el[1])
        printTree90(tree.root)
    elif el[0] == 'd':
        print('delete',el[1])
        if findNode(tree.root,el[1]) == True:
            if findHeight(tree.root) == 1:
                tree.root = None
            else:
                tree.deleteNode(tree.root,el[1])
                printTree90(tree.root)
        else:
            print('Error! Not Found DATA')
            printTree90(tree.root)