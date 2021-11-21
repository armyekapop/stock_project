def staircase(row,i):
    if row > 0:
        stre = "_"*(row-1)+'#'*(i+1)
        if row-1 <= 0:
            return stre
        else:
            return  stre+'\n'+str(staircase(row-1,i+1) )
    elif row < 0:
        row = row
        stre = "_"*(i)+'#'*abs(row)
        if abs(row)-1 <= 0:
            return stre
        else:
            return  stre+'\n'+str(staircase(row+1,i+1) )
    elif row == 0:
        return 'Not Draw!'


print(staircase(int(input("Enter Input : ")),0))