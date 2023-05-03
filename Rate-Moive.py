#recommend a movie to a friend based on the rating and popularity

print("Welcome to moive theater")
print("enjoy SAW moive ")
rate=int(input(("Enter your rate:")))
popularity=float(input("Enter your popularity "))


if rate >= 4 and popularity >=80 :
    print("Highly recommended")
elif rate >= 3 and popularity >=70 :
    print("I recommended it . It is good")
elif rate >= 2 and popularity >=60 :
    print("You should check it out!")  
else:
    print("Don't watch it. It is a waste of time")