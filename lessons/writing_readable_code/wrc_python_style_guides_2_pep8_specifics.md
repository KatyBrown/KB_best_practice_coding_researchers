## PEP8

IIn Python, although we do have a choice of style guides available

The [PEP8](https://www.python.org/dev/peps/pep-0008/) style guide is most commonly used.

PEP here stands for Python Enhancement Proposals; PEPs are design documents for the Python community, typically  specifications or conventions for how to do something in Python, a description of a new feature in Python, etc.

A full list of style guidelines for pep8 is available from the [PEP8 website](https://www.python.org/dev/peps/pep-0008/); here we highlight a few.

### Pep8 Specifics

#### Indentation

Python uses indentation as a way of grouping statements that belong to a particular block of code.

    for i in range(5):
        j = i + 1
        print (j)
    print (i)

Output:

    1
    2
    3
    4
    5
    4

This is different to:

    for i in range(5):
        j = i + 1
        print (j)
        print (i)

Output:

    1
    0
    2
    1
    3
    2
    4
    3
    5
    4

And different to:

    for i in range(5):
        j = i + 1
    print (j)
    print (i)


Output:

    5
    4
This is essential in Python but there are different indentation styles.

**Whole Group Poll**

Do you indent using spaces or tabs?


Spaces are the recommended indentation method in Python. 
The guideline is to use 4 spaces per indentation level - so 4 spaces on level one, 8 spaces on level 2 and so on.

    def myloop():
        for i in range(10):
            j = i + 1
            print (j)
        print (i)


Many people prefer the use of tabs rather than spaces to indent the code for many
reasons (e.g. additional typing, easy to introduce an error by
missing a single space character, etc.) and do not follow this
guideline.

Whether you decide to follow this guideline or not,
be consistent and follow the style already used in the project.

**Python 3 disallows mixing the use of tabs and spaces for indentation.**

PyCharm and other Python editing tools have built-in support for 
converting tab indentation to spaces  in order to
conform to PEP8. So, you can type a tab character and PyCharm will
automatically convert it to 4 spaces.

You can also tell many editors to show non-printable characters
if you are ever unsure what character exactly is being used

e.g. in Pycharm by selecting `View`>`Active Editor`>`Show whitespace`.


#### Maximum Line Length
All lines should be up to 80 characters long, for lines containing comments or docstrings the line length limit should be 73. Some teams strongly prefer a longer line length, and seemed to have settled on the length of 100.

Long lines of code can be broken over multiple lines by wrapping expressions in brackets (preferred method), or using a backslash (`\`) at the end of the line to indicate line continuation (slightly less preferred method).

*Individual activity*

Use brackets () to wrap the following long lines of code.

    if my_first_variable > 1 or my_second_variable > 2 or my_third_variable > 3:
        my_new_variable = my_first_variable + my_second_variable + my_third_variable


Example solution:

    if (my_first_variable > 1
        or my_second_variable > 2
        or my_third_variable > 3):
            my_new_variable = (my_first_variable
                               + my_second_variable
                               + my_third_variable)


You can also use a backslash \ to split code over multiple lines (but it is best to avoid this if you can).

    if my_first_variable > 1 \
        or my_second_variable > 2 \
        or my_third_variable > 3:
            my_new_variable = my_first_variable\
                              + my_second_variable\
                              + my_third_variable

To separate a string over more than one line, you can enclose it in triple quotes - `"""string"""` or `'''string'''`

If you don't want to include the line break in the string, use a backslash \ inside quotes (single or triple)

    print ("""1. This code is broken up over
            more than one line""")

    print ("2. This code is all on \
    the same line")

Output:

    1. This code is broken up over
            more than one line
    2. This code is all on the same line


#### Blank Lines

Function and class definitions should be surrounded with two blank lines.

Method definitions inside a class should be surrounded by a single blank line.

You can use single blank lines in functions to indicate logical sections.

    def function1(x):
        print ("Function 1 is running")

        x += 1

    
    def function2(y):
        print ("Function 2 is running")

        y += 5
        
        

#### Whitespace in Expressions and Statements

The pep8 white space guidelines are fairly similar to how punctuation is used when writing text.

* There shouldn't be spaces between brackets () and the text they contain

**Poll**

Which of the following sentences is correctly punctuated
1. `Style guides (  such as pep8) are important.`

2. `Style guides (  such as pep8  ) are important.`

3. ` Style guides (such as pep8  ) are important.`

4. `Style guides (such as pep8) are important.`

Which of the following Python statements is correctly formatted?
1. `y = ( x / 2 ) + 1`
2. `y = (x / 2 ) + 1`
3. `y = ( x / 2) + 1`
4. `y = (x / 2) + 1`

* Commas , and colons : should have no spaces before, but one space after

1. `Style guides: annoying, but useful`
2. `Style guides : annoying , but useful`
3. `Style guides :annoying ,but useful`


1. 


    def myfun(x, y):
        print(y, x)

2.


    def myfun(x , y) :
        print(y , x)

3.


    def myfun(x ,y) :
        print (y ,x)

Other operators should have a space on either side (unless at the end of a line)

    x = x + 1
    if y == 2:
        print(y / 2)
    if x < 3:
        print (x / 3)

#### Trailing whitespace

There shouldn't be whitespace (spaces or tabs) on the end of a line or on blank lines

In many editors you can make whitespace visible to check this
e.g. in Pycharm by selecting `View`>`Active Editor`>`Show whitespace`.

#### Naming conventions
The main thing to think about when naming a variable or a function is whether the name is useful to you. Many of the example functions in this tutorial have terrible names, it is better to use a descriptive name than x, y, my_var, my_function, function1 etc.

There are various conventions used for naming variables and functions.
* lowercase
* lower_case_with_underscores
* UPPERCASE
* UPPER_CASE_WITH_UNDERSCORES
* CapitalizedWords
* mixedCase
* Capitalized_Words_With_Underscores

Under the pep8 guidelines all function and variable names should use the lower_case_with_underscores convention. 
