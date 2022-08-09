#appending the square of each number to a new list
n = int(input(("Enter the no of Elements in list: ")))
l,m = list(),list()
print("Enter the Array Elements: ")
for i in range(n):
    l.append(int(input("Enter the Element-{}: ".format(i+1))))
print("The List is",l)
for i in l:
    m.append(i**2)
print("The square list is",m)    
