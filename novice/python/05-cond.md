---
layout: page
title: Building programs with Python
subtitle: Making choices
minutes: 15
---
> ## Learning Objectives {.objectives}
>
> *   Write conditional statements including `if`, `elif`, and `else` branches.
> *   Evaluate expressions containing `and` and `or`.
> *   Use conditionals to conditionally process input data.

So what if we want to do something that's dependent on whether a given condition is true? In this lesson, we'll learn how to write code that runs only when certain conditions are true.

## Conditionals

We can ask Python to take different actions, depending on a condition, with an if statement:

~~~ {.python}
num = 37
if num > 100:
    print("greater")
else:
    print("not greater")
print("done")
~~~
~~~ {.output}
not greater
done
~~~

The second line of this code uses the keyword `if` to tell Python that we want to make a choice.
If the test that follows it is true,
the body of the `if`
(i.e., the lines indented underneath it) are executed.
If the test is false,
the body of the `else` is executed instead.
Only one or the other is ever executed:

![Executing a Conditional](img/python-flowchart-conditional.svg)

Conditional statements don't have to necessarily include an `else`.
If there isn't one,
Python simply does nothing if the test is false:

~~~ {.python}
num = 53
print("before conditional...")
if num > 100:
    print("53 is greater than 100")
print("...after conditional")
~~~
~~~ {.output}
before conditional...
...after conditional
~~~

We can also chain several tests together using `elif`,
which is short for "else if" as shown in the example code chunk below:

~~~ {.python}
num = -3
    if num > 0:
        print("Sign of a number:",num,"is:",1)
    elif num == 0:
        print("Sign of a number",num,"is:",0)
    else:
        print("Sign of a number",num, "is:",-1)

~~~
~~~ {.output}
sign of a number -3 is:  -1
~~~

The keyword `elif` is short for `else if`, and is useful to avoid excessive indentation. An 
`if ... elif ... elif ...` sequence is a substitute for the `switch` or `case` statements 
found in other languages.

One important thing to notice in the code above is that we use a double equals sign `==` to test for equality
rather than a single equals sign
because the latter is used to mean assignment.
This convention was inherited from C,
and while many other programming languages work the same way,
it does take a bit of getting used to...

We can also combine tests using `and` and `or`.
`and` is only true if both parts are true:

~~~ {.python}
if (1 > 0) and (-1 > 0):
    print("both parts are true")
else:
    print("one part is not true")
~~~
~~~ {.output}
one part is not true
~~~

while `or` is true if either part is true:

~~~ {.python}
if (1 < 0) or ('left' < 'right'):
    print("at least one test is true")
~~~
~~~ {.output}
at least one test is true
~~~

In this case,
"either" means "either or both", not "either one or the other but not both".

## Climate Analysis: adding a condition to avoid printing comments

We're still getting our column header at the top of our output, and perhaps
we don't want that. We need to able to check whether the line begins with
a '#' (which denotes a comment line), and if so, avoid printing it out.

So let's use an `if` statement to do that:

~~~ {.python}
climate_data = open('../data/sc_climate_data_10.csv', 'r')

for line in climate_data:
    data = line.split(',')

    if data[0][0] == '#':
        # don't want to process comment lines, which start with '#'
        pass
    else:
        # print 4th column (max temperature)
        print('Max temperature', data[3])
~~~

~~~
Max temperature 58.53
Max temperature 58.60
Max temperature 58.30
Max temperature 56.91
Max temperature 59.86
Max temperature 58.95
Max temperature 58.73
Max temperature 61.41
Max temperature 61.27
Max temperature 61.41
~~~