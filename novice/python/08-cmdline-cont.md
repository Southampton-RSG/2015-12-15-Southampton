---
layout: page
title: Building programs with Python
subtitle: Command-Line Programs (Continued)
minutes: 20
---
## Handling Multiple Files

The next step is to teach our program how to handle multiple files.
Since 60 lines of output per file is a lot to page through,
we'll start by creating three smaller files,
each of which has three days of data for two patients:

~~~ {.input}
$ ls data/small-*.csv
~~~
~~~ {.output}
small-01.csv small-02.csv small-03.csv
~~~

~~~ {.input}
$ cat data/small-01.csv
~~~
~~~ {.output}
0,0,1
0,1,2
~~~

~~~ {.input}
$ python readings-02.py data/small-01.csv
~~~
~~~ {.output}
0.333333333333
1.0
~~~

Using small data files as input also allows us to check our results more easily:
here,
for example,
we can see that our program is calculating the mean correctly for each line,
whereas we were really taking it on faith before.
This is yet another rule of programming:
*test the simple things first*.

We want our program to process each file separately,
so we need a loop that executes once for each filename.
If we specify the files on the command line,
the filenames will be in `sys.argv`,
but we need to be careful:
`sys.argv[0]` will always be the name of our script,
rather than the name of a file.
We also need to handle an unknown number of filenames,
since our program could be run for any number of files.

The solution to both problems is to loop over the contents of `sys.argv[1:]`.
The '1' tells Python to start the slice at location 1,
so the program's name isn't included;
since we've left off the upper bound,
the slice runs to the end of the list,
and includes all the filenames.
Here's our changed program
`readings-03.py`:

~~~ {.python}
import sys
import numpy as np

def main():
    script = sys.argv[0]
    for filename in sys.argv[1:]:
        data = np.loadtxt(filename, delimiter=',')
        for m in data.mean(axis=1):
            print m

main()
~~~

and here it is in action:

~~~ {.input}
$ python readings-03.py data/small-01.csv data/small-02.csv
~~~
~~~ {.output}
0.333333333333
1.0
13.6666666667
11.0
~~~

> ## The Right Way to Do It {.callout}
>
> At this point,
> we have created three versions of our script called `readings-01.py`,
> `readings-02.py`, and `readings-03.py`.
> We wouldn't do this in real life:
> instead,
> we would have one file called `readings.py` that we committed to version control
> every time we got an enhancement working.
> For teaching,
> though,
> we need all the successive versions side by side.

## Handling Command-Line Flags

The next step is to teach our program to pay attention to the `--min`, `--mean`, and `--max` flags.
These always appear before the names of the files,
so we could just do this:

~~~ {.python}
import sys
import numpy as np

def main():
    script = sys.argv[0]
    action = sys.argv[1]
    filenames = sys.argv[2:]

    for f in filenames:
        data = np.loadtxt(f, delimiter=',')

        if action == '--min':
            values = data.min(axis=1)
        elif action == '--mean':
            values = data.mean(axis=1)
        elif action == '--max':
            values = data.max(axis=1)

        for m in values:
            print m

main()
~~~

This works:

~~~ {.input}
$ python readings-04.py --max data/small-01.csv
~~~
~~~ {.output}
1.0
2.0
~~~

but there are several things wrong with it:

1.  `main` is too large to read comfortably.

