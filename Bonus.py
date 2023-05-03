name = input("Your Name: ")
email = input("Your Email: ")

if email.find("@gmail.com") == -1 or email.find(" ") != -1:
    print("the email is not valid , please provide a valid email")
elif len(name) <= 2:
    print("the name length must be more than 2 characters, please provide a valid name.")
elif len(name) > 2 and email.find("@gmail.com") != -1:
    print(f"welcome {name}, you registered with the email {email} !")
else:
    print("something wrong!!")