roman = ["M","CM","D","CD","C", "XC", "L", "XL", "X", "IX","V", "IV", "I"]
dec = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
dic = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,}
class translator:
    def __init__(self):
        self.num = None
        self.s = ""

    def deciToRoman(self, num):
        i = 0
        romannum = ""
        while(num>0):
            k = int(num/dec[i])
            while(k>0):
                k = int(num/dec[i])
                romannum += roman[i]
                num -= dec[i]
                k -= 1
            i += 1
        return romannum
    def romanToDeci(self, s: str):
        total = 0
        for i in range(len(s)):
            value = dic[s[i]]
            if i+1 < len(s) and dic[s[i+1]] > value :
                total -= value
            else:
                total += value
        return total
        
if __name__ == '__main__':
    indec = translator()
    x = int(input("test : "))
    print(indec.deciToRoman(x))
    print(indec.romanToDeci(indec.deciToRoman(x)))