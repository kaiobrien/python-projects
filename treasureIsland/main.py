print("Welcome to Treasure Island. Your mission is to find the treasure.")
choice1 = input("You've reached a fork in the road. Will you go left or right?\n").lower()
if choice1 == "left":
    choice2 = input("You've reached a dark lake. Will you swim across it or wait for a boat to bring you across?\n").lower()
    if choice2 == "wait":
        choice3 = input("After crossing the lake and entering the forest you notice trees with different coloured doors,"
                        "do you choose to open the blue, red, or yellow door?\n").lower()
        if choice3 == "yellow":
            print("You won the game")
        else:
            print("Game over")
    else:
        print("Game over")
else:
    print("Game Over")


