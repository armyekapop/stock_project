class Hash:
    def __init__(self, max_size, max_col, threshold):
        self.max_size = max_size
        self.max_col = max_col
        self.threshold = threshold
        self.table = [None] * max_size
        self.current_size = 0
        self.copy_table = []

    def expand(self, x=None):
        self.table = []
        self.current_size = 0
        prime = findPrime(self.max_size * 2)
        addition_table = [None] * (prime)
        self.table = addition_table
        self.max_size = len(self.table)
        for item in self.copy_table:
            self.add(item)
        if x:
            self.add(x)

    def __str__(self):
        ss = ""
        for i in range(1, self.max_size+1):
            ss += f"#{i}	{self.table[i-1]}\n"
        return ss[:-1]

    def checkThreshold(self):
        percent = (self.current_size / self.max_size) * 100
        if percent >= self.threshold:
            print("****** Data over threshold - Rehash !!! ******")
            self.expand()

    def add(self, x):
        t = self.table
        indx = x % self.max_size
        if t[indx] == None:
            t[indx] = x
            self.current_size += 1
            self.checkThreshold()
            return
        i = 0
        cl = 1
        while (indx + pow(i, 2)) % self.max_size <= self.max_size:
            hx = (indx + pow(i, 2)) % self.max_size
            if t[hx] == None:
                t[hx] = x
                self.current_size += 1
                self.checkThreshold()
                return
            if cl >= self.max_col:
                print(f"collision number {cl} at {hx}")
                print("****** Max collision - Rehash !!! ******")
                self.expand()
                return
            print(f"collision number {cl} at {hx}")
            i += 1
            cl += 1


def findPrime(num, i=2):
    if num > 1:
        if num % i == 0:
            return findPrime(num+1, i+1)
        else:
            return num


print(" ***** Rehashing *****")
inp = input("Enter Input : ").split("/")
max_size, max_col, threshold = list(map(int, inp[0].split()))
items = list(map(int, inp[1].split()))
print("Initial Table :")
H = Hash(max_size, max_col, threshold)
print(H)
print("----------------------------------------")
for item in items:
    H.copy_table.append(item)
    print("Add :", item)
    H.add(item)
    print(H)
    print("----------------------------------------")