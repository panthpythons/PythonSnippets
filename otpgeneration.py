"""Importing the secrets Module
The secrets module is designed for generating cryptographically secure random numbers,
 making it ideal for applications like OTPs and tokens."""


import secrets

otp =''.join([str(secrets.randbelow(10)) for num in range(6)] )     

print(otp)