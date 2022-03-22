#!/usr/bin/env python3
import string
import re


class FluffyDog:
    """
    Class defining what a "fluffy dog" is
    """
    def __init__(self, name, breed):
        """
        Generate a new dog object with a name and breed
        """
        # Name of the dog
        self.name = name
        # Breed of the dog
        self.breed = breed


def count_words_in_name(dog):
    """
    Check how many words are in the dog's name
    """
    dog_name = dog.name
    name_sections = re.split(" ", dog_name)
    name_length = len(name_sections)
    print("Dog " + dog_name + " is a " + dog.breed
          + " and their name has " + str(name_length) + " words")


def check_name_whitespace(dog):
    """
    Check if there is any whitespace in the dog's name
    """
    # Make a list of all the whitespace characters from the 'string' package
    ws_chars = list(string.whitespace)
    count_ws = 0

    for ws_char in ws_chars:
        if ws_char in dog.name:
            count_ws += 1

    if count_ws == 0:
        print("There is no whitespace in the name " + dog.name)
    else:
        print("There is whitespace in the name " + dog.name)


def check_name_punctuation(dog):
    """
    Check if there is any punctuation in the dog's name
    """
    # Make a list of all the punctuation characters from the 'string' package
    punc_chars = list(string.punctuation)
    count_punc = 0

    for punc_char in punc_chars:
        if punc_char in dog.name:
            count_punc += 1

    if count_punc == 0:
        print("There is no punctuation in the name " + dog.name)
    else:
        print("There is punctuation in the name " + dog.name)


dog_mr_bones = FluffyDog(name='Mr Bones', breed='poodle')
count_words_in_name(dog_mr_bones)
check_name_whitespace(dog_mr_bones)
check_name_punctuation(dog_mr_bones)
