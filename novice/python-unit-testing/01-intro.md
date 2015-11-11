---
layout: page
title: Writing Robust Code and Unit Testing
subtitle: Introduction
minutes: 5
---

Our previous lessons have introduced the basic tools of programming:
variables and lists, file I/O, loops, conditionals, and most importantly, functions. What they haven't done is show us how to tell if a program is getting the right answer. For the sake of argument, if each line we write has a 99% chance of being right, then a 70-line program will be wrong more than half the time. We need to do better than that, which means we need to:

* write programs that check their own operation; and
* write tests to catch the mistakes those self-checks miss.

> ## Learning Objectives {.objectives}
>
> * how to write code defensively to guard against making errors;
> * how to use a unit testing framework;
> * when it's useful to write tests *before* writing code.
> * how Python reports and handles errors;
