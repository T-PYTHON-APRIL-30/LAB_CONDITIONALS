print("Welcome to movie recommendations")
print()

movieName : str = "CREED 3"
movieRate : int = 3
popularity : float = 72.65

if movieRate <= 5 and popularity <= 100.0 : # movieRate out of 5 , popularity out of 100

    if  movieRate >= 4 or popularity > 80.0 :
        print(f"{movieName} is highly recommended.")
    elif movieRate >= 3 or popularity > 70.0 :
        print(f"I recommend {movieName}. It is good.")
    elif movieRate >= 2 or popularity > 60.0 :
        print(f"You should check {movieName} out!")
    else:
        print("Don't watch it. It is a waste of time.")

else:
    print("There's somethig error !")