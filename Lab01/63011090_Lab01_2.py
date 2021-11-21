print(" *** Wind classification ***")
x = float(input("Enter wind speed (km/h) : "))
if 0<x<=51.99:
    print("Wind classification is Breeze.")
if 52.00<=x<=55.99:
    print("Wind classification is Depression.")
if 56.00<=x<=101.99:
    print("Wind classification is Tropical Storm.")
if 102.00<=x<=208.99:
    print("Wind classification is Typhoon.")
if 209.00<=x:
    print("Wind classification is Super Typhoon.")