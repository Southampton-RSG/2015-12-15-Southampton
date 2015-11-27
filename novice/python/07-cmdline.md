---
layout: page
title: Building programs with Python
subtitle: Command-Line Programs
minutes: 10
---
> ## Learning Objectives {.objectives}
>
> *   Use the values of command-line arguments in a program.
> *   Handle flags and files separately in a command-line program.
> *   Read data from standard input in a program so that it can be used in a pipeline.

At some point we may want to use our program in a pipeline
or run it in a shell script to process thousands of data files. Our climate
data is a good example - we have a sample set of 10 rows for development,
but also a data file with 1000 rows. We may of course want to process many more.
In order to do that,
we need to make our programs work like other Unix command-line tools.

## Passing in the file to process as an argument

So perhaps the biggest limitation is that our script only deals with one
data file, which is **hardcoded** into the script. Like with functions, we'd
ideally want to be able to pass in the filename to process as a parameter. Then,
we can run the script on any data file we like.

Fortunately, Python can handle **command line arguments**, which are passed
to our script in the list `sys.argv[]` we we can use. This feature is provided 
by the Python standard `sys` library, so similarly to how we imported our 
temperature conversion functions, we need to import the `sys` library.

The first argument (`sys.argv[0]`) always contains the name of the script,
with the arguments passed in as `sys.argv[1]`, `sys.argv[2]`, etc.

So we can change our script to handle a filename argument:

~~~ {.python}
import sys
import temp_conversion

filename = sys.argv[1]

climate_data = open(filename, 'r')

for line in climate_data:
    data = line.split(',')

    if data[0][0] == '#':
        # don't want to process comment lines, which start with '#'
        pass
    else:
        # extract our max temperature in Fahrenheit - 4th column
        fahr = float(data[3])

        # don't process invalid temperature readings of -9999
        if fahr != -9999:
            celsius = temp_conversion.fahr_to_celsius(fahr)
            kelvin = temp_conversion.fahr_to_kelvin(fahr)

            print('Max temperature in Celsius', celsius, 'Kelvin', kelvin)
~~~

And if we run that from the shell, with 

~~~ {.bash}
$ python climate_analysis.py ../data/sc_climate_data_10.csv
~~~

So we pass in the filename as argument that gets picked up and used. Handy!
When we run it, we get the following (same as before):

~~~
Max temperature in Celsius 14.73888888888889 Kelvin 287.88888888888886
Max temperature in Celsius 14.777777777777779 Kelvin 287.92777777777775
Max temperature in Celsius 14.61111111111111 Kelvin 287.76111111111106
Max temperature in Celsius 13.838888888888887 Kelvin 286.9888888888889
Max temperature in Celsius 15.477777777777778 Kelvin 288.62777777777774
Max temperature in Celsius 14.972222222222225 Kelvin 288.1222222222222
Max temperature in Celsius 14.85 Kelvin 288.0
Max temperature in Celsius 16.33888888888889 Kelvin 289.4888888888889
Max temperature in Celsius 16.261111111111113 Kelvin 289.4111111111111
Max temperature in Celsius 16.33888888888889 Kelvin 289.4888888888889
~~~

## Running our script on other data files

But now we can run it on any file, for example:

~~~ {.bash}
$ python climate_analysis.py ../data/sc_climate_data_1000.csv
~~~

But wait!

~~~
Max temperature in Celsius 14.73888888888889 Kelvin 287.88888888888886
Max temperature in Celsius 14.777777777777779 Kelvin 287.92777777777775
Max temperature in Celsius 14.61111111111111 Kelvin 287.76111111111106
Max temperature in Celsius 13.838888888888887 Kelvin 286.9888888888889
Max temperature in Celsius 15.477777777777778 Kelvin 288.62777777777774
Max temperature in Celsius 14.972222222222225 Kelvin 288.1222222222222
Max temperature in Celsius 14.85 Kelvin 288.0
Max temperature in Celsius 16.33888888888889 Kelvin 289.4888888888889
Max temperature in Celsius 16.261111111111113 Kelvin 289.4111111111111
Max temperature in Celsius 16.33888888888889 Kelvin 289.4888888888889
Max temperature in Celsius -5572.777777777778 Kelvin -5299.627777777779
Max temperature in Celsius 16.077777777777776 Kelvin 289.22777777777776
...
~~~

