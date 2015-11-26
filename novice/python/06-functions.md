---
layout: page
title: Building programs with Python
subtitle: Modularising your code using functions
minutes: 15
---
> ## Learning Objectives {.objectives}
>
> *   Define a function that takes parameters.
> *   Return a value from a function.
> *   Documenting a function.
> *   Understand why we should divide programs into small, single-purpose 
>     functions.
> *   Define and use a module that contains functions.

At this point, we've written some scripts to do various things, including one to 
loop through a data file and output its contents.
But it's not hard to imagine our code getting more complicated as we add
more features.

We'll see how we can amend our code to be better structured to further increase its readability, as well as its maintainability and reuse in other applications.

### Converting from Fahrenheit to Celsius

Let's look at adding a feature to our code to perform a conversion 
from Fahrenheit to Celsius on the temperature data we are looking at:

~~~ {.python}
celsius = ((data[3] - 32) * (5/9))
~~~

Now this wouldn't work as it is - we can't just apply this formula directly to 
`data[3]` since it's a string. We need to convert it to a number first. To be 
specific, a floating point number.

Fortunately, Python has some built-in functions to do conversions:

~~~ {.python}
climate_data = open('../data/sc_climate_data_10.csv', 'r')

for line in climate_data:
    data = line.split(',')

    if data[0][0] == '#':
        # don't want to process comment lines, which start with '#'
        pass
    else:
        # extract our max temperature in Fahrenheit - 4th column
        fahr = float(data[3])

        # apply standard fahrenheit to Celsius formula
        celsius = ((fahr - 32) * (5/9)) 

        print('Max temperature in Celsius', celsius)
~~~

So we first convert our `data[3]` value to a floating point number using 
`float()`, then we are free to use it in our conversion formula. Depending on 
the structure of your own data, you may find you end up doing this a lot!

So now we get:

~~~
Max temperature in Celsius 14.73888888888889
Max temperature in Celsius 14.777777777777779
Max temperature in Celsius 14.61111111111111
Max temperature in Celsius 13.838888888888887
Max temperature in Celsius 15.477777777777778
Max temperature in Celsius 14.972222222222225
Max temperature in Celsius 14.85
Max temperature in Celsius 16.33888888888889
Max temperature in Celsius 16.261111111111113
Max temperature in Celsius 16.33888888888889
~~~

### Modularising conversion code into a function

~~~ {.python}
climate_data = open('../data/sc_climate_data_10.csv', 'r')

def fahr_to_celsius(fahr):
    # apply standard fahrenheit to Celsius formula
    celsius = ((fahr - 32) * (5/9)) 
    return celsius

for line in climate_data:
    data = line.split(',')

    if data[0][0] == '#':
        # don't want to process comment lines, which start with '#'
        pass
    else:
        # extract our max temperature in Fahrenheit - 4th column
        fahr = float(data[3])

        celsius = fahr_to_celsius(fahr)

        print('Max temperature in Celsius', celsius)
~~~

And when we run it again --- which we most definitely should, to make sure it's still working as expected --- we see the same output, which is correct.


### Modularising conversion code into a library

~~~ {.python}
"""A library to perform temperature conversions"""

def fahr_to_celsius(fahr):
    """Convert Fahrenheit to Celsius.

    Uses standard fahrenheit to Celsius formula

    Arguments:
    fahr -- the temperature in Fahrenheit
    """
    celsius = ((fahr - 32) * (5/9)) 
    return celsius
~~~

When modules and functions are described in Docstrings, we can ask for these explanations directly from the interpreter, which is very useful:

~~~ {.python}
Python 3.4.3 |Anaconda 2.3.0 (x86_64)| (default, Mar  6 2015, 12:07:41) 
[GCC 4.2.1 (Apple Inc. build 5577)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import temp_conversion
>>> help(temp_conversion)
~~~

~~~
Help on module temp_conversion:

NAME
    temp_conversion - A library to perform temperature conversions

FUNCTIONS
    fahr_to_celsius(fahr)
        Convert Fahrenheit to Celsius.
        
        Uses standard fahrenheit to Celsius formula
        
        Arguments:
        fahr -- the temperature in Fahrenheit

FILE
    /Users/user/Projects/RSG/Training/2015-12-15-Southampton/novice/python/code/temp_conversion.py
~~~

~~~ {.python}
>>> help(temp_conversion.fahr_to_celsius)
~~~

~~~
Help on function fahr_to_celsius in module temp_conversion:

fahr_to_celsius(fahr)
    Convert Fahrenheit to Celsius.
    
    Uses standard fahrenheit to Celsius formula
    
    Arguments:
    fahr -- the temperature in Fahrenheit
~~~

And then we need to `import` that function from our module into our script, so we can use it.

~~~ {.python}
from temp_conversion import fahr_to_celsius

climate_data = open('../data/sc_climate_data_10.csv', 'r')

for line in climate_data:
    data = line.split(',')

    if data[0][0] == '#':
        # don't want to process comment lines, which start with '#'
        pass
    else:
        # extract our max temperature in Fahrenheit - 4th column
        fahr = float(data[3])

        celsius = fahr_to_celsius(fahr)

        print('Max temperature in Celsius', celsius)
~~~

Again, the results should be the same as before.

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

