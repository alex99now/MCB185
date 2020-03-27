
===================================

This is meant to be a very quick introduction to the Unix operating
system for the BIS180L bioinformatics laboratory class at UC Davis. The
examples below assume you are using Ubuntu Linux 13.10, other versions
and distributions will probably be fine. Why does the title of this
document mention Unix when the distribution is Linux? Is there a
difference between Unix and Linux? Practically, no; philosophically,
sort-of; politically, yes. No time to discuss. Onward.

## Author, Version, and Other Front-matter ##

This document was authored by Ian Korf. It is in the  Public Domain. No
rights reserved. It is for entertainment purposes only, so if you hurt
yourself, don't blame me. The text was prepared in Markdown format (John
Gruber) using BareBones TextWrangler. The PDF version was formatted with
Marked (by Brett Terpstra) using the GitHub stylesheet. Thanks clever
and kind developers for making my life easier.

## Terminal, Command Line, and Shell ##

Your interface to Unix will be through a **shell** program using the
**command line interface** within a **terminal** application. There are
several types of shells and terminals, but the details of these are
unnecessary for us. The command line is where you type instructions for
what you want the computer to do. Some of these statements are "do this
now" while others are "let's get ready to do this." It may seem silly in
this high-tech age to type your commands when you could simply point and
click or maybe even use voice activation or gesturing. It is easier to
automate typing though. So when it comes time to work with thousands of
files, it will be much easier through a command line interface.

### Terminal Basics ###

Launch the terminal application (the name of this will differ from one
operating system to another and even within a particular OS you will
have several options). Run the `date` command by typing in the terminal
and ending with the **return** key.

	date

Congratulations, you just made your first Unix statement. You type words
on the command line (in this case just one) and then hit return to
execute the command. `date` is but one of hundreds of Unix commands you
have at your fingertips (literally). Like most Unix commands, `date`
does more than simply output the current date in the format you just
witnessed. You can choose any number of formats and even set the
internal clock to a specific time. Let's explore this a tiny bit.
Commands can take **arguments**. Let's tell the `date` program that we
want the date to be formatted a year-month-day and with
hours-minutes-seconds also. The syntax below will seem arcane, but the
various abbreviations should be obvious.

	date "+%Y-%m-%d %H:%M:%S"

### Manual Pages ###

If you want to learn more information about what `date` can do, you can
either look online or use the Unix built-in manual pages. For a quick
refresher on a command, the manual pages are often easiest. But if you
have no idea what the command does, than you might want to look for
assistance online. To read the manual pages for `date` you use the `man`
command.

	man date

You can page through this with the space bar and exit with `q`. In the
above statement, `man` was the command and `date` was the argument. The
program that let you page through the documentation was another Unix
command that you didn't intentionally invoke, it just happens
automatically when you execute the `man` command.

### Injury Prevention ###

