"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

# I think this creates a list of words that will be recalled later.
some_words = ['what', 'does', 'this', 'line', 'do', '?'] #It printed the entire list


# I think this prints "word"
for word in some_words: #this did nothing
    print(word)

# I think this prints "x"
for x in some_words: #this did nothing
    print(x)

# I think this prints the whole list
print(some_words) #printed the entire list in the format of a list

# I think this prints words that contain more than 3 words
if len(some_words) > 3:
    print('some_words contains more than 3 words') #since some_words contained more than 3 words, it printed the statement "some words contain more than 3 words"

# I think this returns the details of the computer
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())

# I think Useful Function gives all the computer information as a callable string
usefulFunction() #it printed the system details
