#!/usr/bin/env python3
#  !Moved imports to the top of the file
import string
import re


#  !Added two blank lines before class definition
#  !Changed class name to CapitalisedWord convention
class FluffyDog:
    """
    Class defining what a "fluffy dog" is
    """
    #  !Changed variable names to be more informative
    def __init__(self, name, breed):
        """
        Generate a new dog object with a name and breed
        """
        # !Removed empty line
        # Name of the dog
        # !Added spaces around "="
        self.name = name
        # Breed of the dog
        self.breed = breed


# !Added two blank lines before function definition
# !Changed function name to be informative and to use the lower case with
# !underscores convention
# !Changed argument name to be consistent with the other functions
def count_words_in_name(dog):
    """
    Check how many words are in the dog's name
    """
    # !Removed blank lines
    # !Changed variable name to lowercase with underscores and used an
    # !informative name
    dog_name = dog.name
    # !Moved import statement to top
    # !Removed extra spaces around comma and brackets
    # !Changed variable name to lowercase with underscores and used an
    # !informative name
    name_sections = re.split(" ", dog_name)
    # !Changed variable name to lowercase with underscores and used an
    # !informative name
    # !Added spaces around "=" sign
    name_length = len(name_sections)
    # !Removed spaces before brackets and added one space on either side of
    # !each plus sign
    # !Used existing variables where possible
    # !Split the long line over two lines
    print("Dog " + dog_name + " is a " + dog.breed
          + " and their name has " + str(name_length) + " words")


# !Added two blank lines before function definition
# !Gave function an informative name in the lowercase with underscores style
# !Changed argument name to be consistent with the other functions
def check_name_whitespace(dog):
    """
    Check if there is any whitespace in the dog's name
    """
    # !Removed blank lines
    # !Changed variable name to be informative and use lowercase with
    # !underscores style
    # !Changed wildcard import (import * from string) to "import string" and
    # !moved to top of file

    ws_chars = list(string.whitespace)
    # !Changed variable to an informative name
    count_ws = 0
    # !Changed variable to an informative name
    # !Moved import to top of file
    # !Removed space before :
    # !Changed i = i + 1 to i += 1 to be consistent with the
    # !check_name_punctuation function
    # !Changed to four space indent
    # !Changed method used for search to match the
    # !check_name_punctuation function
    for ws_char in ws_chars:
        if ws_char in dog.name:
            count_ws += 1
    # !Removed unneeded not
    if count_ws == 0:
        # ! Removed whitespace after print function
        # ! Changed to four space indent
        print("There is no whitespace in the name " + dog.name)
    else:
        # ! Removed whitespace after print function
        print("There is whitespace in the name " + dog.name)


# !Removed excess blank lines
# !Gave function an informative name in the lowercase with underscores style
# !Gave function a name consistent with the other functions
# !Changed argument name to be consistent with the other functions
# !Changed to use dog object rather than dog.name attribute to be consistent
# !with other functions
def check_name_punctuation(dog):
    """
    Check if there is any punctuation in the dog's name
    """
    # !Moved import to top of file
    # !Changed function used to convert to a list to be consistent with
    # !the check_name_whitespace

    punc_chars = list(string.punctuation)
    # !Changed variable to an informative name
    count_punc = 0

    for punc_char in punc_chars:
        if punc_char in dog.name:
            count_punc += 1
    # !Changed functionality to match the check_name_whitespace function
    # !Changed to four space indent
    # !Reversed order to match the check_name_whitespace function
    # !Added one space on either side of "+" character
    # !Removed whitespace before bracket after print
    if count_punc == 0:
        print("There is no punctuation in the name " + dog.name)
    else:
        print("There is punctuation in the name " + dog.name)


# !Changed variable name to be informative and use the lowercase with
# !underscores style
# !Added names to arguments
# Removed excess blank lines
# !Moved import statement to top of file
dog_mr_bones = FluffyDog(name='Mr Bones', breed='poodle')
count_words_in_name(dog_mr_bones)
check_name_whitespace(dog_mr_bones)
check_name_punctuation(dog_mr_bones)
