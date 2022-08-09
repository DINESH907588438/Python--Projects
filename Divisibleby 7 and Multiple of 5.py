#Divisible by 7 and Multiple of 5
l = list()
for i in range(1500,2701):
    if i%7 == 0 and i%5 == 0:
        l.append(i)
print("Numbers Divisble by 7 and Multiple of 5 in the range of 1500 to 2700 : ")        
print(l)        
