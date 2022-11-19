import random

computer = ["Rock", "Paper", "Scissor"]
computer_choose = random.choice(computer)

while True:
    player_choose = input("You choose Rock, Paper or Scissor: ").capitalize()

    print("---------")
    print("You choose: " + player_choose)
    print("Computer choose: " + computer_choose)
    print("---------")

    if computer_choose == player_choose:
        print("--- Draw ---")
    elif player_choose == "Rock":
        if computer_choose == "Paper":
            print("--- You Lose ---")
        else:
            print("--- You Win ---")
    elif player_choose == "Paper":
        if computer_choose == "Rock":
            print("--- You Lose ---")
        else:
            print("--- You Win --- ")
    else:
        if computer_choose == "Paper":
            print("--- You Win ---")
        else:
            print("--- You Lose ---")

    choose_exit = input("Do you want to exit? (Yes / No) ").capitalize()
    if choose_exit == "Yes" or "yes".capitalize() or "y".capitalize() or "Y":
        break

