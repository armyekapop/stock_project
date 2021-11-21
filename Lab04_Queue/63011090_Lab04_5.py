from collections import deque
class Queue2:
    def __init__(self, q = None):
      if q == None:
        self.items = deque()
      else:
        self.items = deque(q,len(q))
    def __str__(self):
        s = ''
        for ele in self.items:
          s += str(ele)+' '
        return s
    def enQueue(self, i):
      self.items.append(i)

    def deQueue(self):
      return self.items.popleft()

    def isEmpty(self):
      return len(self.items) == 0

    def size(self):
      return len(self.items)
class Stack:
    def __init__(self,list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
    def push(self,i):
        self.items.append(i)
    def pop(self):
        return self.items.pop()
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)
if __name__ == '__main__':
    q1 = Queue2()
    s1 = Stack()
    left1, right1 = input('Enter Input (Normal, Mirror) : ').split()
    right = list(right1)
    left = list(left1)
    boom = []
    ooqq =[]
    normal_num = 0
    boom_num = 0
    failin = 0
    for i in right:
        ooqq.insert(0,i)
    right = ooqq
    while(1):
        ch = 0
        for i in range(len(right)):
            # ch = 0
            if i > 0 and i < len(right)-1 and len(right) > 2:
                if right[i-1] == right[i] and right[i] == right[i+1]:
                    boom.append(right[i])
                    right.pop(i-1)
                    right.pop(i-1)
                    right.pop(i-1)
                    ch += 1
                    boom_num += 1
                    if len(right) == 0:
                        ch == 0
                        break
                    break
        if ch == 0:
            break
    ch = 0
    tpo = 0
    ooqq = []
    
    while(1):
        cnl = True
        ch = 0
        if len(boom) > 0:
            for i in range(len(left)):
                if tpo > 3:
                    cnl = True
                    tpo = 0
                if i > 0 and i < len(left)-1 and cnl == True:
                    if left[i-1] == left[i] and left[i] == left[i+1] and len(boom) > 0:
                        x = boom.pop(0)
                        left.insert(i+1,x)
                        ch += 1
                        failin += 1
                        if len(boom) == 0:
                            ch = 0
                            break
                        cnl = False
                        tpo = 0
                        # break
                if cnl == False:
                    tpo += 1
        if ch == 0:
            break
    while(len(left)>0):
        s1.push(left.pop(0))
    s = []
    while(not s1.isEmpty()):
        s.append(s1.pop())
    while(1):
        ch = 0
        for i in range(len(s)):
            # ch = 0
            if i > 0 and i < len(s)-1 and len(s) > 2:
                if s[i-1] == s[i] and s[i] == s[i+1]:
                    s.pop(i-1)
                    s.pop(i-1)
                    s.pop(i-1)
                    ch += 1
                    normal_num += 1
                    if len(s) == 0:
                        ch == 0
                        break
                    break
        if ch == 0:
            break
    testy =[]
    for i in boom:
        testy.insert(0,i)
    boom = testy
    print('NORMAL :')
    print(len(s))
    if len(s) == 0:
        print('Empty')
    else:
        realnor =''
        for i in s:
            realnor += i
        print(realnor)
    if normal_num - failin > 0 and failin > 0:
        print(normal_num - failin,'Explosive(s) ! ! ! (NORMAL)')
        print("Failed Interrupted",failin,"Bomb(s)")
    else:
        print(normal_num,'Explosive(s) ! ! ! (NORMAL)')
    print("------------MIRROR------------")
    print(": RORRIM")
    print(len(right))
    if len(right) == 0:
        print('ytpmE')
    else:
        realnor = []
        realnor1 = ''
        for i in right:
            realnor.insert(0,i)
        for w in realnor:
            realnor1 += w
        print(realnor1)
    print("(RORRIM) ! ! ! (s)evisolpxE",boom_num)
    
