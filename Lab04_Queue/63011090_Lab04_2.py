from collections import deque
class Queue2:    # use deque 
    def __init__(self, q = None):
      if q == None:
        self.items = deque()
      else:
        self.items = deque(q,len(q))
    def __str__(self):
        s = ''
        for i in range(len(self.items)):
            if(i != len(self.items)-1):
                s += "'"+str(self.items[i])+"'"+","+" "
            else:
                s += "'"+str(self.items[i])+"'"
        return "["+s+"]"
    def enQueue(self, i):
      self.items.append(i)

    def deQueue(self):
      return self.items.popleft()

    def isEmpty(self):
      return len(self.items) == 0

    def size(self):
      return len(self.items)
if __name__ == '__main__':
    cust = Queue2()
    c1 = Queue2()
    c2 = Queue2()
    inp = input('Enter people : ')
    for i in inp:
        cust.enQueue(i)
    i = 1
    ic1 = 0
    ic2 = 0
    while(not cust.isEmpty()):
        if ic1 % 3 == 0 and not c1.isEmpty():
            c1.deQueue()
            ic1 = 0
        if ic2 % 2 == 0 and not c2.isEmpty():
            c2.deQueue()
            ic2 = 0
        if c1.size()<5:
            c1.enQueue(cust.deQueue())
        elif c2.size()<5 and c1.size() == 5:
            c2.enQueue(cust.deQueue())
        if(not c2.isEmpty()):
            ic2 += 1
        if(not c1.isEmpty()):
            ic1 += 1
        print(i,cust.__str__(),c1.__str__(),c2.__str__())
        i += 1
