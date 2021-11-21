print("*** String Rotation ***")
str1, str2 = input("Enter 2 strings : ").split()
real = str1+' '+str2
outp = []
re_str1=''
re_str2=''
re_str1 = str1[-2]+str1[-1]
re_str2 = str2[0]+str2[1]+str2[2]
str1 = re_str1+str1[:len(str1)-2]
str2 = str2[3:]+re_str2
outp.append(str1+' '+str2)
while 1:
    re_str1=''
    re_str2=''
    re_str1 = str1[-2]+str1[-1]
    re_str2 = str2[0]+str2[1]+str2[2]
    str1 = re_str1+str1[:len(str1)-2]
    str2 = str2[3:]+re_str2
    outp.append(str1+' '+str2)
    if str1+' '+str2 == real:
        break
if len(outp) <= 5:
    num = 1
    for i in range(len(outp)):
        print(num,outp[i])
        num += 1
    print("Total of ",len(outp),'rounds.')
else:
    num = 1
    for i in range(5):
        print(num,outp[i])
        num += 1
    print(" . . . . . ")
    print(len(outp),outp[-1])
    print("Total of ",len(outp),'rounds.')

