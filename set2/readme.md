TODO: Reflect on what you learned this week and what is still unclear.
Exercise 0 took me a bit to get, I didn't understand the errors I was getting, especially when it came to the tests. I ended up giving up on exercise 3 at 4:30pm on Friday and am attempting it again on Sunday.

I wasnt able to watch the lecture before class so that explains the lack of comprehension during class.

the "str" addition to the string + number task on exercise 0 took me asking someone for help. I still didnt understand how he got the str addition, though it was shown in the lecture.

Exercise 1 made sense after debugging

Exercise 2 seemed to make sense, but I'm not sure if it worked correctly or not.

Attemping exercise 3 now, to do the logical fix it task.
I attempted it by making each of the phrases "WD-4", "No Problem" etc variables and called them after true/false definitions were reached, but I ended up passing 2/4 tests, so I deleted the code and tried again, only reaching 1/4 tests this time.

var1 = "WD-40"
    var2 = "Duct Tape"
    var3 = "No Problem"
    if moves == True:
        should_move == True
             else moves == False
        elif moves == False:
            should_move == True
            return var1
        elif moves == True:
            should_move == False
            return var2

    return None

Current attempt looks like this. I examined some other codes before leaving on Friday to get a grasp of how the right answer looked, but I'll try to figure it out myself.
There is no need to define variables in the code, as you can just return the string and it will be correct.

Everything went smoothly until loop_1c
I tried:

for number in number_of_items:
        return symbol

I know that doesnt give the computer much but it worked for the previous question. I dont know how to call a list. 

 symbols_list = [
        "#",
        "#",
        "#",
        "#",
        "#",
    ]
    
    return symbols_list

    I tried making a symbols list
    
    symbols_list = [
        "#",
        "#",
        "#",
        "#",
        "#",
    ]

    for number_of_items in symbols_list:
        return symbols_list

Returning symbols 

    symbols_list = [
        "#",
        "#",
        "#",
        "#",
        "#",
    ]

    for number_of_items in symbols_list:
        return symbol

    return loops_1c

Another attempt 

    symbols_list = ["#"]

    final = symbols_list * number_of_items

    return symbols_list

    return loops_1c

Very confused, very frustrated

symbols_list = ["#"]

    final = symbols_list * 5
    return symbols_list

Final try

    symbols_list = number_of_items * symbol

    return symbols_list

    Gave up.

    for i in range(number_of_items):
        return symbol

    return loops_1c

14/06/2021

New day, many messages from friends explaining the problem. I now understand that integers cant be read by the program, therefore it doesnt execute.

symbols = [] #create list
    for i in range(0, number_of_items): #for loop with range starting at 0, number of items being the final iteration
        symbols.append(symbol) #add symbol at the end of the list, iterated by number of items

    return symbols

I didnt understand the for loops and missed that part of learning somewhere. I've used for loops in C++ before but I dont know where to put them/what tools to use to solve each problem. I'm not sure if I'm missing a part of the abstraction, but I know I learn the best by being shown examples first and then replicating them, therefore learning through doing rather than taking a concept and applying it by the fundamental rules. Doesnt compute for me.

stars_list = []  # create the list of stars to be 10
    main_list = []  # create the list that will hold the 10 lists

    for j in range(10):  # for loop that iterates 10 times
        stars_list.append("*")  # stars list that adds a star 10 times to each list
    for i in range(10):  # for loop that iterates 10 times, to create 10 lists
        main_list.append(stars_list)  # mainlist adds 1 stars list 10 times

    print(main_list)
    return loops_2

Did not work. I cant figure out how to add an enter, if thats even the problem here.

After looking at the answer, I understand slightly how it works. I didn't know actually having to define the grid within the loop was an issue.

main_list = []  # create the list that will hold the 10 lists

    for j in range(10):  # for loop that iterates 10 times
        stars_list = []  # create the list of stars to be 10
        for i in range(10):  # for loop that iterates 10 times, to create 10 lists
            stars_list.append("*")  # stars list that adds a star 10 times to each list
        main_list.append(stars_list)  # mainlist adds 1 stars list 10 times

    print(main_list)
    return main_list

After consulting the answer, and returning main_list back instead of loops_2, the previous answer worked as well, but I was returning loop_2 and that for some reason was not checking the box.

I need to return the final function, not just the name of it for the next question.

numbers_list = []  # create the list that will hold the 10 lists

    for j in range(10):  # for loop that iterates 10 times
        integers_list = []  # create the list of integers
        for i in range(10):  # iterate 10 times
            integers_list.append(j)  # iterate with the current integer being used
        numbers_list.append(integers_list) 

    print(numbers_list)
    return numbers_list

    I got the right answer, but it didnt get the tick due to using integers rather than a string.
    
    numbers_list = []  # create the list that will hold the 10 lists

    for j in range(10):  # for loop that iterates 10 times
        integers_list = []  # create the list of strings
        for i in range(10):  # iterate 10 times
            integers_list.append(str(j))  # iterate with the current string being used
        numbers_list.append(integers_list)  

    print(numbers_list)
    return numbers_list

    Much quicker result.

    After looking at the answer for the stars box and realising I can use my code from the previous questions, the answers seem less daunting.

