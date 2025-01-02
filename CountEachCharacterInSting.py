"""How to count the each character in sting
   input: str="python"
   output={'p':1,'y':1,'t':1,'h':1,'o':1,'n':1}"""

s = "panthpythons"
d = {}
for i in s:
    if i not in d:
        d[i] = 1  # Add the character as key with its value as the character itself
    else:
        d[i] += 1  # Append the character to the value if it exists already
print(d)