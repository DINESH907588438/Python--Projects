#Multiplication table
ans = 1
T = int(input("Enter any value for table: "))
for i in range(1,21):
    print("{} * {} = {}".format(i,T,i*T))
