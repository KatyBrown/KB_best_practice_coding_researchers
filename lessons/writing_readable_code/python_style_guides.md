## Introduction

Coding style conventions help you to to make sure that your code is consistently formatted and readable by yourself and others.



## Python Coding Style Guide
One of the most important things we can do to make sure our code is readable by others (and ourselves a few months down the line) is to make sure that it is descriptive, cleanly and consistently formatted and uses sensible, descriptive names for variable, function and module names. 

In order to help us format our code, we generally follow guidelines known as a **style guide**. A style guide is a set of conventions that we agree upon with our colleagues or community, to ensure that everyone contributing to the same project is producing code which looks similar in style.


While a group of developers may choose the write and agree upon a new style guide unique to each project, in practice many programming languages have a single style guide which is adopted almost universally by the communities around the world. In Python, although we do have a choice of style guides available, the [PEP8](https://www.python.org/dev/peps/pep-0008/) style guide is most commonly used.

PEP here stands for Python Enhancement Proposals; PEPs are design documents for the Python community, typically  specifications or conventions for how to do something in Python, a description of a new feature in Python, etc.

## Style consistency
Code is read much more often than it is written. Style guidelines are intended to improve the readability of code and make it consistent across the wide spectrum of Python code.

Consistency with the style guide is important. Consistency within a project is more important. Consistency within one module or function is the most important. However, know when to be inconsistent - sometimes style guide recommendations just are not applicable. When in doubt, use your best judgment.

For example

[Code snippet 1](\../../code_snippets/wrc_python_style_guides_example1_bad.py)

	q=' ' 
	x='\n'
	def f(s1,s2):
	 s3=str(s1)
	 s4=str(s2)
	 
	 
	 
	 s11=s2/s1
	 s12=round(s11,2)
	 s11=str(s12)
	 print('number of entries ='+q+s3+x+'number of winners='+q+s4+x+'% success ='+q+s11)

	r=12
	r1=5

	f(r, r1)



Output:

	number of entries = 12
	number of winners= 5
	% success = 0.41

[Code snippet 2](\../../code_snippets/wrc_python_style_guides_example1_better.py)

	def print_values(n_entries, n_winners):
	    '''
	    Print the number of entries and winners and calculate and print
	    the probability of success.
	    '''
	    print ('number of entries = %i' % (n_entries))
	    print ('number of winners = %i' % (n_winners))
	    print ("%% success = %.2f" % (n_winners / n_entries))


	entries = 12
	winners = 5
	print_values(entries, winners)

Output:

	number of entries = 12
	number of winners= 5
	% success = 0.42

Code snippets 1 and 2 produce exactly the same output, but it is much easier to read snippet 2 and to understand what the programmer was trying to do.


A full list of style guidelines for pep8 is available from the [PEP8 website](https://www.python.org/dev/peps/pep-0008/); here we highlight a few.

### Indentation

Python uses indentation as a way of grouping statements that belong to a particular block of code. Spaces are the recommended indentation method in Python code. The guideline is to use 4 spaces per indentation level - so 4 spaces on level one, 8 spaces on level 2 and so on.

Many people prefer the use of tabs to spaces to indent the code for many reasons (e.g. additional typing, easy to ntroduce an error by missing a single space character, etc.) and do not follow this guideline. Whether you decide to follow this guideline or not, be consistent and follow the style already used in the project.

Python 3 disallows mixing the use of tabs and spaces for indentation.


PyCharm and other Python editing tools have built-in support for converting tab indentation to spaces "under the hood" for Python code in order to
conform to PEP8. So, you can type a tab character and PyCharm will automatically convert it to 4 spaces.

You can also tell many editors to show non-printable characters if you are ever unsure what character exactly is being used, e.g. in Pycharm by selecting `View`>`Active Editor`>`Show whitespace`.


### Maximum Line Length
All lines should be up to 80 characters long; for lines containing comments or docstrings (to be covered later) the
line length limit should be 73 - see [this discussion](https://www.google.com/url?q=https://stackoverflow.com/questions/15438326/python-pep-8-docstring-line-length&sa=D&source=editors&ust=1619088968027000&usg=AOvVaw3jn26Qt-kwog_tJnaMR48x) for reasoning behind these numbers. 

Some teams strongly prefer a longer line length, and seemed to have settled on the length of 100. Long lines of code can be broken over multiple lines by wrapping expressions in delimiters, as mentioned above (preferred method), or using a backslash (`\`) at the end of the line to indicate line continuation (slightly less preferred method).

Using delimiters ( ) to wrap a multi-line expression:

	if (a == True and
	    b == False):


Using a backslash (\) for line continuation

	if a == True and \
	    b == False:



### Should a Line Break Before or After a Binary Operator?
Lines should break before binary operators so that the operators do not get scattered across different columns on the screen. In the example below, the eye does not have to do the extra work to tell which items are added and which are subtracted:

PEP 8 compliant - easy to match operators with operands

	income = (gross_wages
		  + taxable_interest
		  + (dividends - qualified_dividends)
		  - ira_deduction
		  - student_loan_interest)


### Blank Lines
Top-level function and class definitions should be surrounded with two blank lines. Method definitions inside a class should be surrounded by a single blank line. You can use single blank lines in functions to indicate logical sections.

### Whitespace in Expressions and Statements

Avoid extraneous whitespace in the following situations:

1 . Immediately inside parentheses, brackets or braces

PEP 8 compliant:

    my_function(colour[1], {id: 2})


Not PEP 8 compliant:

    my_function( colour[ 1 ], { id: 2 } )


2. Immediately before a comma, semicolon, or colon (unless doing slicing where the colon acts like a binary operator
in which case it should should have equal amounts of whitespace on either side)