Typing is bad for your health. Seriously, if you type all day, you will
end up with an repetitive stress injury. Don't type for hours at a time.
Make sure you schedule breaks. Unix has several ways to save your
fingers. Let's go back run the `date` program again. Instead of typing
it in, use the **up arrow** on your keyboard to go backwards through
your command history. If you scroll back too far, you can use the **down
arrow** to move forward through your history (but not into the future,
Unix isn't that smart).

	date "+%Y-%m-%d %H:%M:%S"

You can use the **left arrow** and **right arrow** to edit the text on
the command line.

To see your entire history of commands in this session, use the
`history` command.

	history

If you want to repeat a particular command line, you can select a
specific line of your history. For example, to re-run command line #7,
you type the following:

	!7

Probably the most important finger saver in Unix is **tab completion**.
When you hit the tab key, it completes the rest of the word for you. For
example, instead of typing out `history` you can instead type `his`
followed by the tab key, the rest of the word will be completed. If you
use something less specific, can hit the tab key a second time and Unix
will show you the various legal words. Try typing `h` and then the tab
key twice. Those are all the commands that begin with the letter h. We
will use tab completion constantly. Not only does it save you key
presses and time, it also ensures that your spelling is correct. Try
misspelling the `history` command to observe the error it reports.

	historie

### Variables ###

The shell defines various variables which are called **shell variables**
or **environment variables**. For example, the `USER` variable contains
your user name. You can examine the contents of a variable with the
`printenv` command.

	printenv USER

We won't use variables much, but it's important to know they exist
because some programs use them for configuration. If you want to see all
your environment variables, you can use the `printenv` command without
any arguments. Don't worry if this is very confusing because we don't
care about it at this point.

	printenv

## Files & Directories ##

Unix is mostly a text environment. You will be reading and writing a lot
of text files. To do this you will use a text editor. There are many,
many text editors, and some people are insanely passionate about one or
the other. We don't have time for that. We'll use two: **nano**, which
works from your command line interface, and also **gedit** that works
like a word processor.

In Unix, pretty much everything is a file. You need to be able to
create, edit, and delete files and directories to do anything. You can
do some of these things from the graphical desktop interface, but resist
this. The more comfortable you are using the command line for
everything, the better off you will be.

The **file system** is where your files are stored. This could be a hard
disk or other medium, and there could be one or more. To see how much
free space you have on your file system, use the `df` (disk free)
command with the `-h` option to make it more human-readable (try it both
ways).

	df
	df -h

Another useful command is `du -h` (disk usage) which shows how much
space each of your files and directories uses.

### Creating and Viewing Files ###

(For the this exercise and others that follow, it may be useful to have
your graphical desktop displaying the contents of your home directory.
That way you can see that typing and clicking ar related.)

There are a number of ways to create a file. The `touch` command will
create a file or change its modification time (Unix records when the
last time a file was edited) if it already exists.

	touch foo

The file `foo` doesn't contain anything at all. It is completely empty.
Now lets create a file with some content in it.

	cat > bar

After you hit return, you will notice that you do not return to a
command line prompt. Keep typing. Write a bunch of nonsense lines. Keep
going. Write poetry if you must. Everything you're entering at the
keyboard is now going into the file called `bar`. To end the file, you
need to send the end-of-file character, which is control-D. This
character is at the end of every text file. Hit the control key and then
the letter d. Another way of saying this is hit the ^D character. Note
that you don't type the ^ or the capital D. It's just the way we
communicate in writing that one should type the control key and then the
d key.

To see the contents of the file, you can also use the `cat` command.
This dumps the entirety of the file into your terminal.

	cat bar

This isn't very useful for viewing unless you're a speed reader. You can
inspect the first 10 lines of a file with the `head` command.

	head bar

Similarly, you can inspect the last 10 lines with `tail`.

	tail bar

Both of these commands have command line options so that you can see a
different number of lines. For example, to see just the first line you
would do the following:

	head -1 bar

A more useful way to look at files is with a **pager**. The `more` and
`less` commands let you see a file one terminal page at a time. This is
what you used before when viewing the manual page for the `date`
command. Use the spacebar to advance the page and q to quit. `more` and
`less` do more or less the same thing, but oddly enough `less` does more
than `more`.

	less bar

### Editing Files ###

You can edit files with nano or gedit. Let's stay in the terminal and
use nano for now.

	nano bar

This brings up a terminal-based editor. Now you can change the random
text you just wrote. Use the arrow keys to move the cursor around. Add
some text by typing. Remove some text with the delete key. At the
bottom, you can see a menu that uses control keys. To save the file you
hit the ^O key (control and then the letter o). You will then be
prompted for the file name, at which point you can overwrite the current
file (bar) or make a new file with a different name. To exit nano, use
^X. Note, you don't need to give nano an argument when you start it up.

Open up a new terminal. Create a new file called `unix_notes.txt`
(either by touching it first or saving an empty nano file). Use this to
record the various things you've learned today. You might want to go
back to this later. 

Unix file names often have the following properties:

* all lowercase letters
* no spaces in the name (use underscores or dashes instead)
* an extension such as .txt

### Navigating Directories ###

Whenever you are using a terminal, your focus is a particular directory.
The files you just created above were in a specific directory. To
determine what directory you are currently in, use the `pwd` command
(print working directory).

	pwd

 This will tell you your location is `/home/bios180student` (or maybe
 not if you're reading this outside the context of the class or if the
 documentation is out of date - it doesn't matter, this is your home
 directory). The current directory is also known by the single letter `.`
 (that is not the end of the sentence, it's the period character). If
 you want to know what files are in your current working directory, use
 the following command:

	ls .

`ls` will list your current directory if you don't give it an argument,
so an equivalent statement is simply:

	ls

Notice that `ls` reports the files and directories in your current
working directory. It's a little difficult to figure out which ones are
directories right now. So let's add a command line option to the `ls`
command.

	ls -F

This command adds a character to the end of the file names to indicate
what kind of files they are. A forward slash character indicates that
the file is a directory. These directories inside your working directory
are sub-directories. They are **below** your current location. There are
also directories **above** you. There is at most one directory
immediately above you. We call this your parent directory, which in Unix
is called `..` (again, not the end of this sentence, but rather two
period characters together). You can list your parent directory as
follows:

	ls ..

The `ls` command has a lot of options. Try reading the `man` pages and
trying some of them out. Now is a good time to experiment with a few
command line options. Note that you can specify them in any order and
collapse them if they don't take arguments (some options have
arguments). Don't forget to log your learning in your other terminal.

	man ls
	ls -a
	ls -l
	ls -l -a
	ls -a -l
	ls -la
	ls -al

There are two ways to specify a directory: **relative** path and
**absolute** path. Everything so far has been the relative path. The
command `ls ..` listed the directory above the current directory. The
command `nano bar` edited the file `bar` in the current directory. What
if you want to list some directory somewhere else or edit a file
somewhere else? To specify the absolute path, you precede the path with
a forward slash. For example, to list the absolute root of the Unix file
system, you would type the following:

	ls /

To list the contents of /usr/bin you would do the following

	ls /usr/bin

This works exactly the same from whatever your current working directory
is. But this is not true of the relative path.

	ls ..

To change your working directory, you use the `cd` command. Try changing to the root directory

	cd /
	pwd
	ls

Now return to your home directory by executing `cd` without any arguments.

	cd
	pwd
	ls
	
Now go back to the root directory and create a file in your home
directory. There are a couple short-cut ways to do this. The `HOME`
variable contains the location of your home directory. But ~ (tilde) is
another shortcut for the same thing and requires less typing. Note that
to get the contents of the `HOME` variable, we have to precede it with a
`$`.

	cd /
	touch $HOME/file1
	touch ~/file2

Now create a couple more files but using absolute and relative paths
rather than short-cuts.

	touch /home/bios180student/file3
	cd ~/Documents
	pwd
	ls
	touch ../file4

### Moving and Renaming Files ###

Your home directory is starting to fill up with a bunch of crap. Let's
organize that stuff. First off, let's create a new directory for 'Stuff'
using the `mkdir` command.

	cd
	mkdir Stuff

Notice that the directory starts with a capital letter. This isn't
required, but it's a good practice. Now let's move some files into that new directory with the `mv` command.

	mv foo Stuff

If there are 2 arguments and the 2nd argument is not a directory, the
`mv` command will rename the file. Yes, it's weird that `mv` both moves
and renames files. That's Unix.

	mv bar barf
	mv barf Stuff
	ls

You can move more than one file at a time. The last argument is where
you want to move it to.

	mv file1 file2 file3 file4 Stuff
	ls
	ls Stuff

### Copying and Aliasing ###

The `cp` command copies files. Let's say you wanted a copy of barf in
your home directory.

	cp Stuff/barf .
	ls
	ls Stuff

Now you have 2 copies of barf. If you edit one file, it will be
different from the other. Try that with nano.

	nano barf
	# do some editing and save it
	cat barf
	cat Stuff/barf

When you do the copying, you don't have to keep the same name.

	cp Stuff/barf ./bark
	ls

Things are getting a little messy, so let's put these files back into
the Stuff directory. But let's do it using the * wildcard, which is
somewhat magical because it fills in missing letters of arguments. Every
file that starts with `ba` will now be moved to Stuff.

	mv ba* Stuff
	ls

That was just two files, but I think you can imagine the power of moving
100 files with a single command.

An alias is another name for a file. These are often useful to organize
your files and directories. Let's try it using the `ln -s` command (we
always use the `-s` option with `ln`).

	ln -s Stuff/foo ./foof
	nano foof
	# do some editing
	cat foof
	cat Stuff/foo
	
