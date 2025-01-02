"""find maximum element from the list
   input:l=[1,5,3,2,10]
   output: 10
"""
l=[1,5,3,2,10]
num=l[0] # Start with the first element as the maximum
for i in l:
    if i > num: # If current element is greater, update num
        num=i
print("maximum number :",num)