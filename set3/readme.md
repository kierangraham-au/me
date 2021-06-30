TODO: Reflect on what you learned this week and what is still unclear.
def stubborn_asker(low, high):
    """Ask for a number between low and high until actually given one.

    Ask for a number, and if the response is outside the bounds keep asking
    until you get a number that you think is OK

    Look up the docs for input
    """
    Inputstring = int(
        input("Please enter a number between {} and {}: ").format(low, high)
    )
    while low < Inputstring > high:
        return Inputstring
    else:
        print("The number needs to be between {} and {}")

    print(Inputstring)
    return Inputstring

    Super frustrating question, the int format doesnt make sense in the context. I have no idea how its working and my line doesnt even prompt me for an input.

    Inputstring = int(
        input("Please enter a number between {} and {}: ").format(low, high)
    )
    while low < Inputstring > high:
        return Inputstring
    else:
        print("The number needs to be between {} and {}")

    print(Inputstring)
    return Inputstring

    New try
    number = int()
    print("Think of a number between {} and {}: ".format(low, high))
    Inputstring = int(input("Number: ", number))
    while low < Inputstring > high:
        try:
            return Inputstring
        except TypeError:
            print("The number needs to be between {} and {}".format(low, high))

    print(Inputstring)
    return Inputstring


    Creating my own function didn't work

     def my_function(number=int(input("Number: "))):

        number = int()
        print("Think of a number between {} and {}: ".format(low, high))
        my_function
        while (number < low) or (number > high):
            print("The number needs to be between {} and {}".format(low, high))
            return my_function
        else:
            return number

Finally got the right answer

print("Think of a number between {} and {}: ".format(low, high))
    
    number = int(input("Number: "))

    while (number < low) or (number > high):
        print("The number needs to be between {} and {}".format(low, high))
        number = int(input("Number: "))
    else:
        return number

    Reformatted next question with information from google

    keep_asking = True

    while keep_asking:
        try:
            print(message)
            number = input("Number: ")
        except (ValueError, TypeError):
            print("That is not a number, please try again.")
            number = input("Number: ")

        return number


        Number Guesser

        print("\nWelcome to the guessing game!")
    print("A number between _ and _ ?")
    lowerBound = input("Enter a lower bound: ")
    upperBound = input("Enter an upper bound: ")
    print("OK then, a number between {} and {} ?".format(lowerBound, upperBound))
    lowerBound = int(lowerBound)
    upperBound = int(upperBound)

    actualNumber = random.randint(lowerBound, upperBound)

    guessed = False

    while not guessed:
        guessedNumber = input("Guess a number: ")
        print(
            "You guessed {},".format(guessedNumber),
        )
        try:
            if guessedNumber == actualNumber:
                print("You got it!! It was {}".format(actualNumber))
                guessed = True
            elif guessedNumber < actualNumber:
                print("Too small, try again :'(")
            else:
                print("Too big, try again :'(")
        except (ValueError):
            print("That is not an integer, please try again.")

    return "You got it!"



    Version 2


    print("\nWelcome to the guessing game!")
    print("A number between _ and _ ?")
    lowerBound = input("Enter a lower bound: ")
    upperBound = input("Enter an upper bound: ")
    print("OK then, a number between {} and {} ?".format(lowerBound, upperBound))
    lowerBound = int(lowerBound)
    upperBound = int(upperBound)

    actualNumber = random.randint(lowerBound, upperBound)

    guessed = False

    while not guessed:
        guessedNumber = input("Guess a number: ")
        print(
            "You guessed {},".format(guessedNumber),
        )
        if guessedNumber.isnumeric == True:
            if guessedNumber == actualNumber:
                print("You got it!! It was {}".format(actualNumber))
                guessed = True
            elif guessedNumber < actualNumber:
                print("Too small, try again :'(")
            else:
                print("Too big, try again :'(")
        else:
            print("That is not an integer, please try again.")

    return "You got it!"


Version 3

print("\nWelcome to the guessing game!")
    print("A number between _ and _ ?")
    lowerBound = input("Enter a lower bound: ")
    upperBound = input("Enter an upper bound: ")
    print("OK then, a number between {} and {} ?".format(lowerBound, upperBound))
    lowerBound = int(lowerBound)
    upperBound = int(upperBound)

    actualNumber = random.randint(lowerBound, upperBound)

    guessed = False

    while not guessed:
        try:
            guessedNumber = input("Guess a number: ")
            print(
                "You guessed {},".format(guessedNumber),
            )
        except:
            if not guessedNumber.isnumeric():
                print("That is not an integer, please try again.")
            else:
                guessedNumber.isnumeric()

            if guessedNumber == actualNumber:
                print("You got it!! It was {}".format(actualNumber))
                guessed = True
            elif guessedNumber < actualNumber:
                print("Too small, try again :'(")
            else:
                print("Too big, try again :'(")

    return "You got it!"



