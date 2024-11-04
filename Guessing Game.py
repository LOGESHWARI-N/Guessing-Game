import random

print("Welcome to Guessing Game")

number_to_guess = random.randint(1,100)
guess = None
attempts = 0

print("I guess the number from 1 to 100:")

while guess != number_to_guess:
    guess= int(input("guess a number:"))
    number_to_guess = 50
    attempts += 1
    
    if attempts == 10:
        print("You lost the game")
    
    elif guess < number_to_guess:
        print("guessing number is low ! Try again")

    elif guess > number_to_guess:
        print("guessing number is high! Please Try again")
    

    else:   
        print("Your guessing is correct")

    
      






