"""decorator in Python
  decorator is a function that takes another function as input and extends or modifies 
  its behavior without changing its actual code
  while calling decorator function we use @decorator method"""

#add two number using decorator function
def my_decorator(func):
    def sum_of_numbers(a,b):
        res=func(a,b)
        return res
    return sum_of_numbers

@my_decorator
def add(a,b):
    return a+b
print(add(10,20))
