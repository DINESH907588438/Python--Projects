#Finding how many integers divisble by the Entered number
n = int(input("How many integers do you have? "))
k = int(input("Enter the K value: "))
l,t = list(),list()
for i in range(n):
    l.append(int(input("Enter the Element-{}: ".format(i+1))))
for i in l:
    if i%k == 0:
        t.append(i)
print("The given numbers Divisible by '{}' are :".format(k))        
for i in t:
    print(i)
    

        