### Deleting Files ###

You delete files with the `rm` command. Be careful, because once gone,
they are gone forever.

	ls Stuff
	rm Stuff/file1
	ls Stuff
	rm foof

You didn't type those file names completely, right? You used tab
completion, right?

You can delete multiple files at once too and even whole directories.
But you're better off using the graphical interface to delete files.
Deleting files is not something we wish you to automate.

### Working with Text Files ###

There are 2 kinds of files: text and binary. A text file looks like the
file you're reading. There are familiar letters, words, and punctuation
(include spaces between words). Binary files don't look like this.
Instead, they look like a bunch of random letters, some of which don't
even display properly on your screen. Let's look at one.

	cat /bin/ls

Yuck. Most of the programs you run on a computer are binary files.
Generally speaking, binary files are for machine consumption and text
files are for human consumption (or readability). Text files come in 3
common flavors. Unix text files have a newline character at the end of
each line. Mac text files generally also use newline characters, but
carriage returns were used in the past and are still sometimes used.
Windows files end in carriage returns plus newlines (they have 2
characters to denote end of line). These differences in line endings can
cause problems when interchanging files among computers. For this
reason, avoid interchanging files between you Linux, Mac, and Windows
computers. **One of the stupidest things you can do is to put sequence
data into Microsoft Word or Excel (or similar software) and then attempt
to use it in Unix.**

