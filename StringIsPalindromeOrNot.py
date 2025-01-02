"""Give string is palindrome or Not?
take string from user
inputstring::madam
outpu : is palindrome """

str1=input("Enter the string : ")
empy_string=""
for i in str1:
    empy_string=i+empy_string
if str1==empy_string:
    print("Palindrome")
else:
    print("Not a palindrome")