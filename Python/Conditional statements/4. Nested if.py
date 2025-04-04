weather=input("Enter the weather?\n")
time_of_day=(input("Enter the time_of_day?\n"))
if weather=="sunny":
    if time_of_day=="day":
        print("Hurray!, Let's go for Swimmimg.")
    else:
        print("oops! It's time to sleep.")
elif weather=="winter":
    if time_of_day=="day":
        print("Let's play Badminton.")
    else:
        print("Let's watch a Movie.")
elif weather=="rainy":
    print("you should play Indoor games.")
else:
    print("You better stay inside, prepare a Better Dish and Enjoy your Day.")