Bioinformatics often deals with large text files. These can contain
whole genomes, massive RNA-seq experiments, or thousands of spectra. You
need to appreciate the size of these files so that you don't do stupid
stuff with them, like email them to a colleague. Let's look at the
Arabidopsis thaliana genome. First, let's see how big it is. We'll use
the `ls` with the `-h` and `-l` options so that we can see the size of
the file. Please use tab completion when typing the following.

	ls -lh /data/C.elegans

You should see something that looks similar to this:

	-rw------- 1 ian  staff    29M Nov 26 14:41 c_elegans.PRJNA13758.WS240.genomic.fa.gz
	-rw------- 1 ian  staff   5.9M Oct  9 21:06 c_elegans.PRJNA13758.WS240.protein.fa.gz

There are two files, one contains genomic sequence, the other contains
protein. The genome is 29 megabytes. That's not a very big file, but
it's too big to email. A knee-jerk reaction might be to open this in
your text editor. That's a bad idea for several reasons: (1) You
shouldn't edit data files. (2) It takes way a lot more memory to edit a
file than view its contents. (3) The file is binary. Let's do it anyway.
Use tab completion to do the following.

	nano /data/C.elegans/c_elegans.PRJNA13758.WS240.genomic.fa.gz

The file is binary, so it looks like gibberish. We need to uncompress it
to see its contents. The file name is also hopelessly long. Let's
organize ourselves a little. First, let's create a directory where we
can collect our work.

	mkdir ~/Project0
	cd ~/Project0

The path to the genome file is long. We can simplify it with an alias.

	ln -s /data/C.elegans/c_elegans.PRJNA13758.WS240.genomic.fa.gz ./genome.gz
	ls -lF

Note what `ls -lF` shows you. The `@` symbol trailing the file name
shows you that the file is an alias. The arrow shows you what the alias
points to.

Now let's start uncompressing it. The `gunzip` command uncompresses
files. If we want to stream the file to the terminal in a way similar to
`cat` we use `gunzip -c`.

	gunzip -c genome.gz

When you get sick of watching the text scroll by, you can interrupt it
with a ^C (control-c). ^C is a good way to interrupt a runaway process.
But sometimes it doesn't work and you may have better luck with ^Z,
which sleeps the process (yes, just like the Borg). More on that later.

Sometimes we want to look at the first few lines of a file without
committing ourselves to the whole file. `head` is great for that.

	head genome.gz

Rats, it's still binary. What would be great is if we could uncompress
the file and view the contents with `head`. One of the awesome powers of
Unix is that you can pipeline the output of one program to the input of
another with the pipe `|` token. This might look like a capital I or
lowercase l, but it's not, it's its own strange beast located somewhere
where you right pinkie can access it.

	gunzip -c genome.gz | head

