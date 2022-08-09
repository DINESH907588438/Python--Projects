#Unique Words From the String
def unique(s):
    print("The Unique Words are :")
    for i in s:
        print(i)
s1 = input("Enter the string: ")
unique(set(s1.split(" ")))
         
