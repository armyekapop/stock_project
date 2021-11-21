print(" *** Divisible number ***")
inp = int(input("Enter a positive number : "))
outp = []
strr = ""
if inp == 0:
    print("0 is OUT of range !!!")
else:
    for i in range(inp+1):
        if i == 0:
            continue
        else:
            if inp%i == 0:
                outp.append(i)

    for x in range(len(outp)):
        if x == 0:
            strr += str(outp[x])
        else:
            strr += ' '+str(outp[x])
    print('Output ==>',strr)
    print('Total ==>',len(outp))