Success. The first line of the file is a FASTA header and this is
followed by a bunch of sequence lines. If you don't know what the FASTA
format is, now is a good time to read about the FASTA format online.

FASTA files sometimes contain multiple sequences. As this file
represents the C. elegans genome, we expect 6 chromosomes. Let's look
for those in the file.

	gunzip -c genome.gz | less

Now we can page through the file looking for lines that start with `>`.
As you page through the file, note how long the chromosome is. It will
take you over 12,000 more spacebar presses to get to the next chromosome
(assuming your terminal is still 24 lines). Remember, this is a small
genome. One of the features of `less` is that it allows you to search
for simple patterns. Hit the forward-slash key `/` to bring up the
search prompt at the bottom of the terminal. Now hit the `>` key and
press return. `less` will find the next `>` symbol in the file. Keep
hitting the `/` key and return. `less` remembers the last pattern.

If you need to find patterns in files, the Unix `grep` command is often
the first tool people turn to.

	gunzip -c genome.gz | grep ">"

Now let's save that output to a file. You can redirect the output of a
program to a file with the `>` token.

	gunzip -c genome.gz | grep ">" > chromosomes.txt
	cat chromosomes.txt

You will be creating a lot of files in this course. Sometimes they will
be large. Use `gzip` and `gunzip` as needed. `gzip` usually makes a file
between 50% and 25% its size, so it's a great way to save space,
especially when you start to work with large -omic data files.

	gzip chromosomes.txt
	ls -l
	gunzip chromosomes.txt
	ls -l

Note that `gzip` automatically adds and removes the `.gz` file extension
appropriately.

In Unix, when people send you multiple files, they generally send them
as a **tar ball**. The `tar` command creates archives, which are single
files that contain multiple files. Let's create a bunch of files in this
directory.

	touch file1 file2 file3 file4 file5

Now let's `cd` up a directory and have a look around.

	cd ..
	ls
	ls Project0

To create an archive of Project0, we need to tell the `tar` command that
we want to create the archive with the `-c` option and tell it the name
of the file with the `-f` option.

	tar -c -f project0.tar Project0

Unix options generally go before the arguments on the command line.
That's why `-f project0.tar` goes before `Project0`. You can collapse
single letter options if you're lazy. So the following command is the
same thing.
 
 	tar -cf project0.tar Project0
 	ls

To save space on your file system, you should compress your tar-balls.

	gzip project0.tar
	ls

The `tar` command will do this automatically with the `-z` option. So
when you want to create a tar-ball, the one-liner is as follows:

	tar -czf project0.tar.gz Project0

To decompress a tar-ball, you swap the `-c` option for the `-x` option.
Before we do that, let's create a new directory and inflate the tar-ball
in there so that we make a copy and don't overwrite our original
directory.

	mkdir Stuff
	mv project0.tar.gz Stuff
	cd Stuff
	tar -xzf project0.tar.gz
	ls
	ls Project0

### Using File Permissions ###

A file can have 3 kinds of permissions: read, write, and execute. These
are abbreviated as `rwx` when you do a `ls -l`. Read and write are
obvious, but execute is a little weird. Programs and directories need
executable permission to access them. Important data files, like the
genome of C. elegans, should not be edited. To ensure that, they should
have read only permission. Every file has permissions for the user,
group, and public. So a file can be readable by you and inaccessible to
the public. Let's look at one of the files we just created.

	ls -lF chromosomes.txt

This will produce something like the following, which shows the
permissions, owner (ian), group (staff), size (29 bytes), date, and file
name. 

	-rw-r--r--  1 ian  staff    29B Mar 26 11:11 chromosomes.txt

Let's first turn on all permissions for everyone.

	chmod 777 chromosomes.txt

The explanation of what this does will have to wait for a bit. The file now has the following properties.

	-rwxrwxrwx  1 ian  staff    29B Mar 26 11:11 chromosomes.txt*

The first character is a hyphen. This means the file is an ordinary
file. If the file was a directory, the letter would be a d. If it was an
alias, the letter would be an l. The 3 rwx symbols that follow are the
read, write, and execute permissions for user, group, and public. So
everyone has permission to read, write, and execute this file. If you
copy files from a USB flash drive, it will typically have all these
permissions because the file system on most flash drives is not
Unix-based. Having all permissions on is generally not a good idea. Most
files fit into one of a few categories.

