Username = input("Hello please enter you name: ")


if len(Username) > 2:
    
    emailN = input("Enter your email please :) ")

    if emailN.find("@Gmail.com") != -1:
        print(f"welcome {Username} , you registerred with the email {emailN} !")
    else:
        print("worng email, pleae provide valid email")

else:
    print("provide a name with a length of more than two characters")
        

        