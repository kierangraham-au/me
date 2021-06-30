"""Set 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random
from typing import Type


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """

    print("\nWelcome to the Advanced guessing game!")
    print("A number between 10 and 20 ?")

    started = False

    while not started:
        try:
            lowerBound = input("Enter a lower bound: ")
            lowerBound = int(lowerBound)
            upperBound = input("Enter of upper bound: ")
            upperBound = int(upperBound)

            print(
                "OK then, a number between {} and {} ?".format(lowerBound, upperBound)
            )
            started = True

        except (ValueError, TypeError):
            print("Please enter an Integer: ")

    actualNumber = random.randint(lowerBound, upperBound)
    guessed = False
    while not guessed:
        try:
            guessedNumber = input("Guess a number: ")
            guessedNumber = int(guessedNumber)
            print("You guessed {},".format(guessedNumber))
            if guessedNumber == actualNumber:
                print("You got it!! It was {}".format(actualNumber))
                guessed = True

            elif (lowerBound > guessedNumber) or (upperBound < guessedNumber):
                print("That is not within the bounds.")

            elif guessedNumber < actualNumber:
                print("Too small, try again :'(")
            else:
                print("Too big, try again :'(")
        except (ValueError, TypeError):
            print("{} in not a number, try again: ".format(guessedNumber))

    return "You got it!"


# the tests are looking for the exact string "You got it!". Don't modify that!


if __name__ == "__main__":
    print(advancedGuessingGame())
