# -*- coding: UTF-8 -*-
"""Set 3, Exercise 4."""


import math
import random

# import time


def binary_search(low, high, actual_number):
    """Do a binary search.

    This is going to be your first 'algorithm' in the usual sense of the word!
    you'll give it a range to guess inside, and then use binary search to home
    in on the actual_number.

    Each guess, print what the guess is. Then when you find the number return
    the number of guesses it took to get there and the actual number
    as a dictionary. make sure that it has exactly these keys:
    {"guess": guess, "tries": tries}

    This will be quite hard, especially hard if you don't have a good diagram!

    Use the VS Code debugging tools a lot here. It'll make understanding 
    things much easier.
    """
    tries = 0
    guess = 0

    # Write your code in here

    print("\nWelcome to Kieran's Binary Search")
    print("A guess between {0} and {1}?".format(low, high))
    print("Actual number: {}".format(actual_number))

    while guess != actual_number:

        mid = (high + low) // 2
        mid = int(mid)
        try:

            if guess == actual_number:
                guess = mid
                tries += 1
                print("You got it!")

            elif mid > actual_number:
                high = mid
                tries += 1
                mid = mid - 1
                print("{}".format(mid))
            else:
                low = mid
                tries += 1
                mid = mid + 1
                print("{}".format(mid))
            guess = mid

        except (ValueError, TypeError):
            print("{} is not a number, try again: ".format(guess))

    return {"guess": guess, "tries": tries}


if __name__ == "__main__":
    print(binary_search(1, 100, 5))
    print(binary_search(1, 100, 6))
    print(binary_search(1, 100, 95))
    print(binary_search(1, 51, 5))
    print(binary_search(1, 50, 5))
