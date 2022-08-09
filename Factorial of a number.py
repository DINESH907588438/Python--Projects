#Factorial of a number
ans = 1
n = int(input("Enter the number to find Factorial: "))
for i in range(1,n+1):
    ans *= i
print("The Factorial of {} is {}".format(n,ans))
              
