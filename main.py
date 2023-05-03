movie = "spider man no way home"
rate_movie = 3
popularity_score = 72.65

if rate_movie >= 4 and popularity_score > 80:
    print("Highly recommended")
elif rate_movie >= 3 and popularity_score > 70:
    print("I recommended it . It is good")
elif rate_movie <= 2 and popularity_score > 60:
    print("You should check it out!")
else:
    print("Don't watch it. It is a waste of time")