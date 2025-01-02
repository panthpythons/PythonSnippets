"""find minimun element from the list
   input:l=[1,5,3,2,10]
   output: 10
"""
l=[1,5,3,2,10]
num=l[0] # Start with the first element as the minimum
for i in l:
    if i < num: # If current element is lessthan, update num
        num=i
print("minimum number :",num)
