import random
from colorama import init, Fore

TRY = True
while TRY:
    print(random.randint(1, 6))
    ROLL = input(Fore.BLUE + "Want to roll the dice? (Yes/No): ")
    if ROLL.capitalize() == "Yes":
        continue
    else:
        break
print("Bye Bye Bye!!!")
