# import Python random library
import random

# hey computer, generate a secret
# number between 1 and 100
secret = random.randint(1,100)

# a counter to count number of attempts
# before user found the secret number
attempts = 0

# keep guessing till user inputs 0 to exit
while True:

    # increment counter by 1 for every while loop
    attempts = attempts + 1
    try: # exception handling for wrong input
        # user input
        guess = int(input("What is your guess? "))

        # logical statements to evaluate user input
        if(guess == 0): # exit out of while loop
            print("bye bye")
            break
        elif(guess == secret): # secret found
            print("You found the secret", secret, "in", attempts, "attempts")
            break
        elif(guess > secret): # guess > secret
            print("Too high")
        else:  # guess < secret
            print("Too low")
    # send value error in case wrong input
    except ValueError:
        print("Enter an integer between 1 and 100")