Version 4

print("\nWelcome to the guessing game!")
    print("A number between _ and _ ?")
    lowerBound = input("Enter a lower bound: ")
    upperBound = input("Enter an upper bound: ")
    print("OK then, a number between {} and {} ?".format(lowerBound, upperBound))
    lowerBound = int(lowerBound)
    upperBound = int(upperBound)

    actualNumber = random.randint(lowerBound, upperBound)

    guessed = False

    while not guessed:
        try:
            guessedNumber = int(input("Guess a number: "))
            print(
                "You guessed {},".format(guessedNumber),
            )
            
        except (ValueError, TypeError):
            print("That is not an integer, please try again.")

            guessedNumber = input("Guess a number: ")

            if guessedNumber == actualNumber:
                print("You got it!! It was {}".format(actualNumber))
                guessed = True
            elif guessedNumber < actualNumber:
                print("Too small, try again :'(")
            else:
                print("Too big, try again :'(")

    return "You got it!"

    Version 5


    print("\nWelcome to the guessing game!")
    print("A number between _ and _ ?")
    lowerBound = input("Enter a lower bound: ")
    upperBound = input("Enter an upper bound: ")
    print("OK then, a number between {} and {} ?".format(lowerBound, upperBound))
    lowerBound = int(lowerBound)
    upperBound = int(upperBound)

    actualNumber = random.randint(lowerBound, upperBound)

    guessed = False

    while not guessed:

        guessedNumber = input("Guess a number: ")
        print(
            "You guessed {},".format(guessedNumber),
        )
        if guessedNumber.isnumeric():
            guessedNumber = int(guessedNumber)
            if guessedNumber == actualNumber:
                print("You got it!! It was {}".format(actualNumber))
                guessed = True
            elif guessedNumber < actualNumber:
                print("Too small, try again :'(")
            else:
                print("Too big, try again :'(")
        else:
            print("That is not a number")

    return "You got it!"

    return "You got it!"



    Version 6

    print("\nWelcome to the Advanced guessing game!")
    print("A number between _ and _ ?")

    try:
        lowerBound = input("Enter a lower bound: ")
        upperBound = input("Enter an upper bound: ")
    except (ValueError, TypeError):
        print("That is not an integer, please try again. ")
        lowerBound = input("Enter a lower bound: ")
        upperBound = input("Enter an upper bound: ")
    if lowerBound.isnumeric() and upperBound.isnumeric():

        print("OK then, a number between {} and {} ?".format(lowerBound, upperBound))
    lowerBound = int(lowerBound)
    upperBound = int(upperBound)

    actualNumber = random.randint(lowerBound, upperBound)

    guessed = False

    while not guessed:

        guessedNumber = input("Guess a number: ")
        print("You guessed {},".format(guessedNumber))

        if guessedNumber.isnumeric():
            guessedNumber = int(guessedNumber)
            if (lowerBound > guessedNumber) or (upperBound < guessedNumber):
                print("That is not within the bounds.")
            elif guessedNumber == actualNumber:
                print("You got it!! It was {}".format(actualNumber))
                guessed = True
            elif guessedNumber < actualNumber:
                print("Too small, try again :'(")
            else:
                print("Too big, try again :'(")
        else:
            print("That is not a number")
    else:
        print("That is not a number")

    return "You got it!"


    Version 7

    started = True

    while started:

        lowerBound = input("Enter a lower bound: ")
        if lowerBound.isnumeric():
            continue
        else:
            print("That is not a valid integer.")

        upperBound = input("Enter a lower bound: ")
        if upperBound.isnumeric():
            continue
        else:
            print("That is not a valid integer.")

        lowerBound = int(lowerBound.isnumeric())
        upperBound = int(upperBound.isnumeric())

        print("OK then, a number between {} and {} ?".format(lowerBound, upperBound))

        actualNumber = random.randint(lowerBound, upperBound)

        guessed = False

        while not guessed:

            guessedNumber = input("Guess a number: ")
            print("You guessed {},".format(guessedNumber))

            if guessedNumber.isnumeric():
                guessedNumber = int(guessedNumber)
                if (lowerBound > guessedNumber) or (upperBound < guessedNumber):
                    print("That is not within the bounds.")
                elif guessedNumber == actualNumber:
                    print("You got it!! It was {}".format(actualNumber))
                    guessed = True
                elif guessedNumber < actualNumber:
                    print("Too small, try again :'(")
                else:
                    print("Too big, try again :'(")

    return "You got it!"

     lowerBoundn = lowerBound.isnumeric()
    upperBoundn = upperBound.isnumeric()
    started = True
    
    while started:
      
      try:
        lowerBound = input("Enter a lower bound: ")
        upperBound = input("Enter an upper bound: ")
      
      except:
        lowerBoundn = lowerBound.isnumeric()
        upperBoundn = upperBound.isnumeric()

        lowerBound = int
        upperBound = int
        print("OK then, a number between {} and {} ?".format(lowerBound, upperBound))

        actualNumber = random.randint(lowerBound, upperBound)

        guessed = False

        while not guessed:

            guessedNumber = input("Guess a number: ")
            print("You guessed {},".format(guessedNumber))

            if guessedNumber.isnumeric():
                guessedNumber = int(guessedNumber)
                if (lowerBound > guessedNumber) or (upperBound < guessedNumber):
                    print("That is not within the bounds.")
                elif guessedNumber == actualNumber:
                    print("You got it!! It was {}".format(actualNumber))
                    guessed = True
                elif guessedNumber < actualNumber:
                    print("Too small, try again :'(")
                else:
                    print("Too big, try again :'(")

    return "You got it!"


    Very lost, cant seem to figure out how to loop check each input to receive the right integer. isnumeric seems to be the right fit but It just wont work with the syntax I'm using.
    The second half of the column works great, but as soon as I tried testing it through the course, it didnt work because it requires the inputs to be checked as well. 

    started = True

    while started:

        lowerBound = input("Enter a lower bound: ")
        if lowerBound.isnumeric():
            lowerBound = int(lowerBound)
        else:
            print("That is not a valid input")

        upperBound = input("Enter a upper bound: ")
        if upperBound.isnumeric():
            upperBound = int(upperBound)
        else:
            print("That is not a valid input")


    print("OK then, a number between {} and {} ?".format(lowerBound, upperBound))

    actualNumber = random.randint(lowerBound, upperBound)

    guessed = False

    while not guessed:

        guessedNumber = input("Guess a number: ")
        print("You guessed {},".format(guessedNumber))

        if guessedNumber.isnumeric():
            guessedNumber = int(guessedNumber)
            if (lowerBound > guessedNumber) or (upperBound < guessedNumber):
                print("That is not within the bounds.")
            elif guessedNumber == actualNumber:
                print("You got it!! It was {}".format(actualNumber))
                guessed = True
            elif guessedNumber < actualNumber:
                print("Too small, try again :'(")
            else:
                print("Too big, try again :'(")

    return "You got it!"



