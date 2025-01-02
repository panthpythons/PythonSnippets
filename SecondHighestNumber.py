""" Find the second highest number from given list"""

l=[333,666,222,111,555,777,999]
for i in range(len(l)):
    for j in range(len(l)-1):
        if l[j]>l[j+1]:
            l[j],l[j+1] = l[j+1],l[j]
print(l[-2])