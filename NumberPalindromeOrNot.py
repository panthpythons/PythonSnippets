"""Give number palindrome or Not?
take number from user
input number =121
output = is palindrome"""

num = int(input("Enter a number: "))
original_num = num  # Store the original number
reversed_num = 0

# Reverse the number
while num != 0:
    digit = num % 10  # Get the last digit
    reversed_num = reversed_num * 10 + digit  # Build the reversed number
    num //= 10  # Remove the last digit

# Check if the original number and the reversed number are the same
if original_num == reversed_num:
    print("Given nuumber is Palindrome")
else:
    print("Not a palindrome")
