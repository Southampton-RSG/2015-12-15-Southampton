---
layout: page
title: The Unix Shell
subtitle: Shell Scripts
minutes: 15
---
> ## Learning Objectives {.objectives}
>
> *   Write a shell script that runs a command or series of commands for a fixed set of files.
> *   Run a shell script from the command line.
> *   Write a shell script that operates on a set of files defined by the user on the command line.
> *   Create pipelines that include user-written shell scripts.

We are finally ready to see what makes the shell such a powerful programming environment.
We are going to take the commands we repeat frequently and save them in files
so that we can re-run all those operations again later by typing a single command.
For historical reasons,
a bunch of commands saved in a file is usually called a **shell script**,
but make no mistake:
these are actually small programs.

Let's start by going back to `novice/shell/data` and putting the following line into a new file called `middle.sh` using an editor:

~~~ {.bash}
head -15 sc_climate_data_1000.csv | tail -5
~~~

This is a variation on the pipe we constructed earlier:
it selects lines 11-15 of the file `sc_climate_data_1000.csv`.
Remember, we are *not* running it as a command just yet:
we are putting the commands in a file.

Once we have saved the file,
we can ask the shell to execute the commands it contains.
Our shell is called `bash`, so we run the following command:

~~~ {.bash}
$ bash middle.sh
~~~

~~~ {.output}
299196.8188,972890.0521,48.07,61.41,0.78
324196.8188,972890.0521,48.20,-9999.00,0.72
274196.8188,968890.0521,47.86,60.94,0.83
275196.8188,968890.0521,47.86,61.27,0.83
248196.8188,961890.0521,46.22,58.98,1.43
~~~

Sure enough,
our script's output is exactly what we would get if we ran that pipeline directly.

> ## Text vs. Whatever {.callout}
>
> We usually call programs like Microsoft Word or LibreOffice Writer "text
> editors", but we need to be a bit more careful when it comes to
> programming. By default, Microsoft Word uses `.docx` files to store not
> only text, but also formatting information about fonts, headings, and so
> on. This extra information isn't stored as characters, and doesn't mean
> anything to tools like `head`: they expect input files to contain
> nothing but the letters, digits, and punctuation on a standard computer
> keyboard. When editing programs, therefore, you must either use a plain
> text editor, or be careful to save files as plain text.

What if we want to select lines from an arbitrary file?
We could edit `middle.sh` each time to change the filename,
but that would probably take longer than just retyping the command.
Instead,
let's edit `middle.sh` and replace `sc_climate_data_1000.csv` with a special variable called `$1`:

~~~ {.bash}
$ cat middle.sh
~~~

~~~ {.output}
head -15 "$1" | tail -5
~~~

Inside a shell script,
`$1` means "the first filename (or other parameter) on the command line".
We can now run our script like this:

~~~ {.bash}
$ bash middle.sh sc_climate_data_1000.csv
~~~

~~~ {.output}
299196.8188,972890.0521,48.07,61.41,0.78
324196.8188,972890.0521,48.20,-9999.00,0.72
274196.8188,968890.0521,47.86,60.94,0.83
275196.8188,968890.0521,47.86,61.27,0.83
248196.8188,961890.0521,46.22,58.98,1.43
~~~

or on a different file like this (our full data set!):

~~~ {.bash}
$ bash middle.sh sc_climate_data.csv
~~~

~~~ {.output}
359196.8188,1017890.052,49.39,58.95,0.70
338196.8188,1011890.052,49.28,58.73,0.74
321196.8188,981890.0521,48.20,61.41,0.72
296196.8188,974890.0521,48.07,61.27,0.78
299196.8188,972890.0521,48.07,61.41,0.78
~~~


> ## Double-Quotes Around Arguments {.callout}
>
> We put the `$1` inside of double-quotes in case the filename happens to contain any spaces.
> The shell uses whitespace to separate arguments,
> so we have to be careful when using arguments that might have whitespace in them.
> If we left out these quotes, and `$1` expanded to a filename like
> `climate data.csv`,
> the command in the script would effectively be:
>
>     head -15 climate data.csv | tail -5
>
> This would call `head` on two separate files, `climate` and `data.csv`,
> which is probably not what we intended.


