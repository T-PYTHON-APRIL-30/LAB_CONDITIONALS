name = input("Enter your name: ")

email = input("Enter your email: ")

if len(name) >=3 and email.endswith("@gmail.com") and email.count(" ") == 0 and email.count("@") == 1:
    print(f"You are registerd with name:{name} and Email:{email}")

else:
    print("Your Name Or Email Is Not Valid!")