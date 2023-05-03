name="khalid"
email="khalid@gmail.com"
com=email.endswith(".com")
aate=email.find("@")
noSpace=email.isspace()
if len(name)<2:
    print("the name length must be more than 2 characters, please provide a valid name ")
elif com ==False and aate ==-1  :
    print("your email is not valid")
elif  noSpace==True or ' ' in email:
    print(" the email is not valid , please provide a valid email ,there are space in email")
elif email[0].isdigit()==True:
    print(" the email is not valid , please provide a valid email , you cant start with number ")

elif email.endswith("@gmail.com")==-1:
    print("we only accept @gmail emails .")
else:

    print(f"welcome {name}, you registered with the email {email} !")