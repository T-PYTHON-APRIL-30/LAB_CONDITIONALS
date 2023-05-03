Name = input('Please enter your name: ')

Email = input('Please enter your email: ')

if len(Name) > 2:

    if Email.find("@gmail.com") != -1:
     
        print(f'Welcome {Name}, you registered with the email {Email}!')

    else:
        print('the email is not valid , please provide a valid email!!')
else:
    print('Your name length must be more than 2 characters, please provide a valid name!!')