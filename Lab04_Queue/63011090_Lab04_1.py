from collections import deque
class Queue2:    # use deque 
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
    inp = input('Enter Input : ').split(',')
    for i in inp:
        H = list(i.split())
        if H[0] == 'E':
            S.enQueue((H[1]))
            print("Add",H[1],"index is",S.size()-1)
        if H[0] == 'D':
            if S.isEmpty():
                print(-1)
            else:
                deq = S.deQueue()
                print("Pop",deq,"size in queue is",S.size())
    if(S.size() > 0):
        qq =[]
        while(not S.isEmpty()):
            qq.append(S.deQueue())
        print("Number in Queue is : ",qq)
    else:
        print("Empty")