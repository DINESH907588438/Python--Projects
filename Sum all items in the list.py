#Sum all items in the list
n = int(input(("Enter the no of Elements in list: ")))
l = list()
print("Enter the Array Elements: ")
for i in range(n):
    l.append(int(input("Enter the Element-{}: ".format(i+1))))
print("The List is",l)
print("The sum of all items in the list is",sum(l))
