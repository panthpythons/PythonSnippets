"""How to Reverse a number in Python
take number from user
input : number = 1234
output :4321"""
num = int(input("Enter a number: "))
reversed_num = 0

while num != 0:
    digit = num % 10  # Get the last digit
    reversed_num = reversed_num * 10 + digit  # Add it to the reversed number
    num //= 10  # Remove the last digit from num

print("Reversed number:", reversed_num)