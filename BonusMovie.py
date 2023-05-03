'''write a program that asks the user to provide his name and his email using input , then do the following:
Check that the name length is more than 2 characters.
Check that the email is valid (using string operations and coditionals)
You only accept @gmail emails .
if the email is valid, display a welcome message to the user . for example :
welcome Ahmed, you registered with the email ahmed@gmail.com !

if the email or name is not valid, display the message :
 the email is not valid , please provide a valid email .
or

the name length must be more than 2 characters, please provide a valid name.'''
#write a program that asks the user to provide his name and his email using input , then do the following:
print("welcome to log in programe")
name= input("please give me your name")
email=input("please give me your email")
#Check that the name length is more than 2 characters.
namelength = len(name)
if namelength>2 and  email.endswith("@gmail.com"):
    #Check that the email is valid (using string operations and coditionals)
   print("welcome", name, "you registered with the email", email, "!")
elif namelength<2 or email.endswith("@gmail.com"): 
    print(" the email is not valid , please provide a valid email .")


