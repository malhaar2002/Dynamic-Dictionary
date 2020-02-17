import json
data = json.load(open("data.json"))

#library for autocorrect suggestions
import difflib
from difflib import get_close_matches

word = input("Enter the word: ")
word = word.lower()

suggestion = get_close_matches(word, data.keys())

def translate():
    if word in data:
        for index, value in enumerate(data[word], 1):
                 print(f'{index}. {value}')

    elif len(suggestion) == 0:
        print("Sorry, that word does not exist. Please double check it.")

    else:
        print("Sorry! That word does not exist.")
        print("Did you mean " + str(suggestion[0]) + " instead?")
        def ques_1():
            confirm_suggestion = input("Press 'y' for yes and 'n' for no: ")
            confirm_suggestion = confirm_suggestion.lower()
            if confirm_suggestion == "y":
                for index, value in enumerate(data[suggestion[0]], 1):
                    print(f"{index}. {value}")
            elif confirm_suggestion == "n":
                print("Sorry, that word does not exist. Please double check it.")
            else:
                print("That is not a valid answer.")
                ques_1()
        ques_1()

translate()

input("Press enter to exit")