| Category   | Code         | Oct | Meaning 
|:-----------|:-------------|:----|-----------------------------------------
| raw data   | `-r--r--r--` | 444 | anyone can read, nobody can write
| private    | `-rw-------` | 600 | I can read/write, others nothing
| shared     | `-rw-r--r--` | 644 | I can read/write, group/public can read
| shared     | `-rw-rw-r--` | 664 | We can read/write, public can read

You can change the permissions of a file with the `chmod` command. There
are two different syntaxes. The more human readable one looks like this.

	chmod u-x chromosomes.txt

This command says "change the user (u) to remove (-) the execute (x)
permission from file chromosmes.txt". You add permissions with +.

	chmod u+x chromosomes.txt

The octal format is convenient because it changes all of the permissions
at once, but can be confusing for people who don't think in octal. 4 is
the read permission. 2 is the write permission. 1 is the execute
permission. Each rwx corresponds to one octal number from 0 to 7. So
`chmod 777` turns on all permissions for all types of people and
`chmod 000` turns them all off. I generally use only two permissions:
444 and 644. That is, everything is readable, but somethings only I can
write.

## Processes ##

One of the most important programs in Unix is `top` because it lets us
monitor the health of our computer. Open up a new terminal and start the
program.

	top

On Unix systems, `top` is the equivalent of the the Task Manger in
Windows and the Activity Monitor in Mac OS. Once you start running
bioinformatics software on your computer, you can monitor what is
happening using `top`. 

### Viewing Processes ###

Let's go back to an previous command and watch it with `top`. Notice
that it doesn't use 100% of the CPU.

	gunzip -c genome.gz

Let's do that one more time, and this time we will use the `time`
command to determine the elapsed and CPU time.

	time gunzip -c genome.gz

On my computer, I get the following stats

	real    0m6.930s
	user    0m0.483s
	sys     0m0.859s

It took about 7 seconds to stream the contents to my terminal. The CPU
time is the sum of the user and sys time. Why did it take so much more
real time than CPU time? Because it takes some time to display to the
terminal, during which the CPU isn't very busy. Let's try the same task
and send the output to a file.

	time gunzip -c genome.gz > foo

Big difference!

	real    0m0.413s
	user    0m0.357s
	sys     0m0.056s

Sometimes we don't even need to see the output. In this case, we can
redirect the output to `/dev/null` which is Unix's black hole (not even
electrons escape).

	time gunzip -c genome.gz > /dev/null

Faster still because we don't have to write to the file system.

	real    0m0.356s
	user    0m0.348s
	sys     0m0.009s

Note that the CPU time is slightly greater than the real time. How can
something take less wall clock time than CPU time? Are we violating the
laws of physics? No, your computer has more than one core and can split
up tasks on various cores. For programs that can utilize multiple cores,
the real time may be much less than the CPU time.

### Managing Processes ###

Sometimes you will start a program and decide you want to stop it
permanently or temporarily. Run the following command and then watch
what happens in `top`. You may find it useful to copy-paste this command
from the document to your terminal to make sure you don't introduce
spelling errors.

	perl -e 'while(1){print $i++, chr(10)}'

This command is an endless loop in the Perl programming language that
counts from 0 to some very large number. You cannot do anything useful
in your terminal until the program stops, which unfortunately, is a long
time from now. Fortunately, we can break out of the program with ^C. Do
that now.

But what if you just wanted to pause the program and restart it again?
You can do that with ^Z. So let's go back and execute that command again
(use the up arrow) and this time send it a sleep signal.

	perl -e 'while(1){print $i++, chr(10)}'

Now hit ^Z. To get it to pick up where it left off, use the `fg` command
to put the process into the **foreground**.

	fg

Now go look at `top`. You should see a perl process using a lot of CPU.
Every process (program) on your computer has a process ID (PID). If you
know the PID of a process, you can take control of it (assuming it is
yours). My perl process has PID 6000. On yours it is probably different.
You can view all your processes with the `ps` command. In the following
command, replace `ian` with your user name: `bios180student`.

	ps -u ian

