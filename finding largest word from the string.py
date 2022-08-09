#Finding largest word from the String
S = input("Enter the String: ")
L = list(S.split(" "))
k = list()
for i in L:
    k.append(len(i))
s1 =k.index(max(k))
print("The Largest word is",L[s1])
    
