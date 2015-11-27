---
layout: page
title: Building programs with Python
subtitle: Arrays, Lists etc
minutes: 15
---
> ## Learning Objectives {.objectives}
>
> *   Lists and Arrays in Python
> *   Indexing and slicing

### Arrays in Python

One of the most fundamental data structures in any language is the array. Python doesn't have 
a native array data structure, but it has the list which is much more general and can be used 
as a multidimensional array quite easily.

### List basics

A list in python is just an ordered collection of items which can be of any type. By comparison 
an array is an ordered collection of items of a single type - so a list is more flexible than an 
array.

A list is also a dynamic mutable type and this means we can add and delete elements from the list 
at any time. 

Lists are built into the language (so we don't have to load a library to use them).

To define a list we simply write a comma separated list of items in square brackets:

~~~{.python}
odds = [1, 3, 5, 7, 9, 11, 15]
print('Odds are:', odds)

~~~

~~~{.output}
Odds are: [1, 3, 5, 7, 9, 11, 15]
~~~

This looks like an array because we can use *slicing* notation to pick out an individual element - 
indexes start from 0.

Programming languages like Fortran and MATLAB start counting at 1,
because that's what human beings have done for thousands of years.
Languages in the C family (including C++, Java, Perl, and Python) count from 0
because that's simpler for computers to do.

It takes a bit of getting used to,
but one way to remember the rule is that
the index is how many steps we have to take from the start to get the item we want.

We select individual elements from lists by indexing them:

~~~{.python}
print('first and last:', odds[0], odds[-1])
~~~

will print first and last elements, i.e. value 1 and 7 in this case. 

~~~ {.output}
first and last: 1 15
~~~

Similarly to change the seventh element we can 
assign directly to it:

~~~{.python}
odds[6] = 13
~~~

The *Slicing* notation looks like array indexing but it is a lot more flexible. For example:

~~~{.python}
odds[2:5]
~~~

~~~{.output}
[5, 7, 9]
~~~

is a sublist from the third element to the fifth i.e. from `odds[2]` to `odds[4]`. Notice that the 
final element specified i.e. `[5]` is not included in the slice.

Also notice that you can leave out either of the start and end indexes and they will be assumed to have their maximum possible value. 
For example:

~~~{.python}
odds[5:]
~~~

~~~{.output}
[11, 13]
~~~

is the list from `odds[5]` to the end of the list and

~~~{.python}
odds[:5]
~~~

~~~{.output}
[1, 3, 5, 7, 9]
~~~

is the list up to and not including odds[5] and

~~~{.python}
odds[:]
~~~

~~~{.output}
[1, 3, 5, 7, 9, 11, 13]
~~~

is the entire list.

### Slicing strings 

A section of an array is called a [slice](../../reference.html#slice).
We can take slices of character strings as well:

~~~ {.python}
element = 'oxygen'
print('first three characters:', element[0:3])
print('last three characters:', element[3:6])
~~~

~~~ {.output}
first three characters: oxy
last three characters: gen
~~~
>
> ##Slicing strings challenge{.challenge}
>
> What is the value of `element[:4]`?
> What about `element[4:]`?
> Or `element[:]`?
>
> What is `element[-1]`?
> What is `element[-2]`?
> Given those answers,
> explain what `element[1:-1]` does.

List slicing is more or less the same as string slicing except that we can modify a slice. For example:

~~~{.python}
odds[0:2]=[17,19]
~~~

has the same effect as

~~~{.python}
odds[0]=17
odds[1]=19
~~~

**NOTE:**

Finally it is worth knowing that the list we assign to a slice doesn't have to be the same size as the slice - 
it simply replaces it even if it is a different size.

### Thin slices 

The expression `element[3:3]` produces an [empty string](../../reference.html#empty-string),
 i.e., a string that contains no characters.
 
### Lists and Strings
 
There is one important difference between lists and strings:
we can change the values in a list,
but we cannot change the characters in a string.
For example:

~~~ {.python}
names = ['Newton', 'Darwing', 'Turing'] # typo in Darwin's name
print('names is originally:', names)
names[1] = 'Darwin' # correct the name
print('final value of names:', names)
~~~

~~~ {.output}
names is originally: ['Newton', 'Darwing', 'Turing']
final value of names: ['Newton', 'Darwin', 'Turing']
~~~

works, but:

~~~ {.python}
name = 'Bell'
name[0] = 'b'
~~~

~~~{.error}
>>> name[0]='b'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
~~~

does not.

> ## Ch-Ch-Ch-Changes {.callout}
> 
> Data which can be modified in place is called [mutable](reference.html#mutable),
> while data which cannot be modified is called [immutable](reference.html#immutable).
> Strings and numbers are immutable. This does not mean that variables with string or number values are constants,
> but when we want to change the value of a string or number variable, we can only replace the old value 
> with a completely new value.
>
> Lists and arrays, on the other hand, are mutable: we can modify them after they have been created. We can 
> change individual elements, append new elements, or reorder the whole list.  For some operations, like 
> sorting, we can choose whether to use a function that modifies the data in place or a function that returns a 
> modified copy and leaves the original unchanged.
>
> Be careful when modifying data in place.  If two variables refer to the same list, and you modify the list 
> value, it will change for both variables! If you want variables with mutable values to be independent, you 
> must make a copy of the value when you assign it.
>
> Because of pitfalls like this, code which modifies data in place can be more difficult to understand. However, 
> it is often far more efficient to modify a large data structure in place than to create a modified copy for 
> every small change. You should consider both of these aspects when writing your code.

There are many ways to change the contents of lists besides assigning new values to
individual elements:

~~~ {.python}
odds.append(21)
print('odds after adding a value:', odds)
~~~
~~~ {.output}
odds after adding a value: [17, 19, 5, 7, 9, 11, 13, 15, 21]
~~~

~~~ {.python}
del odds[0]
print('odds after removing the first element:', odds)
~~~
~~~ {.output}
odds after removing the first element: [19, 5, 7, 9, 11, 13, 15, 21]
~~~

~~~ {.python}
odds.reverse()
print('odds after reversing:', odds)
~~~
~~~ {.output}
odds after reversing: [21, 15, 13, 11, 9, 7, 5, 19]
~~~

While modifying in place, it is useful to remember that python treats lists in a slightly counterintuitive way.

If we make a list and (attempt to) copy it then modify in place, we can cause all sorts of trouble:

~~~ {.python}
odds = [1, 3, 5, 7]
primes = odds
primes += [2]
print('primes:', primes)
print('odds:', odds)
~~~
~~~ {.output}
primes: [1, 3, 5, 7, 2]
odds: [1, 3, 5, 7, 2]
~~~

This is because python stores a list in memory, and then can use multiple names to refer to the same list.
If all we want to do is copy a (simple) list, we can use the list() command, so we do not modify a list we did not mean to:

~~~ {.python}
odds = [1, 3, 5, 7]
primes = list(odds)
primes += [2]
print('primes:', primes)
print('odds:', odds)
~~~
~~~ {.output}
primes: [1, 3, 5, 7, 2]
odds: [1, 3, 5, 7]
~~~

This is different from how variables worked in lesson 1, and more similar to how a spreadsheet works.

### Basic array operations

So far so good, and it looks as if using a list is as easy as using an array.

Where things start to go wrong just a little is when we attempt to push the similarities 
between lists and arrays one step too far. For example, suppose we want to create an array 
initialised to a particular value. Following the general array idiom in most languages we 
might initialise the elements to a value, say, 1. e.g.:

~~~ {.python}
myList=[]
myList[1]=1
myList[2]=1
...
~~~

only to discover that this doesn't work because we can't assign to a list element that doesn't already exist.

~~~{.error}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list assignment index out of range
~~~

One solution is to use the append method to add elements one by one:

~~~ {.python}
myList=[]
myList.append(1)
myList.append(1)
...
~~~

This works but it only works if we need to build up the list in this particular order - which most of the time you want to do anyway.
