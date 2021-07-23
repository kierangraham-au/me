# -*- coding: UTF-8 -*-
"""Run the tests.

This file tests your code. It'll check that the work in each
of the exercise files does what it's supposed to.
"""

import importlib.util as importUtils
import os
import string
import sys
from pathlib import Path

from colorama import Fore, Style
from func_timeout import FunctionTimedOut, func_timeout

sys.path.append(os.path.dirname(os.path.dirname(__file__)))


from codeHelpers import (
    completion_message,
    ex_runs,
    finish_up,
    lab_book_entry_completed,
    loadExerciseFile,
    nyan_cat,
    syntax_error_message,
    test,
    test_flake8,
)

EM = Fore.YELLOW
NORM = Fore.WHITE

TIMEOUT_IN_SECONDS = 3


SET_NUMBER = 8
testResults = []

if "week" in os.getcwd():
    os.chdir("..")


def exam_test(
    expected,
    args,
    function_to_test,
    finishing_function=None,
    extra_message="",
    chdir=False,
):
    print(extra_message)
    template = (
        "{n}:\n"  ############################################################
        "    given:    {a}\n"
        "    expected: {e}\n"
        "    got:      {g}\n"
    )
    try:
        if chdir:
            if "quiz" not in os.getcwd():
                os.chdir("./quiz")
        got = function_to_test(*args)
        if chdir:
            if "week" in os.getcwd():
                os.chdir("..")
        if finishing_function:
            print("raw", got)
            got = finishing_function(got)
        if len(args) == 0:
            args = "* no args *"
        elif len(args) == 1:
            args = args[0]
        # else:
        #     args = args
        message = template.format(
            n=function_to_test.__name__, a=args, e=expected, g=got
        )
        testResults.append(test(got == expected, message))
    except Exception as e:
        message = template.format(n=function_to_test.__name__, a=args, e=expected, g=e)
        testResults.append(test(False, message))


