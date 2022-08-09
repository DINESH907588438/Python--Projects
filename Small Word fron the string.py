#Finding the Small word from String
S =input("Enter the String: ")
S1 = list(S.split(" "))
l = list()
print("The small word is : ")
for i in S1:
    l.append(len(i))
k = l.index(min(l))
print(S1[k])
