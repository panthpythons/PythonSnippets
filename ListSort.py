"""  s1=i+s1 This line is the core of the reversal process. For each character i in s, it updates s1 by adding i to the front of s1. By placing i before s1, each new character from s is added at the beginning of s1, reversing the character order as the loop progresses."""

""" sort the given list without sort method
   input:l=[1,5,3,2,10]
   output: [1,2,3,5,10]"""

l = [1, 5, 3, 2, 10]
for i in range(len(l) - 1):
    for j in range(len(l) - 1 - i):  # Reduce range to avoid index out of bounds
        if l[j] > l[j + 1]:
            l[j], l[j + 1] = l[j + 1], l[j]
print("sorted lis :",l)