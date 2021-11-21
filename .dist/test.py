import random
def find_num(inp):
    ran = [random.randint(1,25) for _ in range(5)]
    print("random :",ran)
    near = abs(inp-ran[0])
    num = 1
    for i in range(5):
        if abs(inp-ran[i])<near:
            near = abs(inp-ran[i])
            num = i+1      
    print("output :",num)

x = int(input("input : "))
if x>0 and x<=25:
    find_num(x)
else:
    print("Error")