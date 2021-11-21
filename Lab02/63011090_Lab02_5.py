class game():
    def __init__(self) -> None:
        pass
    def TorKham(self,list_inp):
        r_arr = list(list_inp.split(","))
        list_check = []
        list_real = []
        ex = False
        i = 0
        while(ex == False):
            if " " not in r_arr[i]:
                if r_arr[i] == 'X':
                    ex = True
                if r_arr[i] == 'R':
                    del list_real[0:i+1]
                    del list_check[0:i+1]
                    del r_arr[0:i+1]
                    i = -1
                    print("game restarted")
            else:
                recc = r_arr[i].split(" ")
                opt = recc[0]
                wait = str(recc[1]).lower()
                if opt == 'P'and i == 0:
                    list_check.append(wait)
                    list_real.append(recc[1])
                    print("'"+str(recc[1])+"'"+" ->",list_real)
                if opt == 'P'and i > 0 :
                    c1 = str(list_check[i-1]).lower()
                    c2 = str(recc[1]).lower()
                    if c2[0]+c2[1]==c1[-2]+c1[-1] and wait not in list_check:
                        list_check.append(wait)
                        list_real.append(recc[1])
                        print("'"+str(recc[1])+"'"+" ->",list_real)
                    else:
                        ex = True
                        r = str(recc[1])
                        print("'"+r+"'"+" -> game over")
                if opt != 'P':
                    r = str(opt)+" "+str(wait)
                    print("'"+r+"' is Invalid Input !!!")
                    ex = True
            i += 1

            if i>len(r_arr)-1:
                ex = True

print("*** TorKham HanSaa ***")
list_inp = input("Enter Input : ")
r1 = game()
r1.TorKham(list_inp)
