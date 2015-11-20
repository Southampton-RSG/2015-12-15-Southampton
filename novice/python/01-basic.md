---
layout: page
title: Building programs with Python
subtitle: Python Basics - Running the Python interpreter, Variables
minutes: 15
---
> ## Learning Objectives {.objectives}
>
> *   Running the Python interpreter
> *   Introduction to Python variables
> *   Creating and Assigning values to variables

## Running the Python interpreter

Normally, you write Python programs in a Python script, which is basically a file of Python commands you can run.
But to start with, we'll take a look at the Python interpreter.
It's similar to the shell in how it works, in that you type in commands and it
gives you results back, but instead you use the Python language.

It's a really quick and convenient way to get started with Python, particularly when learning about things like how to use variables, and it's good for playing around with what you can do and quickly testing small things.
But as you progress to more interesting and complex things you need to move over to writing proper Python scripts, which we'll see later.

You start the Python interpreter from the shell by:

~~~ {.bash}
$ python
~~~

And then you are presented with something like:

~~~ {.output}
Python 3.4.3 |Anaconda 2.3.0 (x86_64)| (default, Mar  6 2015, 12:07:41) 
[GCC 4.2.1 (Apple Inc. build 5577)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
~~~

And lo and behold! You are presented with yet another prompt.
So, we're actually running a Python interpreter from the shell - it's only yet another program we can run from the shell after all.
But shell commands won't work again until we exit the interpreter.

You can exit the interpreter and get back to the shell by typing:

~~~ {.python}
>>> exit()
~~~

...or alternatively pressing the Control and D keys at the same time.
Then you'll see:

~~~ {.output}
$ 
~~~

Phew - back to the shell!

But let's get back to the Python interpreter and learn about variables in Python:

~~~ {.bash}
$ python
~~~

And we're back to the Python interpreter:

~~~ {.output}
Python 3.4.3 |Anaconda 2.3.0 (x86_64)| (default, Mar  6 2015, 12:07:41) 
[GCC 4.2.1 (Apple Inc. build 5577)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
~~~

So from now on, Python only! Let's get started...

## Variables

A variable is just a name for a value,
such as `x`, `current_temperature`, or `subject_id`.
Python's variables must begin with a letter.
A variable in Python is defined through assignment i.e. we can create a new variable simply by assigning a value to it using `=`.
As an illustration,
consider the simplest `collection` of data,
a single value.
The line below assigns a value to a variable:

~~~ {.python}
weight_kg = 55
~~~

Once a variable has a value, we can print it:

~~~ {.python}
print(weight_kg)
~~~
~~~ {.output}
55
~~~

and do arithmetic with it:

~~~ {.python}
print('weight in pounds:', 2.2 * weight_kg)
~~~
~~~ {.output}
weight in pounds: 121.0
~~~

In the above example, a floating point number `55` object has a tag labelled `weight_kg`.

If we reassign to `weight_kg`, we just move the tag to another object as shown below.
 
We can change a variable's value by assigning it a new one:

~~~ {.python}
weight_kg = 57.5
print('weight in kilograms is now:', weight_kg)
~~~
~~~ {.output}
weight in kilograms is now: 57.5
~~~

Now the name `weight_kg` is attached to another floating point number `57.5` object.

Hence, in Python, a `name` or `identifier` or `variable` is like a name tag attached to an object.
Python has `names` and everything is an `object`.

As the example above shows,
we can print several things at once by separating them with commas.

If we imagine the variable as a sticky note with a name written on it,
assignment is like putting the sticky note on a particular value:

![Variables as Sticky Notes](img/python-sticky-note-variables-01.svg)

This means that assigning a value to one variable does *not* change the values of other variables.
For example,
let's store the subject's weight in pounds in a variable:

~~~ {.python}
weight_lb = 2.2 * weight_kg
print('weight in kilograms:', weight_kg, 'and in pounds:', weight_lb)
~~~
~~~ {.output}
weight in kilograms: 57.5 and in pounds: 126.5
~~~

![Creating Another Variable](img/python-sticky-note-variables-02.svg)

and then change `weight_kg`:

~~~ {.python}
weight_kg = 100.0
print('weight in kilograms is now:', weight_kg, 'and weight in pounds is still:', weight_lb)
~~~
~~~ {.output}
weight in kilograms is now: 100.0 and weight in pounds is still: 126.5
~~~

![Updating a Variable](img/python-sticky-note-variables-03.svg)

Since `weight_lb` doesn't remember where its value came from,
it isn't automatically updated when `weight_kg` changes.
This is different from the way spreadsheets work.

Although we commonly refer to `variables` even in Python (because it is the common terminology), we really mean `names` or `identifiers`. In Python, `variables` are name tags for values, not labelled boxes.


> ## What's inside the box? {.challenge}
>
> Draw diagrams showing what variables refer to what values after each statement in the following program:
>
> ~~~ {.python}
> weight = 70.5
> age = 35
> # Take a trip to the planet Neptune
> weight = weight * 1.14
> age = age + 20
> ~~~

> ## Sorting out references {.challenge}
>
> What does the following program print out?
>
> ~~~ {.python}
> first, second = 'Grace', 'Hopper'
> ~~~
>
> ~~~{.output}
> first = Grace
> second = Hopper
> ~~~
>
> ~~~{.python}
> third, fourth = second, first
> print(third, fourth)
> ~~~


