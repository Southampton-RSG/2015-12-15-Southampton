---
layout: page
title: Building programs with Python
subtitle: Creating Functions
minutes: 20
---
> ## Learning Objectives {.objectives}
>
> *   Define a function that takes parameters.
> *   Return a value from a function.
> *   Documenting a function
> *   Set default values for function parameters.
> *   Explain why we should divide programs into small, single-purpose functions.

<!--
At this point,
we've written code to draw some interesting features in our inflammation data,
loop over all our data files to quickly draw these plots for each of them,
and have Python makes decisions based on what it sees in our data.
But, our code is getting pretty long and complicated;
what if we had thousands of datasets,
and didn't want to generate a figure for every single one?
Commenting out the figure-drawing code is a nuisance.
-->
Also, what if we want to use that code again,
on a different dataset or at a different point in our program?
Cutting and pasting it is going to make our code get very long and very repetitive,
very quickly.
We'd like a way to package our code so that it is easier to reuse,
and Python provides for this by letting us define things called 'functions' -
a shorthand way of re-executing longer pieces of code.

Let's start by defining a function `fahr_to_kelvin` that converts temperatures from Fahrenheit to Kelvin:

~~~ {.python}
def fahr_to_kelvin(temp):
    return ((temp - 32) * (5/9)) + 273.15
~~~

The definition opens with the word `def`,
which is followed by the name of the function
and a parenthesized list of parameter names.
The [body](../../reference.html#function-body) of the function --- the
statements that are executed when it runs --- is indented below the definition line,
typically by four spaces.

When we call the function,
the values we pass to it are assigned to those variables
so that we can use them inside the function.
Inside the function,
we use a [return statement](../../reference.html#return-statement) to send a result back to whoever asked for it.

Let's try running our function.
Calling our own function is no different from calling any other function:

~~~ {.python}
print ("Freezing point of water: ", fahr_to_kelvin(32))
print ("Boiling point of water: ", fahr_to_kelvin(212))
~~~
~~~ {.output}
Freezing point of water: 273.15
Boiling point of water: 373.15
~~~

We've successfully called the function that we defined,
and we have access to the value that we returned.
The value returned looks right.


### Composing Functions

Now that we've seen how to turn Fahrenheit into Kelvin,
it's easy to turn Kelvin into Celsius:

~~~ {.python}
def kelvin_to_celsius(temp):
    return temp - 273.15

print ("Absolute zero in Celsius: ", kelvin_to_celsius(0))
~~~
~~~ {.output}
Absolute zero in Celsius: -273.15
~~~

What about converting Fahrenheit to Celsius?
We could write out the formula,
but we don't need to.
Instead,
we can [compose](../../reference.html#function-composition) the two functions we have already created:

~~~ {.python}
def fahr_to_celsius(temp):
    temp_k = fahr_to_kelvin(temp)
    result = kelvin_to_celsius(temp_k)
    return result

print ("Freezing point of water in Celsius: ", fahr_to_celsius(32))
~~~
~~~ {.output}
Freezing point of water in Celsius: 0.0
~~~

This is our first taste of how larger programs are built:
we define basic operations,
then combine them in ever-large chunks to get the effect we want.
Real-life functions will usually be larger than the ones shown here --- typically half a dozen to a few dozen lines --- but
they shouldn't ever be much longer than that,
or the next person who reads it won't be able to understand what's going on.

> ## Variables inside and outside functions {.challenge}
>
> What does the following piece of code display when run - and why?
>
> ~~~ {.python}
> f = 0
> k = 0
>
> def f2k(f):
>   k = ((f-32)*(5/9)) + 273.15
>   return k
>
> f2k(8)
> f2k(41)
> f2k(32)
>
> print(k)
> ~~~

> ## Combining strings {.challenge}
>
> "Adding" two strings produces their concatenation:
> `'a' + 'b'` is `'ab'`.
> Write a function called `fence` that takes two parameters called `original` and `wrapper`
> and returns a new string that has the wrapper character at the beginning and end of the original.
> A call to your function should look like this:
>
> ~~~ {.python}
> print(fence('name', '*'))
> *name*
> ~~~

> ## Palindrome String check {.challenge}
>
> A "Palindrome" is a word, phrase, number, or other sequence of characters which reads the same backward or forward.
>Write a function (any name of your choice) that takes `input_string` as a parameter
>and returns either `True` or `False` based on whether the input string is a palindrome or not respectively. 
>Try to make it case insensitive.  
>Following the function definition, a call to your function should look like this:
>
> ~~~{.python}
> is_palindrome("hello")
> False
> is_palindrome("Deed")
> True
> ~~~
