# Writing Readable Code: Coding Style Guides
An introduction to Python style guides and why and how they are used, using the pep8 style guide as an example.

**Learning outcomes**
* Understanding of why style guides and coding conventions are important
* Familiarity with programming style guides and how and why they are used, focussed on the pep8 Python style guide
* Familiarity with naming conventions 
* Ability to format a piece of code to meet the pep8 specifications 
* Awareness of tools which check if code meets specifications


[Part 1 - Introduction](#why-use-a-coding-style-guide)

[Part 2 - Pep8 Specifics](wrc_python_style_guides_2_pep8_specifics.md)

[Part 3 - Pep8 Exercise](wrc_python_style_guides_3_pep8_exercise.md)

[Part 4 - Automatic Style Checking](wrc_python_style_guides_4_automatic_checking.md)

[Part 5 - Further Reading](wrc_python_style_guides_5_further_reading.md)

## Why use a coding style guide?

Coding style conventions help you to make sure that your code is consistently formatted and readable by yourself and others.


#### 💬 Class Discussion

When you are trying to understand a piece of code, what do you find makes it easier or more difficult?


#### 👥 Small Group Activity

The following two code snippets produce the same output. Which is more readable? Which features make one snippet more readable than the other?

[Code snippet](../../code_snippets/wrc_python_style_guides_example1_bad.py)
```python
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
```


Output:

	number of entries = 12
	number of winners= 5
	% success = 0.41

[Code snippet](../../code_snippets/wrc_python_style_guides_example1_better.py)
```python
def print_values(n_entries, n_winners):
    """
    Print the number of entries and winners and calculate and print
    the probability of success.
    """
    print('number of entries = %i' % n_entries)
    print('number of winners = %i' % n_winners)
    print("%% success = %.2f" % n_winners / n_entries)


entries = 12
winners = 5
print_values(entries, winners)

```

Output:

	number of entries = 12
	number of winners= 5
	% success = 0.42
&nbsp;


<details>
    <summary>
        Solution
    </summary>
&nbsp;


Code snippets 1 and 2 produce exactly the same output, but it is much easier to read snippet 2 and to understand what the programmer was trying to do.

* Snippet 2 has some documentation
* Variable names and function name are more informative in snippet 2
* Bigger indents in snippet 2
* All the variables used inside the function are provided as arguments
* Strings are formatted more clearly
&nbsp;


</details>

## Style Guides

There are guidelines available to format code in different languages known as **style guides**. 


Code is read much more often than it is written. Style guidelines are intended to improve the readability of code and make it consistent across the wide spectrum of Python code.


A style guide is a set of conventions agreed upon by a group or community to ensure that all the code produced by the group is similar in style.  It is similar to using correct grammar, spelling and punctuation when writing prose - it's usually not essential, but it can make things clearer, more accessible and more professional.


## Style consistency


#### 💬 Class Discussion

What will be the output for `print (a)`, `print (b)` and `print(c())` in the code snippet below?

[Code snippet](../../code_snippets/wrc_style_consistency.py)
```python
a = list()
a.append(1)
a.extend([2, 3])

b = []
b = b + [1]
b += [2, 3]

def c():
    return [1, 2, 3]

print(a)
print (b)
print (c())
```

Using a consistent style:
* Makes it quicker and easier to understand your code
* Makes it easier to find and fix mistakes
* Saves "mental energy" when reading the code
* Makes others more likely to use and develop your code


#### 💬 Class Discussion

Put the following in order of importance

- Code within a module or function should have a consistent style
- Code should be consistent with a style guide
- Code within a project should use a consistent style 
&nbsp;
  
  
<details>
    <summary>
        Solution
    </summary>

1. Code within a module or function should have a consistent style


2. Code within a project should use a consistent style


3. Code should be consistent with a style guide 

</details>
&nbsp;


Different groups use different style guides and project or group specific guidelines should take precedent over the pep8 conventions.

[Part 2: Pep8 Specifics](wrc_python_style_guides_2_pep8_specifics.md)


*Lesson adapted from: https://github.com/carpentries-incubator/python-intermediate-development/blob/gh-pages/_episodes/15-coding-conventions.md*