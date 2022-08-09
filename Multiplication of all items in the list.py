#Multiplication of all items in the list
n = int(input(("Enter the no of Elements in list: ")))
l,m = list(),1
print("Enter the Array Elements: ")
for i in range(n):
    l.append(int(input("Enter the Element-{}: ".format(i+1))))
print("The List is",l)
for i in l:
    m*=i
print("The Multiplication of all items in the list is ",m)    

