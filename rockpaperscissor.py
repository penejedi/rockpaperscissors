import random
import sys

# initial total of wins, loses and ties
wins = 0
loses = 0
ties = 0

# available choices for pc
move_choices = ["ROCK", "PAPER", "SCISSORS"]

print("ROCK, PAPER, SCISSORS")
# infinite loop unless user type in 'q'
while True:
    pc_move = random.choice(move_choices)  # pc choose randomly every loop
    print("{} wins, {} loses, {} ties".format(wins, loses, ties))
    user_move = input("Enter your move: (r)ock (p)aper (s)cissors or "
                      "(q)uit\n")
    valid_choices = "rpsq"

    # choice is valid
    while user_move.casefold() in valid_choices:
        # quit from games
        if user_move.casefold() == "q":
            sys.exit()
        # rock is user choice
        elif user_move.casefold() == "r":
            print("{} versus...".format(move_choices[0]))
            print(pc_move)
            if pc_move == move_choices[0]:
                print("It is a tie!")
                ties += 1
            elif pc_move == move_choices[1]:
                print("You loose!")
                loses += 1
            elif pc_move == move_choices[2]:
                print("You win!")
                wins += 1
            break
        # paper is user choice
        elif user_move.casefold() == "p":
            print("{} versus...".format(move_choices[1]))
            print(pc_move)
            if pc_move == move_choices[0]:
                print("You win!")
                wins += 1
            elif pc_move == move_choices[1]:
                print("It is a tie!")
                ties += 1
            elif pc_move == move_choices[2]:
                print("You loose!")
                loses += 1
            break
        # scissors is user choice
        elif user_move.casefold() == "s":
            print("{} versus...".format(move_choices[2]))
            print(pc_move)
            if pc_move == move_choices[0]:
                print("You loose!")
                loses += 1
            elif pc_move == move_choices[1]:
                print("You win!")
                wins += 1
            elif pc_move == move_choices[2]:
                print("It is a tie!")
                ties += 1
            break
    # return to loop if choice is not valid
    else:
        print("Please type either r, p, s or q")
        continue
        