However you attain the PID of your offending process, you can `kill` it.
Replace `6000` with your PID.

	kill 6000

You can put processes into the **background**. This will mean the
terminal no longer controls them. You can't ^C to interrupt such a
process, but you can use the `kill` command. Add `&` to the end of a
command line to put it into the background or use the `bg` command to
put a paused process into the background. You shouldn't need to do these
things in this class, but we include this info for completeness.

## Unix Reference ##

| Token  | Function
|:--------|:-------------------------------------|
| .       | your current directory (see pwd)
| ..      | your parent directory
| ~       | your home directory (also $HOME)
| ^c      | send interrupt signal to current process
| ^d      | send end-of-file character
| ^z      | send sleep signal current process: see bg and fg
| tab     | tab-complete names
| *       | wildcard - matches everything
| &       | send command to background
| \|      | pipe output from one command to another
| >       | redirect output to file

| Command   | Example       | Intent                        |
|:----------|:--------------|:------------------------------|
| `bg`      | `bg`          | send a sleeping process to background
| `cat`     | `cat > f`     | create file f and wait for keyboard (see ^d)
|           | `cat f`       | stream contents of file f to STDOUT
|           | `cat a b > c` | concatenate files a and b into c
| `cd`      | `cd d`        | change to relative directory d
|           | `cd ..`       | go up one directory
|           | `cd /d`       | change to absolute directory d
| `chmod`   | `chmod 644 f` | change file permissions 
|           | `chmod u+x f` | change file permissions
| `cp`      | `cp f1 f2`    | make a copy of file f1 called f2
| `cut`     | `cut -f 5 ff` | print column 5 from file ff
| `date`    | `date`        | print the current date
| `df`      | `df -h .`     | display free space on file system
| `du`      | `du -h ~`     | display the sizes of your files
| `fg`      | `fg`          | send sleeping process to foreground
| `grep`    | `grep p f`    | print lines with the letter p in file f
| `gzip`    | `gzip f`      | compress file f
| `gunzip`  | `gunzip f.gz` | uncompress file f.gz
| `head`    | `head f`      | display the first 10 lines of file f
|           | `head -2 f`   | display the first 2 lines of file f
| `history` | `history`     | display the recent commands you typed
| `kill`    | `kill 1023`   | kill process with id 1023
| `less`    | `less f`      | page through a file
| `ln`      | `ln -s f1 f2` | make f2 an alias of f1
| `ls`      | `ls`          | list current directory
|           | `ls -l`       | list with file details
|           | `ls -la`      | also show invisible files
|           | `ls -lta`     | sort by time instead of name
|           | `ls -ltaF`    | also show file type symbols
| `man`     | `man ls`      | read the manual page on ls command
| `mkdir`   | `mkdir d`     | make a directory named d
| `more`    | `more f`      | page through file f (see less)
| `mv`      | `mv foo bar`  | rename file foo as bar
|           | `mv foo ..`   | move file foo to parent directory
| `nano`    | `nano`        | use the nano text file editor
| `passwd`  | `passwd`      | change your password
| `pwd`     | `pwd`         | print working directory
| `ps`      | `ps`          | show current processes
|           | `ps -u ian`   | show processes user ian is running
| `rm`      | `rm f1 f2`    | remove files f1 and f2
|           | `rm -r d`     | remove directory d and all files beneath
|           | `rm -rf /`    | destroy your computer
| `rmdir`   | `rmdir d`     | remove directory d
| `sort`    | `sort f`      | sort file f alphabetically by first column
|           | `sort -n f`   | sort file f numerically by first column
|           | `sort -k 2 f` | sort file f alphabetically by column 2
| `ssh`     | `ssh hal`     | remotely log into machine hal
| `tail`    | `tail f`      | display the last 10 lines of file f
|           | `tail -f f`   | as above and keep displaying if file is open
| `tar`     | `tar -cf ...` | create a compressed tar-ball (-z to compress)
|           | `tar -xf ...` | decompress a tar-ball (-z if compressed)
| `time`    | `time ...`    | determine how much time a process takes
| `top`     | `top`         | display processes running on your system
| `touch`   | `touch f`     | update file f modification time (create if needed)
| `wc`      | `wc f`        | count the lines, words, and characters in file f
