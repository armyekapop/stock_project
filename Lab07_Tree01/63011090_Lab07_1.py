class Node:
    left = right = None
    def __init__(self, data):
        self.data = data
 
def inorder(root):
 
    if root is None:
        return
 
    inorder(root.left)
    print(root.data, end=' ')
    inorder(root.right)
 
def insert(root, key):
 
    if root is None:
        return Node(key)
 
    if key < root.data:
        root.left = insert(root.left, key)

    else:
        root.right = insert(root.right, key)
 
    return root
def printTree(node, level = 0):
        if node != None:
            printTree(node.right, level + 1)
            print('     ' * level, node.data)
            printTree(node.left, level + 1)
def findMax(a, b):
    if a >= b:
      return a
    else:
      return b
def findHeight(root):
    if root is None:
      return 0

    return findMax(findHeight(root.left),findHeight(root.right))+1;

if __name__ == '__main__':
    root = None
    inp = [int(i) for i in input('Enter Input : ').split()]
    for i in inp:
        root = insert(root,i)
    printTree(root)