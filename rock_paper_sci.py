import numpy as np
# Rock, Papers, scissors


def rps_game():


    options = ["rock", "paper", "scissors"]
    user_wins = 0
    comp_wins = 0
    draw = 0

    # ask = np.random.randint(1,4)

    while True:
        user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
        if user_input == "q":
            break

        if user_input not in options:
            print("type: rock,paper or scissors: ")
            continue

        roll = np.random.randint(1, 4)
        comp_input = options[roll - 1]

        # 3 condition to check the game
        if user_input == "rock" and comp_input == "paper":
            print("You WON!!!")
            user_wins += 1

        elif user_input == "paper" and comp_input == "rock":
            print("You WON!!!")
            user_wins += 1

        elif user_input == "scissors" and comp_input == "paper":
            print("You WON!!!")
            user_wins += 1
        elif user_input == comp_input:
            print("DRAW YOWEE!!!")
            draw += 1

        else:
            print("Comp Wins!!!")
            comp_wins += 1

    print("\n\nYou WON", user_wins, "times")
    print("Comp WON", comp_wins, "times")
    print("You DRAW", draw, "times")
    print("\nGOODBYE!!!!!!")

