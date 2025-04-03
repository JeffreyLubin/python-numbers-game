#This is a simple numbers game

import random

high_score = []

# Pretend like this function doesn't exist
"""def record_high_score(guess_count):
    high_score.append(guess_count)
    print(high_score)"""

while True:

    numbers = [str(random.randint(0,25))]
    print(numbers)
    guess_count = 1
    numbers_count = 1


    # This while loop takes the user through the main game
    # Starts with user input
    while True:

        number_guess = input("\nGuess a number, any number!\nPress X to exit\n")

        # Check if amount of guesses is greater than 5, reset number if not
        if numbers_count >= 5:
            numbers = [str(random.randint(0,25))]
            numbers_count -= 4

        # Win scenario
        elif number_guess in numbers:
            high_score.append(guess_count)
            print(high_score)
            print(
                "\nCongrats, you win!\n Your total amount of tries was " 
                f"{guess_count}.\n")
            break

        # Close game
        elif number_guess == 'x':
            break

        # Lose turn, add a guess_count to keep track of how many turns
        # Lose turn, keep track of how many losses to reset the random number
        # Resetting random number is intentional; prevents trying every number
        else:
            print("\nAww man, you lose! Try again.\n")
            guess_count += 1
            numbers_count += 1
    

    # Closes the game entirely
    if number_guess == 'x':
        break

    # Restart prompt
        
    restart_try = input("Would you like to try again? y/n ")
            
    if restart_try != 'y':
        break
    else:
        print("Good luck!")     

        