We still need to edit `middle.sh` each time we want to adjust the range of lines,
though.
Let's fix that by using the special variables `$2` and `$3`:

~~~ {.bash}
$ cat middle.sh
~~~

~~~ {.output}
head "$2" "$1" | tail "$3"
~~~

~~~ {.bash}
$ bash middle.sh sc_climate_data_1000.csv -20 -5
~~~

~~~ {.output}
252196.8188,961890.0521,46.22,60.94,1.43
152196.8188,960890.0521,48.81,-9999.00,1.08
148196.8188,959890.0521,48.81,59.43,1.08
325196.8188,957890.0521,48.20,61.36,0.72
326196.8188,957890.0521,47.44,61.36,0.80
~~~

This does work,
but it may take the next person who reads `middle.sh` a moment to figure out what it does.
We can improve our script by adding some **comments** at the top:

~~~ {.bash}
$ cat middle.sh
~~~

~~~ {.output}
# Select lines from the middle of a file.
# Usage: middle.sh filename -end_line -num_lines
head "$2" "$1" | tail "$3"
~~~

A comment starts with a `#` character and runs to the end of the line.
The computer ignores comments,
but they're invaluable for helping people understand and use scripts.

What if we want to process many files in a single pipeline?
For example, if we want to sort our `.csv` files by length, we would type:

~~~ {.bash}
$ wc -l *.csv | sort -n
~~~

because `wc -l` lists the number of lines in the files
(recall that wc stands for 'word count', adding the -l flag means 'count lines' instead)
and `sort -n` sorts things numerically.
We could put this in a file,
but then it would only ever sort a list of `.csv` files in the current directory.
If we want to be able to get a sorted list of other kinds of files,
we need a way to get all those names into the script.
We can't use `$1`, `$2`, and so on
because we don't know how many files there are.
Instead, we use the special variable `$@`,
which means,
"All of the command-line parameters to the shell script."
We also should put `$@` inside double-quotes
to handle the case of parameters containing spaces
(`"$@"` is equivalent to `"$1"` `"$2"` ...)
Here's an example:

~~~ {.bash}
$ cat sorted.sh
~~~

~~~ {.output}
wc -l "$@" | sort -n
~~~

