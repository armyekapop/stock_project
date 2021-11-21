class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)           

    def pop(self):
        result = -1

        if self.stack != []:
            result = self.stack.pop()

        return result
    
    def isEmpty(self):
        return self.stack == []
    
    def topChar(self):
        result = -1

        if self.stack != []:
            result = self.stack[len(self.stack) - 1]

        return result

def isOperand(c):
    return c not in {'+','-','*','/','^','(',')'}

operators = "+-*/^"

def isOperator(c):
    return c in operators

def getPrecedence(c):
    result = 0

    for char in operators:
        result += 1

        if char == c:
            if c in '-/':
                result -= 1
            break

    return result

def toPostfix(expression):
    result = ""

    stack = Stack()

    for char in expression:
        if isOperand(char):
            result += char
        elif isOperator(char):
            while True:
                topChar = stack.topChar()

                if stack.isEmpty() or topChar == '(':
                    stack.push(char)
                    break
                else:
                    pC = getPrecedence(char)
                    pTC = getPrecedence(topChar)

                    if pC > pTC:
                        stack.push(char)
                        break
                    else:
                        result += stack.pop()

        elif char == '(':
            stack.push(char)
        elif char == ')':
            cpop = stack.pop()

            while cpop != '(':
                result += cpop
                cpop = stack.pop()

    while not stack.isEmpty():
        cpop = stack.pop()
        result += cpop

    return result

if __name__ == '__main__':
    inp = input('Enter Infix : ')
    postfix = toPostfix(inp)
    print("Postfix :",postfix)
    