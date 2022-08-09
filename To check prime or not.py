#To check the number is Prime or not
N = int(input("Enter the number to Check: "))
for i in range(2,N):
    if N%i == 0:
        print("The Given number {} is Not prime".format(N))
        break
    else:
        print("The Given number {} is prime".format(N))
        break
        
