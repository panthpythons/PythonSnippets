"""factorial of number
take input from user
   input: 5
   output: 120 """
num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Factorial:", factorial)
