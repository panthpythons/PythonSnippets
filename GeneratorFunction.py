""" generator function"""
""" At lest one yield keyword is there we consider as generator function .its use for Memory Usage,
while time of calling generator function we use next() method.
if we not use next()  method its print generator object."""
def generator_fun(a, b):
    yield a * b  # The result of a multiplied by b is yielded

# Create a generator object by calling the generator function
mult = generator_fun(10, 20)

# Use next() to get the next value from the generator
print(next(mult))  # This will print 200, as 10 * 20 is 200
