#Fibonacci series Between 0 to 50
a,b = 0,1
print(a,b,end=" ")
for i in range(7):
    c = a+b
    print(c,end = " ")
    a=b
    b=c
