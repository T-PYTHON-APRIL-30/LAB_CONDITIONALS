from re import M

#Create a variable for the movie (choose any movie you like)
movie = "split"

#Create a variable of type int to hold the rating of the movie out of 5 . Give this movie 3
rating = 4

#Create a popularity score of type float , let it be 72.65
popularity_score  = 72.65


#Using an if statement
#Check if the movie rating is 4 or greater and the popularity is greater than 80 , print "Highly recommended"
if rating >= 4 and popularity_score > 80:
    print(f"\n{movie} is Highly recommended!\n")
    
#else if the movie rating is 3 or greater and the popularity is greater than 70 , print "I recommended it . It is good"
elif rating >=3 and popularity_score > 70:
    print(f"\n{movie} movie is recommended. It's a good movie\n")

#else if the movie rating is 2 or less and the popularity is greater than 60 , print "You should check it out!"
elif rating <= 2 and popularity_score > 60:
    print(f"\n{movie} movie is worth checking\n")

#else the movie rating is 2 or less and the popularity is less than 50 , print "Don't watch it. It is a waste of time"
else:
    print(f"\ndon't watch {movie} movie. It's a waste of time\n")