numbers_list = []  # create the list that will hold the 10 lists

    for j in range(10):  # for loop that iterates 10 times
        integers_list = []  # create the list of strings
        for i in range(10):  # iterate 10 times
            integers_list.append(str(i))  # iterate with the current string being used
        numbers_list.append(integers_list)  

    print(numbers_list)
    return numbers_list

Loops 5

Looks like I have to use dictionaries or tuples here. Something like that.


numbers_list = []  # create the list that will hold the 10 lists

    for i in range(10):  # for loop that iterates 5 times
        integers_list = []  # create the list of integers
        for j in range(0, 5):  # iterate 5 times
            integers_list.append(
                str(i) + str(j)
            )  # iterate with i and j, adding them together
        numbers_list.append(integers_list)

    print(numbers_list)
    return numbers_list

    didnt need to but it returned values adding each other together, which I was afraid of. I need to find a way to include the integers as seperate lists maybe?

    numbers_list = []  # create the list that will hold the 10 lists

    for i in range(10):  # for loop that iterates 5 times
        integers_list = []  # create the list of integers
        for j in range(0, 5):  # iterate 5 times
            integers_list.append(
                "i" + str(i), "j" + str(j)
            )  # iterate with i and j, adding them together
        numbers_list.append(integers_list)

    print(numbers_list)
    return numbers_list

    didnt work

    numbers_list = []  # create the list that will hold the 10 lists

    for i in range(10):  # for loop that iterates 5 times
        integers_list = []  # create the list of integers
        for j in range(0, 5):  # iterate 5 times
            integers_list.append(
                ("i" + i, "j" + j)
            )  # iterate with i and j, adding them together
        numbers_list.append(integers_list)

    print(numbers_list)
    return numbers_list

Another
    numbers_list = []  # create the list that will hold the 10 lists

    for i in range(10):  # for loop that iterates 5 times
        integers_list = []  # create the list of integers
        for j in range(0, 5):  # iterate 5 times
            integers_list.append(
                ("i{i}", "j{j}")
            )  # iterate with i and j, adding them together
        numbers_list.append(integers_list)

    print(numbers_list)
    return numbers_list


    Another
    
    numbers_list = []  # create the list that will hold the 10 lists

    for i in range(10):  # for loop that iterates 5 times
        integers_list = []  # create the list of integers
        for j in range(0, 5):  # iterate 5 times
            integers_list.append((str("i")+i,str("j")+j))  # iterate with i and j, adding them together
        numbers_list.append(integers_list)

    print(numbers_list)
    return numbers_list




Got the right answers but it didnt get the tick

numbers_list = []  # create the list that will hold the 10 lists

    for i in range(10):  # for loop that iterates 5 times
        integers_list = []  # create the list of integers
        for j in range(0, 5):  # iterate 5 times
            integers_list.append(("i" + str(i), "j" + str(j)))
        numbers_list.append(integers_list)

    print(numbers_list)
    return numbers_list

    After looking at the answer, I can see the format option needed i and j in it. I shouldve googled how the format option works because it wouldve made my life easier.

    numbers_list = []  # create the list that will hold the 10 lists

    for i in range(10):  # for loop that iterates 5 times
        integers_list = []  # create the list of integers
        for j in range(0, 5):  # iterate 5 times
            integers_list.append("(i{}, j{})".format(i, j))
        numbers_list.append(integers_list)

    print(numbers_list)
    return numbers_list

    final answer, post trouble shooting with formatting



    wedge_list = []  # create wedge list

    for i in range(
        1, 11
    ):  # add 1 to the range so you dont get the initial list generated
        mario_list = []  # create the second list inside the for loop
        for j in range(i):  # iterate with i to receive increasing numbers
            mario_list.append(
                str(j)
            )  # iterate with j so the for loop continues going up until it reaches the i cut off
        wedge_list.append(mario_list)  # add each list with each iteration

    return wedge_list

    wasnt too hard, once I figured out the range issue creating an extra []

    Structure for final question
    
    final_list = []  # create final list

    for i in range(1, 11):  #
        boss_list = []  #
        for j in range(i):  #
            boss_list.append(str(j))  #
        final_list.append(boss_list)  #

    return final_list

    final_list = []  # create final list
    depth = 5
    width = 9
    n = 1

    for i in range(depth):
        stars_grid = []
        for j in range(width):
            if j > i:
                stars_grid.append("*")
            stars_grid.append(" ")
        final_list.append(stars_grid)

    print(final_list)
    return final_list

Test

final_list = []  # create final list
    depth = 4
    width = 4
    n = 1

    for i in range(depth):
        stars_grid = []
        for j in range(width):
            if j == i:
                stars_grid.append("*")
            stars_grid.append(" ")
        final_list.append(stars_grid)

    print(final_list)
    return final_list

    Final Answer
    Had to mess around with equations and finally got it when I put the equations in the for loop, rather than defining them at the top
    
     final_list = []  # create final list

    j = 0
    n = (j * 2) + 1
    g = (9 - n) // 2
    x = 0
    y = 0
    z = 0

    for j in range(0, 5, 1):
        stars_grid = []
        n = (j * 2) + 1
        g = (9 - n) // 2
        for x in range(g):
            stars_grid.append(" ")
        for y in range(n):
            stars_grid.append("*")
        for z in range(g):
            stars_grid.append(" ")

        final_list.append(stars_grid)

    print(final_list)
    return final_list
