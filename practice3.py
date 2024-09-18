#Text-Based Adventure game

answer = input("do you want to play this game? [Yes/No]:")

if answer == "Yes":
    print("Welcome to the game❗")
    answer = input ("Do you want to go jungle or cave? [jungle/cave]:")
    if answer == "jungle":
        print("You see the hungry tiger🐯 Tiger will eat you.")
    elif answer == "cave":
        print("you see the bear🐻in font of the cave")
        answer = input("do you want to fight with the bear🐻or run away🏃‍♂️ [fight🦾/ runaway🏃‍♂️]:")
        if answer == "fight":
            print("bear🐻 is too much strong🦾❗ you loss the game")
        else:
            print("WOW! still you are alive❗")


else:
    print("The Game closed")