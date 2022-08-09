#Dispalyng Ascii Value of Each Character
S = input("Enter the String: ")
l = dict()
for i in S:
    l[i]=ord(i)
print(l)
