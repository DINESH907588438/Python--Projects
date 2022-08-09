#Displaying Common Words of the string
s1 = input("Enter the String-1: ")
s2 = input("Enter the String-2: ")
l1,l2 = list(s1.split(" ")),list(s2.split(" "))
print("The Common Words are: ")
for i in l1:
    if i in l2:
        print(i)
