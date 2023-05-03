movie = "John wick"
movieRating = 3
moviePopularity = 72.65

if movieRating >= 4 and moviePopularity > 80:
    print (movie, " is highly recommended")
elif movieRating >= 3 and moviePopularity > 70:
    print ("i recommended it, its good")
elif movieRating <= 2 and moviePopularity > 60:
    print ("check it out")
else:
    print ("dont watch it, iys a waste of time")
