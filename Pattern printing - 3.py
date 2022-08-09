#Pattern printing-3
N = ord(input("Enter the last Alphabit of your pattern: "))
for i in range(65,N):
    print(chr(i)*(i-64))
