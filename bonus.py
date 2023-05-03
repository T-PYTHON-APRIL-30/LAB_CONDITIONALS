'''
A program that asks the user to provide his name and his email using input , then do the following:
Check that the name length is more than 2 characters.
Check that the email is valid (using string operations and coditionals)
You only accept @gmail emails .
if the email is valid, display a welcome message to the user . for example :
'''

from operator import contains


name = input("Enter your name: ")
if(len(name)<2):
    print("Invalid name, try again")
else:
    email = input("Type your Email: ")



