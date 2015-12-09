---
layout: page-md
title: Software Prerequisites
---

**Prior to the workshop, it is vital that you install some software on your laptop and create an account at Github by following the instructions below!**

There is little time during the workshop to deal with installation problems, so it makes the day run much more smoothly if you arrive with your software already installed.

## Help!

We maintain a list of common problems that can occur during installation and ways of solving them. Take a look at the [Configuration Problems and Solutions wiki page](https://github.com/swcarpentry/workshop-template/wiki/Configuration-Problems-and-Solutions) for help.

If you still have trouble, we will run a **Software Installation surgery from 09.30 AM until 12.30 PM** on  ***Monday, December 14, 2015***. This will take place in room 3013 (Simon Hettrick's office), Building 32, Highfield campus. If you would like to come along to the surgery, [email us to arrange a time](mailto:rsg-info@soton.ac.uk). 


## Bash

Among many other things, Bash allows you to automate dull and boring tasks. We use it during the command line section of the course.

#### Windows

Bash will be provided as part of the Git for Windows installation as described below.

#### Mac OS X

The Bash shell is accessed by opening the "Terminal" application. The Terminal application can be found in the "Utilities" folder which is in your "Applications" folder.

#### Linux

The Bash shell is accessed via the Terminal application.

## Text Editor

A text editor is the piece of software you use to view and write code. If you have a preferred text editor, please use it. If you don&#39;t have one, we recommend the following.

#### Windows

[Notepad++](https://notepad-plus-plus.org/download/v6.8.7.html). Just download the installer and run it.

#### Mac OS X and Linux

Nano is a text editor that is installed by default on Mac OS X and Linux.

You can verify you have nano installed by opening a terminal and entering:</p>

~~~ {.code}
nano
~~~

If nano is not installed, you will receive an error. If it is installed, nano will open (appearing not dissimilar to the terminal window, but with menu items at the bottom of the window).

To exit nano press CTRL+X (you might be prompted you to save or discard modified buffer - just type "N" to exit without saving).


## Python

We use Python 3.4, because it is generally the most widely used version of Python. We will also use the numpy and matplotlib libraries and the nose unit testing framework. Fortunately, these do not need to be installed separately! The "Python3.4 Anaconda" installation provides everything Python-related you will need for the workshop. To install Anaconda, follow the instructions below.

#### Windows

Download the [Python3.4 Anaconda installer](https://repo.continuum.io/archive/Anaconda3-2.3.0-Windows-x86_64.exe). Double click the installer and follow the instructions.

#### Mac OS X

Download the [Python 3.4 Anaconda MAC OS X Graphical installer](https://repo.continuum.io/archive/Anaconda3-2.3.0-MacOSX-x86_64.pkg). Double click the `.pkg` file and follow the instructions.

#### Linux

Download the [Python3.4 Anaconda installation script](https://repo.continuum.io/archive/Anaconda3-2.3.0-Linux-x86_64.sh). Install via the terminal like this:

~~~{.code}
bash Anaconda3-2.3.0-Linux-x86_64.sh
~~~

## Git

Git is the version control software we will use. It allows you to keep track of your software and the edits made to it.

####Create a Github account

**You should must create a Github account before attending the workshop!**

To create an account, [go to the Github website](https://github.com/join) and provide your details. It's quick and it's free. Once you have your account, you need to install the Git software as described below.

#### Windows

Download and install [Git for Windows](http://git-scm.com/download/win). **Please note** that you can accept the default installation options, **with one exception** - at the step 'Configuring the terminal emulator to use with Git Bash' you **must** select 'Use Windows default console window'.

#### Mac OS X

On Mac OS X 10.9 Mavericks and 10.10 Yosemite, Git will be installed automatically the first time you try to run it.  Open a terminal and enter:

~~~ {.code}
git
~~~

There may be a short delay whilst the installer operates. You can then follow the prompts to install the Apple command line development tools.

On Mac OS X 10.6 Snow Leoapard, Mac OS X 10.7 Lion and 10.8 Mountain Lion, download and open the [Git installer image](http://downloads.sourceforge.net/project/git-osx-installer/git-2.3.5-intel-universal-snow-leopard.dmg?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Fgit-osx-installer%2Ffiles%2F&ts=1441637770&use_mirror=kent). Double click the `.pkg` file and follow the instructions.

If you intend to use an earlier version of Mac OS X, please contact us before the event.

#### Linux

Install via a terminal like this:

Ubuntu 14.04LTS and derivatives:

~~~ {.code}
sudo apt-get install git
~~~

Fedora 22:

~~~ {.code}
su -
dnf install git
~~~

## Verify your setup

To make sure that everything has installed correctly, we have written a simple Python script to test the prerequisites.

**Close your existing terminal and reopen it (this is important!)**.

Enter the command below into your terminal. It will download the python script and run it to check your prerequisites. 

#### Windows

From the Git folder in the Start Menu, open the Git Bash terminal.

~~~ {.code}
curl -L http://goo.gl/HuPJu3 | python
~~~

#### Mac OS X, Linux

Close your existing terminal and reopen it.  **This is important!**

~~~ {.code}
curl -L http://goo.gl/HuPJu3 | python3.4
~~~


On Windows, Mac OS X and Linux, the script will run and output some text. If everything has installed correctly, within the text you will see eight passes and no failures, like this:

~~~ {.code}
check command line shell (virtual-shell)...	pass
check Git (git)...	pass
check Nose (nosetests)...	pass
check Nose Python package (nose)...	pass
check Python version (python)...	pass
check Argparse (argparse)...	pass
check NumPy (numpy)...	pass
check Matplotlib (matplotlib)...	pass
~~~

If anything fails, please [contact us](mailto:rsg-info@soton.ac.uk) before the workshop.

## During the workshop

We will make use of the [Etherpad](https://public.etherpad-mozilla.org/p/SWC-Soton-Dec2015) collaboration tool during the workshop (Etherpad allows a group to edit documents online collaboratively in real-time). Please use this to keep collaborative notes and ask (and answer!) each others questions.
