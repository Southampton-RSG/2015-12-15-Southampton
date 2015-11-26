---
layout: page
title: Building programs with Python
subtitle: Processing data files
minutes: 15
---
> ## Learning Objectives {.objectives}
>
> *   Write a script to open a data file and print out its contents.
> *   Perform some operations on strings to extract desired data from it.
> *   Understand the basics of how Python handles objects.
> *   Understand good practices of how and when to write a code comment.

So far we've seen how to use and manipulate variables, and how to use loops in a script to process strings.
But let's take a look at a more interesting use case - performing some
temperature conversions on our CSV data file.

We'll start out by looking at how to read the data file and print
its contents in a script, and then modify our script to perform
some conversions and output that.
Along the way, we'll see how we can make our code more understandable to 
others (as well as ourselves, when we might come back to it at a later date).

<!-- ** Mention CSV specific library -->

### Printing out the contents of a data file

We first need to be able to read in our data from the `sc_climate_data_10.csv`
file, and using a loop, print out each line. Let's write another script
called `climate_analysis.py`, and enter the following:

~~~ {.python}
climate_data = open('../data/sc_climate_data_10.csv', 'r')

for line in climate_data:
    print(line)
~~~

Using `open`, we first specify the file we wish to open, and then include how
we want to use that file. If we wanted to open a file to write to, we would use 'w', but in this case, we specify `r` for reading.

In general, we know that a loop will iterate over a collection and set a loop
variable to be each item in that collection. When Python deals with files, it
does something quite helpful in a loop. By specifying `climate_data` as our collection, it reads in a single line at a time from our data file, assigning it to our `line` loop control variable.

We can run our code with:

~~~ {.bash}
$ python climate_analysis.py
~~~

And we get the following output:

~~~
# POINT_X,POINT_Y,Min_temp_Jul_F,Max_temp_jul_F,Rainfall_jul_inch

461196.8188,1198890.052,47.77,58.53,0.76

436196.8188,1191890.052,47.93,58.60,0.83

445196.8188,1168890.052,47.93,58.30,0.74

450196.8188,1144890.052,48.97,56.91,0.66

329196.8188,1034890.052,49.26,59.86,0.78

359196.8188,1017890.052,49.39,58.95,0.70

338196.8188,1011890.052,49.28,58.73,0.74

321196.8188,981890.0521,48.20,61.41,0.72

296196.8188,974890.0521,48.07,61.27,0.78

299196.8188,972890.0521,48.07,61.41,0.78

~~~

Hmmm... but that's not really perfect, since it's also printing out additional
newlines which exist at the end of each line in our data file.
We can remove them by stripping them out, using `rstrip`, a function
that works on strings. We can use it like:

~~~ {.python}
    print(line.rstrip())
~~~

So what's happening here?

> ## Python and object orientation - in a nutshell {.callout}
> 
> So far we've used strings, which are a type of object in Python.
> In general, an object is an instance of something called a class.
>
> A class defines how a certain thing can behave, and an object
> is then a particular thing that behaves the way its class tells it to.
> You can define classes that include properties (like variables, associated
> with that class), and methods (like functions, also associated with
> that class and can perform operations on them). We can use classes to
> define things in the real world.
>
> For example, a car is made up of things like an engine, wheels, windows,
> and so forth - these things could be defined as classes. And for
> each of these, they would have their own properties and methods. A wheel class
> for example, could have diameter and width as properties, and a window
> could have size, tint and shape and properties, and assuming it's an 
> electric window, it could have up() and down() as methods to raise
> and lower the window. A class can have as many properties and methods
> as we choose to define for it.
>
> When we define a particular car, we could say it has a single engine,
> four wheels and four windows. Each of these would be an object --- an instance
> of its class --- each with its own set of properties, which could all
> be different. We're taking advantage of the fact that all four
> windows and all four wheels will behave the same way, but individually.
> Using the down() method on one of the windows would cause
> that window to lower, but only that window.
>
> So, in our example, `line` is a String object, an instance of a String class.
> And that String class has a defined method called `rstrip()`, which 
> removes the trailing newline. There are many other String methods which
> are incredibly useful!

So, let's try that out:

~~~ {.python}
climate_data = open('../data/sc_climate_data_10.csv', 'r')

for line in climate_data:
    print(line.rstrip())
~~~

And now we get:

~~~
# POINT_X,POINT_Y,Min_temp_Jul_F,Max_temp_jul_F,Rainfall_jul_inch
461196.8188,1198890.052,47.77,58.53,0.76
436196.8188,1191890.052,47.93,58.60,0.83
445196.8188,1168890.052,47.93,58.30,0.74
450196.8188,1144890.052,48.97,56.91,0.66
329196.8188,1034890.052,49.26,59.86,0.78
359196.8188,1017890.052,49.39,58.95,0.70
338196.8188,1011890.052,49.28,58.73,0.74
321196.8188,981890.0521,48.20,61.41,0.72
296196.8188,974890.0521,48.07,61.27,0.78
299196.8188,972890.0521,48.07,61.41,0.78
~~~

Much better!

### Selecting and printing out only part of the data

But we're not being very discriminating with our data, we're just blindly
printing out everything. Since we need to process the individual column
that represents the maximum temperature for July, the 4th one, how do we extract it from the line of data?

As luck (or more likely, good design) would have it, there's a handy string method called `split()` which can separate all the columns into a list.

We've seen how we can trim trailing newlines from strings with `rstrip()` acting on a string object. Well, we use `split()` in exactly the same way:

~~~ {.python}
    data = line.split(',')
~~~

Although in this case, we're capturing the returned list from `split()` into a 
variable called `data`. We can access elements in that list as before.

So, let's change our code accordingly:

~~~ {.python}
climate_data = open('../data/sc_climate_data_10.csv', 'r')

for line in climate_data:
    data = line.split(',')

    # print 4th column (max temperature)
    print('Max temperature', data[3])
~~~

Now, it's important to remember that the column we want, the maximum 
temperature, is the 4th column. But in Python list indexes start at 0, so in 
fact we need to obtain the value from `data[3]` and **not** `data[4]`. So, we 
have made a note to that effect in a *comment*.

> ## When should you add a comment? {.callout}
> 
> The trick is to keep your audience in mind when writing code --- this could
> be someone else in the lab, or perhaps someone in another institution. A
> good rule of thumb is to assume that someone will **always** read your code
> at a later date, and this includes a future version of yourself. It can be
> easy to forget why you did something a particular way in six months time.
> 
> Which leads to a good point about comments: generally, they should explain
> the **why**. In most cases, the code already explains the **how**, so if
> something could be considered unclear, add a comment.
> 
> A [good philosophy on code comments](http://blog.codinghorror.com/code-tells-you-how-comments-tell-you-why/) is that **the best kind of comments are 
> the ones you don't need**. You should write your code so it's easier to 
> understand without comments first, and only add comments when it **cannot**
> be made easier to understand.

And we get:

~~~
Max temperature Max_temp_jul_F
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

This perhaps isn't what we want - the column header is also part of the output!