Version 8

It doesnt make any sense. I tried using isdigit() and that didnt help. There doesnt seem to be any resources on how to figure this out.

Version 9

started = False
    started2 = False

    while not started:
        try:
            lowerBound = int(input("Enter a lower bound: "))
        except ValueError:
            print("That is not a valid input")
        

    while not started2:

        try:
            upperBound = int(input("Enter a upper bound: "))
        except ValueError:
            print("That is not a valid input")

    print("OK then, a number between {} and {} ?".format(lowerBound, upperBound))

    actualNumber = random.randint(lowerBound, upperBound)

    guessed = False

    while not guessed:

        guessedNumber = input("Guess a number: ")
        print("You guessed {},".format(guessedNumber))

        if guessedNumber.isnumeric():
            guessedNumber = int(guessedNumber)
            if (lowerBound > guessedNumber) or (upperBound < guessedNumber):
                print("That is not within the bounds.")
            elif guessedNumber == actualNumber:
                print("You got it!! It was {}".format(actualNumber))
                guessed = True
            elif guessedNumber < actualNumber:
                print("Too small, try again :'(")
            else:
                print("Too big, try again :'(")

    return "You got it!"

Getting help from a friend because I know I'm close but I just cant get the beggining part to match up right.

Final Answer

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

    Still a bit confused but I needed to get it done. Glad its finished and I'll take a look at my previous formatting to understand what I was doing that was messing up the first part, resulting in the second part not working. The second part was working fine but I couldn't get through the first function.

    Binary Search
    

