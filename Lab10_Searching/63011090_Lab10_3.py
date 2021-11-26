class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)


class hash:
    pass
    # Code Here


def get_next_index(lst, value, n, max_try):
    arr = [0]*(n+1)
    try_ = 0
    arr[0] = value
    # for x in lst:
    #    print(x)
    print("collision number {} at {}".format(try_+1, arr[0]))
    while try_ < max_try-1:
        try_ += 1
        arr[try_] = (arr[try_-1] + try_*2-1) % n
        #print("debug", arr[try_])
        # print("{} = ({} + {}) % {}".format(arr[try_],arr[try_-1],try_*try_ ,n))
        if lst[arr[try_]] == None:
            return arr[try_]
        else:
            print("collision number {} at {}".format(try_+1, arr[try_]))

    # print(arr)
    return -1

# F(i) = F(i-1) + 2*i - 1


size, inp = input(" ***** Fun with hashing *****\nEnter Input : ").split('/')
size = size.split()
sizeTable = int(size[0])
maxColis = int(size[1])
# print(sizeTable, maxColis)
currentSize = 0
arr = [None]*sizeTable
inp = inp.split(',')

for i in inp:
    if currentSize != sizeTable:
        a, b = i.split()
        sum = 0
        for j in a:
            sum += ord(j)

        # print(sum)
        n = sum % sizeTable
        # print(n)
        if arr[n] == None:
            arr[n] = Data(a, b)
            currentSize += 1

        else:
            index = get_next_index(arr, n, sizeTable, maxColis)
            if index != -1:
                arr[index] = Data(a, b)
                currentSize += 1
            else:
                print("Max of collisionChain")

        for k in range(0, len(arr)):
            print("#"+str(k+1), end="      ")
            print(arr[k])
        print("---------------------------")
    else:
        print("This table is full !!!!!!")
        break