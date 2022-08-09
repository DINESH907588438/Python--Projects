#To check the character is Vowel or not
c = input("Enter the Character: ")
s = "aeiouAEIOU"
if c in s:
    print("The Entered Character '{}' is Vowel".format(c))
else:
    print("The Entered Character '{}' is Consonant".format(c))
