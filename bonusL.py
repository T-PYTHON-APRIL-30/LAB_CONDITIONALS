Username = input("Hello please enter you name: ")
emailN = input("Enter your email please :) ")

if len(Username) < 2:
    if emailN.find('@gmail.com') > -1:
        print(f'Welcome {Username}, you registered with the email {emailN}!')
        if emailN.find('@gmail.com') <= -1:
         print('the email is not valid , please provide a valid email!')
else:
    print('length of the name must be more than 2 char, please provide a name')
        