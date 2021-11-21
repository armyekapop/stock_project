print("*** Reading E-Book ***")
TXT,HL = input("Text , Highlight : ").split(",")
x = TXT.replace(HL,"["+HL+"]")
print(x)