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
    def insertt(self, i):
      if len(self.items) == 0:
        self.items.append(i)
      else:
        x = i.split()
        ch = 0
        for el in self.items:
          y = el.split()
          if y[0] != x[0]:
            ch += 1
          else:
            qin = self.items.index(el)
            for elin in self.items:
              q = elin.split()
              if q[0] == x[0]:
                qin += 1
            self.items.insert(qin,i)
            ch = 0
            break
        if ch != 0:
          self.items.append(i)
    def size(self):
      return len(self.items)
if __name__ == '__main__':
    S1 = Queue2()
    left, right = input('Enter Input : ').split('/')
    peo = left.split(',')
    func = right.split(',')
    dic = {}
    for w in peo:
      g = w.split()
      dic[g[1]] = g[0]
    for i in func:
      H = i.split()
      if H[0] == 'E':
        wDict = dic[H[1]]+" "+H[1]
        S1.insertt(wDict)
      if H[0] == 'D':
        if not S1.isEmpty():
          x = S1.deQueue()
          qq = x.split()
          print(qq[1])
        else:
          print("Empty")
      