What's this `-5572.777777777778`? If we look at our 
`sc_climate_data_1000.csv` file, we can see there are some maximum
temperature values of -9999. As it turns out, this value represents
an invalid temperature reading!

This is a consequence of dealing with real data, and sometimes we need
to be able to deal with anomalies such as this. In particular, we
should make sure we fully understand the data we are using, and what
it means. Otherwise, we run the risk of making assumptions and 
processing the data incorrectly.

In this case, we can fix our code by adding in a condition:

~~~ {.python}
        # don't process invalid temperature readings of -9999
        if fahr != -9999:
            celsius = temp_conversion.fahr_to_celsius(fahr)
            kelvin = temp_conversion.fahr_to_kelvin(fahr)

            print('Max temperature in Celsius', celsius, 'Kelvin', kelvin)
~~~

So in this special case, we ensure that we aren't processing these
invalid values. In practice, we'd also need to make sure that any
conclusions we may reach from processing the data in this way are
also still valid.

## Adding in a checks for the right number of arguments

But if we (or someone else) runs our script accidentally with no filename,
we get:

~~~
Traceback (most recent call last):
  File "climate_analysis.py", line 5, in <module>
    filename = sys.argv[1]
IndexError: list index out of range
~~~

Since our filename is reading from an element in `sys.argv` that isn't
present. This is not very helpful! To make it easier to diagnose
such problems, we can implement a simple check to ensure the right
number of arguments are given to our script.

Insert the following before the `filename` assignment:

~~~ {.python}
script = sys.argv[0]
assert len(sys.argv) == 2, script + ": requires filename"
~~~

Now when we run it with no arguments, we get:

~~~
Traceback (most recent call last):
  File "climate_analysis.py", line 5, in <module>
    assert len(sys.argv) == 2, script + ": requires filename"
AssertionError: climate_analysis.py: requires filename
~~~

More helpful! We could make this even more helpful by providing more 
information about the file that is required.

## Using our script in a pipeline

Currently, our script outputs some friendly text to show what the data
means. But when it comes to using it within a pipeline, where we might
process the output data in some way, the additional text may make this
more difficult.

Assuming we've documented our code properly and the nature of the output
is clearly understood, we can simplify the output by changing the
`print()` statement:

~~~ {.python}
            print(str(celsius)+", "+str(kelvin))
~~~

Here, we are using Python's `+` operator to **concatenate** strings 
together, so we can get output such as `20.561111111111114, 293.7111111111111`.

We could run the script now in a pipeline, for example, to get the first
10 rows of output:

~~~ {.bash}
python climate_analysis-12.py ../data/sc_climate_data_1000.csv | head -10
~~~

But now we get a really odd error:

~~~
...
Traceback (most recent call last):
  File "climate_analysis-12.py", line 25, in <module>
    print(str(celsius)+", "+str(kelvin))
BrokenPipeError: [Errno 32] Broken pipe
Exception ignored in: <_io.TextIOWrapper name='<stdout>' mode='w' encoding='UTF-8'>
BrokenPipeError: [Errno 32] Broken pipe
~~~

This is an odd consequence of using Python in a command line pipeline ---
it doesn't cope with piping output to other commands very well.

We can fix this by including the following at the top, after our 
`temp_conversion` import:

~~~ {.python}
import signal
signal.signal(signal.SIGPIPE, signal.SIG_DFL)
~~~

We're telling our Python script to ignore any pipe errors --- not ideal,
but solves our problem. We can now do things like:

~~~ {.bash}
python climate_analysis-12.py ../data/sc_climate_data_1000.csv | wc -l
~~~

Which tells us the number of lines it processed, taking into account the
-9999 values it ignored:

~~~
     923
~~~

> ## The Right Way to Do It {.callout}
>
> If our programs can take complex parameters or multiple filenames,
> we shouldn't handle `sys.argv` directly.
> Instead,
> we should use Python's `argparse` library,
> which handles common cases in a systematic way,
> and also makes it easy for us to provide sensible error messages for our 
> users.