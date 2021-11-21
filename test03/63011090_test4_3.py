
def gcd(a,b):
    if b == 0:
        return abs(a)
    else:
        return gcd(b,a%b)

a,b = input("Enter Input : ").split()
a = int(a)
b = int(b)
if a == 0 and b== 0:
    print("Error! must be not all zero.")
else:
    if a == 0 and a>b:
        print("The gcd of",a,"and",b,"is :",gcd(a,b))
    elif abs(a) >= abs(b):
        print("The gcd of",a,"and",b,"is :",gcd(a,b))
    else:
        print("The gcd of",b,"and",a,"is :",gcd(a,b))