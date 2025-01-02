l=[10,20,30,40,10,20,20,40]
l2=[] # to add unique elements
for i in l:
    if i not in l2:
        l2.append(i) #append() method is used to add elements to end of the list
print(l2)

"""Reversing Words in a Sentence"""
str="It looks like you're asking about lists in Python! A list is a built-in data structure in Python that allows you to store multiple items in a single variable. Lists are mutable, meaning their content can be changed after they are created"

split_str=str.split(" ")
l=[]
for i in split_str:
    l.append(i[::-1])
res=" ".join(l)
print(res)
