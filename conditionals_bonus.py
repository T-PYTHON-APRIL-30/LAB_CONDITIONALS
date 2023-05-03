print ("Welcome to our website")
print ("Please note that we only accept Gmail accounts")
print ("and your username should contain more than 2 letters")
username = (input("Your username: "))
E_mail = (input("Your Gmail account: "))
E_mail = E_mail.replace(" ","")
E_mail = E_mail.lower()

if len(username) > 2 and E_mail.endswith("@gmail.com") :
    print (f"Welcome {username}, you registered with the email {E_mail}")
elif len(username) <= 2 and E_mail.endswith("@gmail.com") :
    print("the name length must be more than 2 characters, please provide a valid name.")   
elif len(username) > 2 and E_mail.rfind("@gmail.com") :
    print (" the email is not valid , please provide a valid email .")
else :
    print ("please check for the conditions")