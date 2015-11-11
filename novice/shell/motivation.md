---
layout: slides
title: Automating tasks with the Unix shell
subtitle: 
---

## What is the shell?

- Command line interface to applications
- Called the 'shell' since it wraps the complexity of the operating system in a simple wrapper
- Can have shell commands in a file - called a 'script'
    - ... but are still just programs
- Developed in the 1970's - syntax can be parochial
- Every Unix-like system (e.g. Linux, Mac OS X) has the shell
- Most popular shell is Bash (Bourne Again SHell)

## Boromir speaks

![](img/boromir.png)

- This is wrong.

## A Typical Problem

- Running the same workflow on several samples can be labour intensive
    + e.g. the same set of processing steps over many files
- Manual manipulation of data files is...
    + Often not captured in documentation
    + Hard to reproduce
    + Prone to error
    + Difficult to troubleshoot, review, or improve

## How does the shell help?

- Workflow steps can be automated
    + Through the use of shell scripts
    + Even through one-line commands
    + It's a bit like Lego
- Built-in commands allow for easy data manipulation (e.g. sort, grep, etc.)
- Automation improves reproducibility and makes troubleshooting easier
- *Let the computer do the work!*

## Other reasons to learn the shell

- It makes you more productive!
    + Can do simple, repetitive things far more quickly
    + ...even complex things
    + You don't need to learn it all for it to be very useful
- Many applications/services depend on the shell
    + Scientific applications
    + Common server applications (e.g. web servers, databases)
    + High Performance Computing resources (e.g. IRIDIS, Lyceum, ARCHER)
- Foundation for the rest of the course

## Learning objectives

We'll find out how to:

> * Navigate the file system
> * Create files and directories
> * *Redirect* output from commands to files
> * Chaining commands together using *pipes*
> * Write loops to repeat operations many times
> * Include multiple commands in a shell *script*
> * How to find files and things within files

## Getting started

If you haven't already, let's get a shell running!

- **Windows**: run **Git Bash**
- **Mac OS X**: run **Terminal** under *Applications -> Utilities*
- **Linux**: run **Terminal** application

Then go to **http://bit.ly/SWCSoton** and follow instructions for downloading repository and configuring environment.

## Let us begin...

## An example filesystem I

![](img/filesystem.png)

## An example filesystem II

![](img/home-directories.png)

## Pipes example

![](img/redirects-and-pipes.png)

## Limitations

- Bash scripts good for quickly automating repetitive tasks that call other programs... up to a point!
    + More advanced techniques often have steep learning curve
    + Writing more complex Bash scripts can take a lot longer
    + Large Bash scripts often difficult to read and maintain

- For larger tasks use a more general language (like Python)
    + Can be more productive and lead to more maintainable code
    + You can still use Bash's pipes and redirects with them!