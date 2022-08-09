#Frequency of Each Vowel
S = list(input("Enter the String: "))
a = "aeiouAEIOU"
print("The Frequency of Each Vowel is : ")
l = list()
for i in S:
    if i in a:
        l.append((i,S.count(i)))
        S2 = set(l)
for k in S2:
    print(k)
