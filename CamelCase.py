"""
Lab1Q3 - Justin Third - 8/23/2023
Create a MIPO application to validate and test a variable to ensure it does not contain invalid special characters
Assuming _ and - are NOT accepted
    RESOURCES
    1 = https://automatetheboringstuff.com/2e/chapter7/
    2 = https://stackoverflow.com/questions/29334276/capitalize-first-letter-of-the-first-word-in-a-list-in-python
    3 = https://www.digitalocean.com/community/tutorials/python-join-list
"""

import re

# Define a main function to run the core code
def main():
    # Utilize builtin input to store the variable name for validating
    variable = input(f'Please enter a variable name for validation and formatting: ')

    # Utilize a tuple to collect two returns from the text variable function
    numExists, specCharExists = testVariable(variable)

    # while a number occupies the first spaces or special characters are included
    while specCharExists or numExists:
        # Ask the user to try again
        variable = input(f'Variables should not begin with a number! Do not include any special '
                         f'characters! ("!@#$%^&*()-+?_=,<>\\/[]\')\n'
                         f'Please enter a variable name for validation and formatting: ')
        # Test the new variable for a valid entry
        numExists, specCharExists = testVariable(variable)

    # Once a correct variable is entered, seperate at the spaces
    wordSplitVariable = variable.split(" ")

    # create a variable to hold the corrected words
    correctedWords = []

    # Loop through each word in the split sentence
    for word in wordSplitVariable:  # 2
        if word == wordSplitVariable[0]:
            # Lowercase the first word
            word = word.lower()
            correctedWords.append(word)
        else:
            # Everything else is capitalized
            word = word.capitalize()
            correctedWords.append(word)

    # Display the corrected words joined neatly
    print("".join(correctedWords))  # 3


# define a tool that can be repetitively called to validate user entry
def testVariable(userInput):
    # Look for 1 or more digits at the biggining of the entry
    numStartRegex = re.compile(r'^(\d)+')  # 1
    numExists = numStartRegex.search(userInput)  # 1

    # Look for any special characters period
    specialCharRegex = re.compile(r'["!@#$%^&*()\-+?_=,<>/\\\[\]\']')
    specCharExists = specialCharRegex.search(userInput)

    # Return the matches or "None" Types
    return numExists, specCharExists

# Run the main program
main()
