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
if __name__ == '__main__':
    S = Queue2()
    book, func = input('Enter Input : ').split('/')
    list1 = book.split()
    list2 = func.split(",")
    for i in list1:
        S.enQueue(i)
    for i in list2:
        H = list(i.split())
        if H[0] == 'E':
            S.enQueue((H[1]))
        if H[0] == 'D':
            S.deQueue()
    outp = set()
    dup = False
    while(not S.isEmpty()):
      x = S.deQueue()
      if (x in outp):
        dup = True
        break
      else:
        outp.add(x)
    if dup == False:
      print("NO Duplicate")
    else:
      print("Duplicate")