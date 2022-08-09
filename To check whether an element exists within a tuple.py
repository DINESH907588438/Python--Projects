#To check whether an element exists within a tuple
n = int(input(("Enter the no of Elements in tuple: ")))
l = list()
print("Enter the tuple Elements: ")
for i in range(n):
    l.append(int(input("Enter the Element-{}: ".format(i+1))))
print("The tuple is",tuple(l))
N = int(input("Enter the Element to check: "))
if N in l:
    print("The Entered Element {} is in tuple".format(N))
else:
    print("The Entered Element {} is not in tuple".format(N))
        
        

