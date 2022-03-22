#!/usr/bin/env python3
"""
The code below defines a new class "FLUFFYDOG" and three functions.
These functions:
    * Check how many words are in the dog's name
    * Check the name for whitespace
    * Check the name for punctuation
The result of running each function is printed to the screen.

The code works but it contains a number of pep8, style and consistency issues.
Try to find and correct these issues. Don't worry about improving the comments
or docstrings, they are just to explain how the code works. For this exercise
there's also no need to improve how the code functions, except to make it
consistent.

Corrected code is available as wrc_pep8_exercise_corrected.py but your
answer may differ. All of the changes made are listed in
wrc_pep8_exercise_corrected.py
"""
class FLUFFYDOG:
    """
    Class defining what a "fluffy dog" is
    """
    def __init__(self, xx, yy):
        """
        Generate a new dog object with a name and breed
        """

        # Name of the dog
        self.name=xx
        # Breed of the dog
        self.breed = yy

def chname(my_dog):
    """
    Check how many words are in the dog's name
    """


    NNN= my_dog.name
    import re
    x = re.split(" " , NNN )
    l=len(x)
    print  ("Dog "+my_dog.name + " is a " +   my_dog.breed + " and their name has "+ str(l) +" words")

def ws(D):
    """Check if there is any whitespace in the dog's name"""


    # Make a list of all the whitespace characters from the 'string' package
    p = list(whitespace)
    i = 0
    for pp in p:
      import re
      if re.search(pp, D.name) :
        i = i + 1
    if i != 0:
     print ("There is whitespace in the name " + D.name)
    else:
        print ("There is no whitespace in the name " + D.name)



def FINDPUNCT(dogname):
    """
    Check if there is any punctuation in the dog's name
    """
    # Make a list of all the punctuation characters from the 'string' package
    import string
    p = string.punctuation.split()
    i = 0
    for pp in p:
        if pp in dogname:
            i += 1
    if i <1:

        print ("There is no punctuation in the name "+dogname)
    else:
     print ("There is punctuation in the name " + dogname)

ddd=FLUFFYDOG('Mr Bones' , 'poodle')
chname(ddd)
from string import *
ws(ddd)

FINDPUNCT(ddd.name)

