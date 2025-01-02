"""print even and odd numbers from list
   input :[1,2,4,7,9,15]
   ouput :[2,4]
"""

l=[1,2,4,7,9,15]
even_list=[]
odd_list=[]
for i in l:
    if i %2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
print("Even numbers : ",even_list)
print("Odd numbers :", odd_list)