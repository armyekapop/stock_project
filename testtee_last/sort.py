def bubblesort(inp):
    for i in range(len(inp)):
        for j in range(0,len(inp)-1-i):
            if inp[j+1]<inp[j]:
                inp[j],inp[j+1]=inp[j+1],inp[j]
def inserttion(inp):
    for i in range(1,len(inp)):
        keepindex=i
        while keepindex>0 and inp[keepindex]<inp[keepindex-1]:
            inp[keepindex],inp[keepindex-1]=inp[keepindex-1],inp[keepindex]
            keepindex-=1
def selection(inp):
    for i in range(len(inp)):
        valuemin=inp[i]
        minindex=i
        for j in range(i+1,len(inp)):
            if inp[j]<valuemin:
                valuemin=inp[j]
                minindex=j
        inp[i],inp[minindex]=inp[minindex],inp[i]     
inp=list(map(int,input('Enter Input : ').split()))
selection(inp)
print(inp)