class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

class AVL_Tree(object):
 
    def insert(self, root, key):
     
        if not root:
            return TreeNode(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
 
        root.height = 1 + max(self.getHeight(root.left),
                           self.getHeight(root.right))
 
        balance = self.getBalance(root)
 
        if balance > 1 and key <= root.left.val:
            print("Right Right Rotation")
            return self.rightRotate(root)
 
        if balance < -1 and key >= root.right.val:
            print("Left Left Rotation")
            return self.leftRotate(root)

        if balance > 1 and key >= root.left.val:
            print("Left Right Rotation")
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
 
        if balance < -1 and key <= root.right.val:
            print("Right Left Rotation")
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
 
        return root
 
    def leftRotate(self, z):
 
        y = z.right
        T2 = y.left
 
        y.left = z
        z.right = T2

        z.height = 1 + max(self.getHeight(z.left),
                         self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                         self.getHeight(y.right))
 
        return y
 
    def rightRotate(self, z):
 
        y = z.left
        T3 = y.right
 
        y.right = z
        z.left = T3
 
        z.height = 1 + max(self.getHeight(z.left),
                        self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                        self.getHeight(y.right))
 
        return y
 
    def getHeight(self, root):
        if not root:
            return 0
 
        return root.height
 
    def getBalance(self, root):
        if not root:
            return 0
 
        return self.getHeight(root.left) - self.getHeight(root.right)

    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node.val)
            self.printTree(node.left, level + 1)
 
print(" *** AVL Tree Insert Element ***")
myTree = AVL_Tree()
root = None
data = input("Enter Input : ").split()
for e in data:
    print('insert : {} '.format(e))
    root = myTree.insert(root, int(e))
    myTree.printTree(root)
    print('====================')

