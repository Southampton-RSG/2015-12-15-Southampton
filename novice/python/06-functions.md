---
layout: page
title: Building programs with Python
subtitle: Modularising your code using functions
minutes: 15
---
> ## Learning Objectives {.objectives}
>
> *   

### Converting from Fahrenheit to Celsius

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

