# Writing Readable Code: Coding Style Guides

[Part 1 - Introduction](wrc_python_style_guides_1_intro.md)

[Part 2 - Pep8 Specifics](wrc_python_style_guides_2_pep8_specifics.md)

[Part 3 - Pep8 Exercise](wrc_python_style_guides_3_pep8_exercise.md)

[Part 4 - Automatic Style Checking](#automatic-style-checking)

## Automatic Style Checking

So far, we've been checking code for pep8 compliance manually, by examining the code ourselves. However, tools exist to automate at least part of these checks.

### pycodestyle

Today we'll use the command line tool [pycodestyle](https://github.com/PyCQA/pycodestyle) to do this.

#### 👥 Small Group Activity
In the command line, run `pycodestyle` on the original version of the pep8 exercise from earlier.
['code_exercises/wrc_pep8_exercise.py']('../../code_exercises/wrc_pep8_exercise.py')

```bash
pycodestyle wrc_pep8_exercise.py
```

You should see a big list of errors.

Do these errors correspond with the ones you found yourselves? Which are the same and which are different?

Note that we haven't discussed every pep8 guideline so there may be some which we haven't covered.

Now run `pycodestyle` again on your corrected version of the code. Did you miss any errors?

It's likely that the tool picked up some errors which you missed and vice versa.

Automated checkers like this are extremely useful for finding style errors in your code. However, they can't always catch everything.

#### 💬 Class Discussion
What types of errors could not be found automatically?

It's also possible that you or your group have decided to ignore certain types of errors or to follow a different convention in some cases. You can set up the tool to ignore certain types of error, or certain files.

### Online Style Checkers
You can also check if your code is pep8 compliant by pasting it into various online tools.
One example is [pep8online.com](http://pep8online.com/)
These tools have the same benefits and limitations as using pycodecheck.

### IDE Style Checkers
Many Python development environments include tools to check code for compliance with a style guide.

In PyCharm, pep8 errors are found by default when running `Code --> Inspect Code...`.

![pep8 coding style violation]("../../figures/wrc_pep8_1.PNG")
![pep8 naming convention violation]("../../figures/wrc_pep8_2.PNG")

In general, it is best to use automated tools to reduce your workload in checking the style of your code, but to also try to stick to the style guide while writing the code rather than correcting it at the end.


Further Reading
[How to Write Beautiful Python Code With PEP 8](https://realpython.com/python-pep8/)

[Why consistency is important](https://blog.devgenius.io/why-code-consistency-is-important-9d95bdebcef4)

[The three levels of code consistency](https://css-tricks.com/write-better-code-3-levels-code-consistency/)

[Why coding style matters](https://www.smashingmagazine.com/2012/10/why-coding-style-matters/)



