from collections import deque
 
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
 
 
def isOperator(c):
    return c == '+' or c == '-' or c == '*' or c == '/' or c == '^'
 

def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data, end='')
 
 
def inorder(root):
    if root is None:
        return
 
    if isOperator(root.data):
        print('(', end='')
 
    inorder(root.left)
    print(root.data, end='')
    inorder(root.right)
 
    if isOperator(root.data):
        print(')', end='')

def Preorder(root):
 
    if root:
 
        print(root.data, end='')
 
        Preorder(root.left)
 
        Preorder(root.right)
 
def construct(postfix):
 
    if not postfix:
        return
 
    s = deque()
    for c in postfix:
        if isOperator(c):
            x = s.pop()
            y = s.pop()
 
            node = Node(c, y, x)
            s.append(node)
 
        else:
            s.append(Node(c))
    
    return s[-1]
 
def printTree90(root, level = 0):
    if root != None:
        printTree90(root.right, level + 1)
        print('     ' * level, root.data)
        printTree90(root.left, level + 1)
 
if __name__ == '__main__':
 
    postfix = input('Enter Postfix : ')
    root = construct(postfix)

    print('Tree :')
    printTree90(root)
    print('--------------------------------------------------')
    print('Infix : ', end='')
    inorder(root)
 
    print('\nPrefix : ', end='')
    Preorder(root)