2.  If `action` isn't one of the three recognized flags,
    the program loads each file but does nothing with it
    (because none of the branches in the conditional match).
    [Silent failures](reference.html#silence-failure) like this
    are always hard to debug.

This version pulls the processing of each file out of the loop into a function of its own.
It also checks that `action` is one of the allowed flags
before doing any processing,
so that the program fails fast:

~~~ {.python}
import sys
import numpy as np

def main():
    script = sys.argv[0]
    action = sys.argv[1]
    filenames = sys.argv[2:]
    assert action in ['--min', '--mean', '--max'], \
           'Action is not one of --min, --mean, or --max: ' + action
    for f in filenames:
        process(f, action)

def process(filename, action):
    data = np.loadtxt(filename, delimiter=',')

    if action == '--min':
        values = data.min(axis=1)
    elif action == '--mean':
        values = data.mean(axis=1)
    elif action == '--max':
        values = data.max(axis=1)

    for m in values:
        print m

main()
~~~

This is four lines longer than its predecessor,
but broken into more digestible chunks of 8 and 12 lines.

Python has a module named [argparse](http://docs.python.org/dev/library/argparse.html)
that helps handle complex command-line flags. We will not cover this module in this lesson
but you can go to Tshepang Lekhonkhobe's [Argparse tutorial](http://docs.python.org/dev/howto/argparse.html)
that is part of Python's Official Documentation.

## Handling Standard Input

The next thing our program has to do is read data from standard input if no filenames are given
so that we can put it in a pipeline,
redirect input to it,
and so on.
Let's experiment in another script called `count-stdin.py`:

~~~ {.python}
import sys

count = 0
for line in sys.stdin:
    count += 1

print count, 'lines in standard input'
~~~

This little program reads lines from a special "file" called `sys.stdin`,
which is automatically connected to the program's standard input.
We don't have to open it --- Python and the operating system
take care of that when the program starts up ---
but we can do almost anything with it that we could do to a regular file.
Let's try running it as if it were a regular command-line program:

~~~ {.input}
$ python count-stdin.py < data/small-01.csv
~~~
~~~ {.output}
2 lines in standard input
~~~

A common mistake is to try to run something that reads from standard input like this:

~~~ {.input}
$ count_stdin.py data/small-01.csv
~~~

i.e., to forget the `<` character that redirect the file to standard input.
In this case,
there's nothing in standard input,
so the program waits at the start of the loop for someone to type something on the keyboard.
Since there's no way for us to do this,
our program is stuck,
and we have to halt it using the `Interrupt` option from the `Kernel` menu in the Notebook.

We now need to rewrite the program so that it loads data from `sys.stdin` if no filenames are provided.
Luckily,
`numpy.loadtxt` can handle either a filename or an open file as its first parameter,
so we don't actually need to change `process`.
That leaves `main`:

~~~ {.python}
def main():
    script = sys.argv[0]
    action = sys.argv[1]
    filenames = sys.argv[2:]
    assert action in ['--min', '--mean', '--max'], \
           'Action is not one of --min, --mean, or --max: ' + action
    if len(filenames) == 0:
        process(sys.stdin, action)
    else:
        for f in filenames:
            process(f, action)
~~~

Let's try it out:

~~~ {.python}
0.333333333333
1.0
~~~

That's better.
In fact,
that's done:
the program now does everything we set out to do.

> ## Arithmetic on the command line {.challenge}
>
> Write a command-line program that does addition and subtraction:
>
> ~~~ {.python}
> $ python arith.py 1 + 2
> ~~~
> ~~~ {.output}
> 3
> ~~~
> ~~~ {.python}
> $ python arith.py 3 - 4
> ~~~
> ~~~ {.output}
> -1
> ~~~
>
> What goes wrong if you try to add multiplication using '*' to the program?

> ## Finding particular files {.challenge}
>
> Using the `glob` module introduced [02-loop.html](earlier),
> write a simple version of `ls` that shows files in the current directory with a particular suffix:
>
> ~~~ {.python}
> $ python my_ls.py py
> ~~~
> ~~~ {.output}
> left.py
> right.py
> zero.py
> ~~~

> ## Changing flags {.challenge}
>
> Rewrite `count-stdin.py` so that it uses `-n`, `-m`, and `-x` instead of `--min`, `--mean`, and `--max` respectively.
> Is the code easier to read?
> Is the program easier to understand?

> ## Adding a help message {.challenge}
>
> Separately,
> modify the program so that if no parameters are given
> (i.e., no action is specified and no filenames are given),
> it prints a message explaining how it should be used.

> ## Adding a default action {.challenge}
>
> Separately,
> modify the program so that if no action is given
> it displays the means of the data.

> ## A file-checker {.challenge}
>
> Write a program called `check.py` that takes the names of one or more inflammation data files as arguments
> and checks that all the files have the same number of rows and columns.
> What is the best way to test your program?

> ## Counting lines {.challenge}
>
> Write a program called `line-count.py` that works like the Unix `wc` command:
>
> *   If no filenames are given, it reports the number of lines in standard input.
> *   If one or more filenames are given, it reports the number of lines in each, followed by the total number of lines.