def theTests(path_to_code_to_check="../me"):
    """Run all the tests."""
    print("\nWelcome to the exam!")
    print("May the odds be ever in your favour.\nEspecially today!")

    if ex_runs(path_to_code_to_check, exerciseNumber=1, weekNumber=SET_NUMBER):
        exam = loadExerciseFile(
            path_to_code_to_check, weekNumber=SET_NUMBER, exerciseNumber=1
        )

        # testResults.append(test(test_flake8(ex1path), "pass the linter"))
        exam_test(
            True,
            [],
            exam.string_please,
            finishing_function=lambda x: type(x) is str,
            extra_message="Don't over think this! just return a string!",
        )
        exam_test(
            True,
            [],
            exam.list_please,
            finishing_function=lambda x: type(x) is list,
            extra_message="Don't over think this! just return a list!",
        )
        exam_test(
            True,
            [],
            exam.dictionary_please,
            finishing_function=lambda x: type(x) is dict,
            extra_message="Don't over think this! just return a dictionary!",
        )
        exam_test(True, [5], exam.is_it_5)
        exam_test(False, [4], exam.is_it_5)
        exam_test(False, ["cats"], exam.is_it_5)
        exam_test(0, [5], exam.take_five)
        exam_test(5, [10], exam.take_five)
        exam_test(-5, [0], exam.take_five)

        exam_test("Hello the Queen", ["the Queen"], exam.greet)
        exam_test("Hello Pr♂nc♀♂", ["Pr♂nc♀♂"], exam.greet)

        exam_test(4, [[3, 3, 3, 3, 1]], exam.three_counter)
        exam_test(0, [[0, 1, 2, 5, -9]], exam.three_counter)

        exam_test(2, [7], exam.n_counter)
        exam_test(5, [0, [0, 0, 0, 0, 0, [0]]], exam.n_counter)

        # fmt: off
        fizza = [
            1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 
            13, 14, "FizzBuzz", 16, 17, "Fizz", 19, "Buzz", "Fizz", 22, 23, 
            "Fizz", "Buzz", 26, "Fizz", 28, 29, "FizzBuzz", 31, 32, "Fizz", 34, 
            "Buzz", "Fizz", 37, 38, "Fizz", "Buzz", 41, "Fizz", 43, 44, 
            "FizzBuzz", 46, 47, "Fizz", 49, "Buzz", "Fizz", 52, 53, "Fizz", 
            "Buzz", 56, "Fizz", 58, 59, "FizzBuzz", 61, 62, "Fizz", 64, "Buzz", 
            "Fizz", 67, 68, "Fizz", "Buzz", 71, "Fizz", 73, 74, "FizzBuzz", 76, 
            77, "Fizz", 79, "Buzz", "Fizz", 82, 83, "Fizz", "Buzz", 86, "Fizz", 
            88, 89, "FizzBuzz", 91, 92, "Fizz", 94, "Buzz", "Fizz", 97, 98, 
            "Fizz", "Buzz", ]
        # fmt: on
        exam_test(fizza, [], exam.fizz_buzz)

        exam_test(
            "|a| |s|e|r|i|a|l| |k|i|l|l|e|r|", ["a serial killer"], exam.put_behind_bars
        )
        exam_test("|a| |b|a|r|t|e|n|d|e|r|", ["a bartender"], exam.put_behind_bars)

        exam_test(["red fox"], ["x"], exam.pet_filter)
        exam_test([], ["q"], exam.pet_filter)
        exam_test(
            ["pig", "sheep", "guinea pig", "pigeon", "alpaca", "guppy"],
            ["p"],
            exam.pet_filter,
        )

        exam_test("e", [], exam.best_letter_for_pets)

        word_lengths = [[3, 3, 3], [4, 4, 4], [5, 5, 5], [6, 6, 6], [7, 7, 7]]
        exam_test(
            word_lengths,
            [],
            exam.make_filler_text_dictionary,
            lambda x: [[len(w) for w in x[k]] for k in x.keys()],
        )

        exam_test(
            True,
            [50],
            exam.random_filler_text,
            lambda x: len(x.split(" ")) == 50 and len(x) > 3 * 50,
        )

        exam_test(
            True,
            [1000],
            exam.random_filler_text,
            lambda x: len(x.split(" ")) == 1000 and len(x) > 3 * 1000,
        )

        clean_out_old_env()

        exam_test(
            True,
            [100],
            exam.fast_filler,
            lambda x: len(x.split(" ")) == 100 and len(x) > 3 * 100,
            # chdir=True, # NFI what this does :(
        )

        # exam_test(True, ["./week8/dict_racey.json"], os.path.exists)

        exam_test(
            True,
            [10],
            exam.fast_filler,
            lambda x: x[0] in string.ascii_uppercase and x[1] in string.ascii_lowercase,
            "Test if fast_filler is capitalised",
        )
        exam_test(
            True,
            [10],
            exam.fast_filler,
            lambda x: x[-1] == ".",
            "Test if fast_filler finishes with a .",
        )

        print(
            "The point of saving the dictionary is that it's fast!",
            "The pattern of saving a value locally so that you don't",
            "need to go and get it is called caching.",
            "This test runs fast_filler 10 times, and if it manages it in less",
            "than a second, then you're good to go!",
            sep="\n",
        )
        try:
            TIMEOUT_IN_SECONDS = 1
            func_timeout(
                TIMEOUT_IN_SECONDS,
                lambda: [exam.fast_filler(1000) for _ in range(10)],
                args=[],
            )
            testResults.append(test(True, "subsequent fast_filler"))
        except FunctionTimedOut as t:
            m = (
                "Timed out trying to run fast filler 10 times in 1 second, "
                "subsequent fast_filler probably wasn't fast enough"
            )
            print(m, str(t))
            testResults.append(test(False, m + str(t)))
        except Exception as e:
            testResults.append(test(False, "subsequent fast_filler failed: " + str(e)))

    message = (
        "Cowabunga! You've got all the tests passing!\n"
        "Well done, that's all the exercises for this term out of the way!"
    )
    print(testResults)
    return finish_up(testResults, message, nyan_cat())


def clean_out_old_env():
    """Remove old JSON before running more tests.
    
    Previous tests leave an old json file. The code looks for it, and finds it
    but it was made by the previous student, not this one.
    """
    d = "dict_racey.json"
    if os.path.exists(d):
        print("Remove the old cached JSON before continuing.")
        os.remove(d)


if __name__ == "__main__":
    theTests()
    # "C:\\Users\\ben\\code1161\\StudentRepos\\chriswng"
