name = input("Please enter your name: ")
print(name)
email = input("Please enter your email: ")
print(email)
namelen = len(name)
if namelen > 2:
    if email.endswith("gmail.com") and email.count("  ") == 0 and email.count("@") == 1:
        print(f"Welcome",(name))
    else:
        print("please enter a valid email")

else:
    print("olease enter name greater than 2 charater")
