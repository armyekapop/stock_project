def FindCharacter(data):
    a = list(data)
    for i in a:
        if i >= 'a' and i <= 'z' :
            return i
def FindSequenChar(data):
    lis = []
    for item in data :
        lis.append([FindCharacter(item),item])
    for i in range(len(lis)-1):
        for j in range(len(lis)-i-1): 
            if lis[j][0] > lis[j+1][0] : 
                lis[j], lis[j+1] = lis[j+1], lis[j] 
    return lis
   


data = input('Enter Input : ').split(' ')
dataOfResult = FindSequenChar(data)
for i in dataOfResult:
    print(i[1],end=' ')