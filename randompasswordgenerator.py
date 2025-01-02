"""
random: Provides functions to generate random choices, useful for password generation.
string: Contains pre-defined character sets like letters, digits, and punctuation.
"""


import random
import string

password_length = 8

chars = string.ascii_letters+string.digits+string.punctuation

password = ''.join(random.choices(chars,k=password_length))

print(password)