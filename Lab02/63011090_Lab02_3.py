def odd_even(typ, inp , opt):
    if typ == 'S':
        x = ""
        num = len(inp)
    if typ == 'L':
        x = []
        r_arr = list(inp.split(" "))
        num = len(r_arr)
    for i in range(num):
        if i%2 == 1 and opt == 'Even'and typ == 'S':
            x += inp[i]
        if i%2 == 0 and opt == 'Odd'and typ == 'S':
            x += inp[i]
        if i%2 == 1 and opt == 'Even'and typ == 'L':
            x.append(r_arr[i])
        if i%2 == 0 and opt == 'Odd' and typ == 'L':
            x.append(r_arr[i])
    return x
print("*** Odd Even ***")
typ, inp, opt = input("Enter Input : ").split(",")
print(odd_even(typ, inp, opt))