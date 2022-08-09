#Median among three Numbers
A = int(input("Enter the number-1: "))
B = int(input("Enter the number-2: "))
C = int(input("Enter the number-3: "))
l = list()
l.extend([A,B,C])
l.remove(max(l))
l.remove(min(l))
print("The Median among the Entered numbers is: ",)
for i in l:
    print(i)
