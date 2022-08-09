#Temperature Conversion
C = int(input("Enter the Celcius value: "))
F = (C+1.8)*32
C = (F/32)-1.8
print("Fahrenheit({} Celcius) = {}".format(C,F))
print("Celcius({} Fahrenheit) = {}".format(F,C))
