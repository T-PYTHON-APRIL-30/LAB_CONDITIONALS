name = input("Your Name: ")
email = input("Your Email: ")

if not email.endswith("@gmail.com") or email.find(" ") != -1 or email.count("@") == 1:
    print("the email is not valid , please provide a valid email")
elif len(name) <= 2:
    print("the name length must be more than 2 characters, please provide a valid name.")
elif len(name) > 2 and email.endswith("@gmail.com"):
    print(f"welcome {name}, you registered with the email {email} !")
else:
    print("something wrong!!")