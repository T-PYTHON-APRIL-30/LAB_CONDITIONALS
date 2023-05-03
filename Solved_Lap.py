#variable for the movie
movie_name = 'Titanc'

#variable for the rating
rat = int(3)

#popularity score
pop_score = float(72.65)

if rat >=4 and pop_score > 80:
    print('Highly recommended')

elif rat >=3 and pop_score >70:
    print('I recommended it. It is good')

elif rat <=2 and pop_score >60:
    print('You should check it out')

else:
    print("Don't watch it. It is a waste of time")