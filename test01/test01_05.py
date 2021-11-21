roman = ["M","CM","D","CD","C", "XC", "L", "XL", "X", "IX","V", "IV", "I"]
dec = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
dic = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,}
class MyInt:
    def __init__(self,num):
        self.num = num
    def toRoman(self):
        i = 0
        romannum = ""
        while(self.num>0):
            k = int(self.num/dec[i])
            while(k>0):
                k = int(self.num/dec[i])
                romannum += roman[i]
                self.num -= dec[i]
                k -= 1
            i += 1
        return romannum
    
    
if __name__ == '__main__':
    print(" *** class MyInt ***")
    numA,numB = input("Enter 2 number : ").split()
    a = MyInt(int(numA))
    b = MyInt(int(numB))
    print(numA,"convert to Roman :",a.toRoman())
    print(numB,"convert to Roman :",b.toRoman())
    
    print(a)