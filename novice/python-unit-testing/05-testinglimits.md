---
layout: page
title: Writing Robust Code and Unit Testing
subtitle: Limits to Testing
minutes: 10
---

> ## Learning Objectives {.objectives}
>
> * Understand the limits and value of unit testing

Like any other piece of experimental apparatus, a complex program requires a much higher investment in testing than a simple one. Putting it another way,
a small script that is only going to be used once, to produce one figure,
probably doesn't need separate testing: its output is either correct or not. A linear algebra library that will be used by thousands of people in twice that number of applications over the course of a decade, on the other hand, definitely does.

Unfortunately, it's practically impossible to prove that a program will always do what it's supposed to. To see why, consider a function that checks whether a character strings contains only the letters 'A', 'C', 'G', and 'T'. These four tests clearly aren't sufficient:

```python
assert is_all_bases('A')
assert is_all_bases('C')
assert is_all_bases('G')
assert is_all_bases('T')
```

because this version of `is_all_bases` passes them:

```python
def is_all_bases(bases):
    return True
```

Adding these tests isn't enough:

```python
assert not is_all_bases('X')
assert not is_all_bases('Y')
assert not is_all_bases('Z')
```

because this version still passes:

```python
def is_all_bases(bases):
    return bases[0] in 'ACGT'
```

We can add yet more tests:

```python
assert is_all_bases('ACGCGA')
assert not is_all_bases('CGAZ')
```

But no matter how many we have, we can always write a function that passes them, but does the wrong thing in other cases. And as we add more tests, we have to start worrying about whether the tests themselves are correct, and about whether we can afford the time needed to write them. After all, if we really want to check that the square root function is correct for all values between 0.0 and 1.0, we need to write over a billion test cases; that's a lot of typing, and the chances of us getting every one right are effectively zero.

Testing is still worth doing, though: it's one of those things that doesn't work in theory, but is surprisingly effective in practice. If we choose our tests carefully, we can demonstrate that our software is as likely to be correct as a mathematical proof or a physical experiment.

Ensuring that we have the right answer is only one reason to test software. The other is that it speeds up development by reducing the amount of re-work we have to do. Even small programs can be quite complex, and changing one thing can all too easily break something else. If we test changes as we make them, and automatically re-test things we've already done, we can catch and fix errors while the changes are still fresh in our minds.
