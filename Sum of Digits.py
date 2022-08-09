#Sum of Digits
n = int(input("Enter the number: "))
sum = 0
while n > 0:
    remainder = n % 10
    sum+=remainder
    n = n // 10
print("The Sum digits: ",sum)    
