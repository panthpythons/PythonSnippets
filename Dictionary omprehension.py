"""Swap key-values from dictionary by using dictionary Comprehension
 input : d={"abc":1,"number":2,"name":"python"}
outpur:	{1:"abc",2:"number","python":"name"}"""

d={"abc":1,"number":2,"name":"python"}
d1 ={ values:keys for keys,values in d.items()} #It  will swap each key-value pair in the dictionary d
print("Swap key-values from dictionary:",d1)
