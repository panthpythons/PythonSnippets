"""Remove empty tuple by using list Comprehension
 input:t1=[(),(),("abc",1,2),3,4,()]
 output:[("abc",1,2),3,4]"""

t1=[(),(),("abc",1,2),3,4,()]
t2=[i for i in t1 if i] #The condition if i keeps only elements that are not empty (non-falsy values).
print("Remove empty tuple:",t2)