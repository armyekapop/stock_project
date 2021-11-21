inp = input("Enter number end with (-1) : ").split()
inp = [int(i) for i in inp]
check = []
if -1 not in inp:
    print("Invalid INPUT !!!")
else:
    if len(inp) == -1 and inp[0] == -1:
        print("Not found")
    else:
        for i in inp:
            if i == -1:
                break
            if i not in check:
                check.append(i)
        