~~~ {.bash}
$ bash sorted.sh *.csv ../test_directory/creatures/*.dat
~~~

~~~ {.output}
      11 sc_climate_data_10.csv
     155 ../test_directory/creatures/minotaur.dat
     163 ../test_directory/creatures/basilisk.dat
     163 ../test_directory/creatures/unicorn.dat
    1001 sc_climate_data_1000.csv
 1048580 sc_climate_data.csv
 1050073 total
~~~

> ## Why Isn't It Doing Anything? {.callout}
>
> What happens if a script is supposed to process a bunch of files, but we
> don't give it any filenames? For example, what if we type:
>
>     $ bash sorted.sh
>
> but don't say `*.dat` (or anything else)? In this case, `$@` expands to
> nothing at all, so the pipeline inside the script is effectively:
>
>     wc -l | sort -n
>
> Since it doesn't have any filenames, `wc` assumes it is supposed to
> process standard input, so it just sits there and waits for us to give
> it some data interactively. From the outside, though, all we see is it
> sitting there: the script doesn't appear to do anything.

We have two more things to do before we're finished with our simple shell scripts.
If you look at a script like:

~~~
wc -l "$@" | sort -n
~~~

you can probably puzzle out what it does.
On the other hand,
if you look at this script:

~~~
# List files sorted by number of lines.
wc -l "$@" | sort -n
~~~

you don't have to puzzle it out --- the comment at the top tells you what it does.
A line or two of documentation like this make it much easier for other people
(including your future self)
to re-use your work.
The only caveat is that each time you modify the script,
you should check that the comment is still accurate:
an explanation that sends the reader in the wrong direction is worse than none at all.

Second,
suppose we have just run a series of commands that did something useful --- for example,
that created a graph we'd like to use in a paper.
We'd like to be able to re-create the graph later if we need to,
so we want to save the commands in a file.
Instead of typing them in again
(and potentially getting them wrong)
we can do this:

~~~ {.bash}
$ history | tail -4 > redo-figure-3.sh
~~~

The file `redo-figure-3.sh` now contains:

~~~
297 bash goostats -r NENE01729B.txt stats-NENE01729B.txt
298 bash goodiff stats-NENE01729B.txt /data/validated/01729.txt > 01729-differences.txt
299 cut -d ',' -f 2-3 01729-differences.txt > 01729-time-series.txt
300 ygraph --format scatter --color bw --borders none 01729-time-series.txt figure-3.png
~~~

After a moment's work in an editor to remove the serial numbers on the commands,
we have a completely accurate record of how we created that figure.

> ## Unnumbering {.callout}
>
> Nelle could also use `colrm` (short for "column removal") to remove the
> serial numbers on her previous commands.
> Its parameters are the range of characters to strip from its input:
>
> ~~~
> $ history | tail -5
>   173  cd /tmp
>   174  ls
>   175  mkdir bakup
>   176  mv bakup backup
>   177  history | tail -5
> $ history | tail -5 | colrm 1 7
> cd /tmp
> ls
> mkdir bakup
> mv bakup backup
> history | tail -5
> history | tail -5 | colrm 1 7
> ~~~

In practice, most people develop shell scripts by running commands at the shell prompt a few times
to make sure they're doing the right thing,
then saving them in a file for re-use.
This style of work allows people to recycle
what they discover about their data and their workflow with one call to `history`
and a bit of editing to clean up the output
and save it as a shell script.

> ## Variables in shell scripts {.challenge}
>
> In the test_directory/molecules directory, you have a shell script called `script.sh` containing the 
> following commands:
>
> ~~~
> head $2 $1
> tail $3 $1
> ~~~
> 
> While you are in the molecules directory, you type the following command:
>
> ~~~
> bash script.sh '*.pdb' -1 -1
> ~~~
> 
> Which of the following outputs would you expect to see?
>
> 1. All of the lines between the first and the last lines of each file ending in `*.pdb`
>    in the molecules directory 
> 2. The first and the last line of each file ending in `*.pdb` in the molecules directory
> 3. The first and the last line of each file in the molecules directory
> 4. An error because of the quotes around `*.pdb`

> ## List unique species {.challenge}
> 
> Leah has several hundred data files, each of which is formatted like this:
> 
> ~~~
> 2013-11-05,deer,5
> 2013-11-05,rabbit,22
> 2013-11-05,raccoon,7
> 2013-11-06,rabbit,19
> 2013-11-06,deer,2
> 2013-11-06,fox,1
> 2013-11-07,rabbit,18
> 2013-11-07,bear,1
> ~~~
> 
> Write a shell script called `species.sh` that takes any number of
> filenames as command-line parameters, and uses `cut`, `sort`, and
> `uniq` to print a list of the unique species appearing in each of
> those files separately.

> ## Why record commands in the history before running them? {.challenge}
> 
> If you run the command:
> 
> ~~~
> history | tail -5 > recent.sh
> ~~~
> 
> the last command in the file is the `history` command itself, i.e.,
> the shell has added `history` to the command log before actually
> running it. In fact, the shell *always* adds commands to the log
> before running them. Why do you think it does this?

> ## Script reading comprehension {.challenge}
> 
> Joel's `data` directory contains three files: `fructose.dat`,
> `glucose.dat`, and `sucrose.dat`. Explain what a script called
> `example.sh` would do when run as `bash example.sh *.dat` if it
> contained the following lines:
> 
> ~~~
> # Script 1
> echo *.*
> ~~~
> 
> ~~~
> # Script 2
> for filename in $1 $2 $3
> do
>     cat $filename
> done
> ~~~
> 
> ~~~
> # Script 3
> echo $@.dat
> ~~~
