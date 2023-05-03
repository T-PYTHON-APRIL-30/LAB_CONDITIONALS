movie = "Random movie"
rating: int = 3
popularity: float = 72.65

if rating >= 4 and popularity > 80 :
    print ("highly recommended")
elif rating >= 3 and popularity > 70 :
    print ("I recommend it")
elif rating <= 2 and popularity > 60 :
    print ("you should check it out")
elif rating <= 2 and popularity < 50 :
    print ("Don't watch it. It's a waste of time")
else :
    print ("this kind of movie is out of my recommendation conditions")
