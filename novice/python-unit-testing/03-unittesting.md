---
layout: page
title: Writing Robust Code and Unit Testing
subtitle: Unit Testing
minutes: 20
---

> ## Learning Objectives {.objectives}
>
> * Understand what a unit test is
> * How to use the Nose unit testing framework to structure and run Python unit tests

Most people don't enjoy writing tests, so if we want them to actually do it, it must be easy to:

- add or change tests,
- understand the tests that have already been written,
- run those tests, and
- understand those tests' results.

Test results must also be reliable. If a testing tool says that code is working when it's not, or reports problems when there actually aren't any, people will lose faith in it and stop using it.

The simplest kind of test is a **unit test** that checks the behavior of one component of a program. As an example, suppose we're testing a function called `rectangle_area` that returns the area of an `(x0, y0, x1, y1)` rectangle. We'll start by testing our code directly using `assert`. Here, we call the function three times with different arguments, checking that the right value is returned each time.

~~~ {.python}
from rectangle2 import rectangle_area

assert rectangle_area([0, 0, 1, 1]) == 1.0
assert rectangle_area([1, 1, 4, 4]) == 9.0
assert rectangle_area([0, 1, 4, 7]) == 24.0
~~~

~~~ {.output}
---------------------------------------------------------------------------
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError
~~~

This result is used, in the sense that we know something's wrong, but look closely at what happens if we run the tests in a different order:

~~~ {.python}
assert rectangle_area([0, 1, 4, 7]) == 24.0
assert rectangle_area([1, 1, 4, 4]) == 9.0
assert rectangle_area([0, 0, 1, 1]) == 1.0
~~~

~~~ {.output}
---------------------------------------------------------------------------
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError
~~~

Python halts at the first failed assertion, so the second and third tests aren't run at all. It would be more helpful if we could get data from all of our tests every time they're run, since the more information we have, the faster we're likely to be able to track down bugs. It would also be helpful to have some kind of summary report: if our test suite includes thirty or forty tests (as it well might for a complex function or library that's widely used), we'd like to know how many passed or failed.

So - let's look at the code to see what's wrong.

~~~ {.python}
def rectangle_area(coords):
    x0, y0, x1, y1 = coords
    return (x1 - x0) * (x1 - y0)
~~~

Clearly `x1 - y0` should be `y1-y0`! But let's not fix it yet...

Here's a different approach. First, let's create a new file called `test_rectangle2.py` (note the `test_` prefix - this is important!), and put each test in a function with a meaningful name.

~~~ {.python}
from rectangle2 import rectangle_area

def test_unit_square():
    assert rectangle_area([0, 0, 1, 1]) == 1.0

def test_large_square():
    assert rectangle_area([1, 1, 4, 4]) == 9.0

def test_actual_rectangle():
    assert rectangle_area([0, 1, 4, 7]) == 24.0
~~~

Next, we can use the `nose` package to run our tests for us:

~~~ {.in}
$ nosetests
~~~

~~~ {.output}
..F
======================================================================
FAIL: test_rectangle2.test_actual_rectangle
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/user/Work/anaconda/lib/python3.4/site-packages/nose/case.py", line 198, in runTest
    self.test(*self.arg)
  File "/Users/user/Work/Python Codes/python-unit-testing/code/test_rectangle2.py", line 10, in test_actual_rectangle
    assert rectangle_area([0, 1, 4, 7]) == 24.0
AssertionError

----------------------------------------------------------------------
Ran 3 tests in 0.002s

FAILED (failures=1)
~~~

`nosetests` looks for files with a ``test_`` prefix and runs them, looking for functions whose names also start with the letters `'test_'` and runs each one:

-  If the function completes without an assertion being triggered, we count the test as a *success*
-  If an assertion fails, we count the test as a *failure*.
-  If any other exception occurs, we count it as an *error*, because the odds are that the test itself is broken.

So now we can fix our code in rectangle2.py, so it should read:

~~~ {.python}
def rectangle_area(coords):
    x0, y0, x1, y1 = coords
    return (x1 - x0) * (y1 - y0)
~~~

`nose` is an xUnit testing library. The name "xUnit" comes from the fact that many of them are imitations of a Java testing library called JUnit. The [Wikipedia page](http://en.wikipedia.org/wiki/List_of_unit_testing_frameworks) on the subject lists dozens of similar frameworks in almost as many languages,
all of which have a similar structure: each test is a single function that follows some naming convention (e.g., starts with `'test_'`), and the framework runs them in some order and reports how many passed, failed, or were broken.

> ## Challenge {.challenge}
> 
> 1.  A colleague of yours has written a function that calculates the running total of all the values in a list, e.g.,
>     `running([0, 1, 2])` produces the list `[0, 1, 3]`.
>     Write some unit test functions for it in a `test_running.py` file
>     (including `from running import running` at the top), and then use `nose` 
>     to see what bugs you can find.

## Revisiting Climate Analysis

Going back to our climate analysis code, you'll remember we wrote two
temperature conversion functions. Let's write some unit tests for them.

> ## Challenge {.challenge}
> 
> 1. Write some unit tests for the `fahr_to_kelvin` function in 
>    `temp_conversion.py`, which you can find in 
>    `python-unit-testing/code/temp_conversion.py`.
>    Place your unit tests in a new file called `test_temp_conversion.py`
>    in the `python-unit-testing/code` directory, and use `nose` to run
>    the tests.
>    Try and think about tests that could **break** your code --- what
>    are its limits?
> 
> 2. Once you've completed your tests, add them to version control along
>    with your climate code.

So why are we checking in our tests as well to version control?

The big advantage is that as our code develops, we can update our test
cases and check these in, ensuring that ourselves (and others) always have a set 
of tests to verify our code at each step of development. This way, when we
implement a new feature, we can check a) that the feature works using a test
we write for it, and b) that the development of the new feature doesn't break
any existing functionality.

