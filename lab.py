MovieName = "2049"
MovieRating = 3
MoviePoP = 72.65
if MovieRating >= 4 and MoviePoP > 80:
    print("Highly recommended")
elif MovieRating >= 3 and MoviePoP > 70:
    print("i recommend it, it's good")
elif MovieRating <= 2 and MoviePoP > 60:
    print("you should check it out")
else: 
    print("dont watch it , it's waste of time")
