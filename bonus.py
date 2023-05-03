validLogin = True

userName= input ("enter your name: ")
email= input ("enter you email: ")


if len(userName) < 3:
    validLogin = False
elif "@gmail.com" not in email or " " in email:
    validLogin = False

if validLogin == True:
    print("welcome {}, you registered with the email {} !".format(userName,email))
else:
    print("the email is not valid , please provide a valid email")