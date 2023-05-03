# LAB_CONDITIONALS
movie = "Frozen"
rating = int(3)
popularity = float(72.65)

if rating >= 4 and popularity > 80:
    print("Highly recommended")
elif rating >= 3 and popularity > 70:
    print("I recommended it . It is good")
elif rating <= 2 and popularity > 60:
    print("You should check it out!")
elif rating <= 2 and popularity < 50:
    print("Don't watch it. It is a waste of time")


# Bonus
# write a program that asks the user to provide his name and his email using input , then do the following:
Name = input("Please Enter Your Name(more than 2 letters): ")
Email = input("Please Enter Your Email(@gmail.com)only: ")
letterCount = Name.__len__()
spaces = Email.replace(" ", "")

if letterCount < 3:
    print("the name length must be more than 2 characters, please provide a valid name.")
if spaces.endswith("@gmail.com") == False:
    print("the email is not valid , please provide a valid email.")
else:
    print(f"welcome {Name}, you registered with the email {spaces}")
