from random import randint

logo = """

                                                                 
                        _   _                        _           
 ___ _ _ ___ ___ ___   | |_| |_ ___    ___ _ _ _____| |_ ___ ___ 
| . | | | -_|_ -|_ -|  |  _|   | -_|  |   | | |     | . | -_|  _|
|_  |___|___|___|___|  |_| |_|_|___|  |_|_|___|_|_|_|___|___|_|  
|___|                                                            
                                                                                
"""

#ascii art generator - http://patorjk.com/software/taag/#p=display&f=BlurVision%20ASCII&t=anusha%20
print(logo)

print("""
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
""")

attempts = 0
level = input("Choose a difficulty. Type 'easy' or 'hard': ")
if level == 'easy':
    attempts = 5
else:
    attempts = 10

chosen_num = randint(1,100)

game_over = False
while not game_over:
    print(f"You have {attempts} attempts remaining to guess")
    num = int(input("Make a guess: "))
    attempts -= 1

    if num == chosen_num:
        game_over = True
        print(f"You got it! answer is {chosen_num}")
    elif attempts == 0:
        game_over = True
        print(f"You lost! Answer was {chosen_num} Better luck next time.")
    elif num < chosen_num:
        print("Too Low")
        print("Guess again")
    else:
        print("Too High")
        print("Guess again")


