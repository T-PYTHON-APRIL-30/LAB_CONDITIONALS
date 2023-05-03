"""
write a program that asks the user to provide his name and his email using input , then do the following:
Check that the name length is more than 2 characters.
Check that the email is valid (using string operations and coditionals)
You only accept @gmail emails .
if the email is valid, display a welcome message to the user . for example :
welcome Ahmed, you registered with the email ahmed@gmail.com !

if the email or name is not valid, display the message :
 the email is not valid , please provide a valid email .
or

the name length must be more than 2 characters, please provide a valid name.

"""

import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

def isValid(email):
    if re.fullmatch(regex, email):
      return True
    else:
      return False

name = input("Please enter your name: ")
email = input("Please enter your email: ")

if len(name) > 2:
    print("The name length must be more than 2 characters, please provide a valid name.")
elif isValid:
    print("The email is not valid, please provide a valid email.")
#elif email.isspace or email.startswith(0,1,2,3,4,5,6,7,8,9):
#    print("The email is not valid, please provide a valid email.")
else:
    print(f"Welcome {name}, you registered with the email {email}!")

