# Exercise 15: Reading Files
## Study Drills
### Above each line, write out in English what that line does.
See ```ex15.py``` for details.

Output is shown below:
```
(venv)marclaughton at MacBookPro in ~/Development/Projects/Learn_Python_The_Hard_Way/Ex15 on exercise-15*
 ➜  python ex15.py ex15_sample.txt
Here's your file 'ex15_sample.txt'
We are now no longer the Knights who say Ni.
NI.
Shh...
We are now the Knights who say...'Ekki-ekki-ekki-ekki-PTANG. Zoom-Boing, z'nourrwringmm.'

Type the filename again:
> ex15_sample.txt
We are now no longer the Knights who say Ni.
NI.
Shh...
We are now the Knights who say...'Ekki-ekki-ekki-ekki-PTANG. Zoom-Boing, z'nourrwringmm.'

```
### If you are not sure ask someone for help or search online. Many times searching for "python THING" will find answers to what that THING does in Python. Try searching for "python open."
Using ```python open``` was interpreted as a command, resulting in the following error:

```
(venv)marclaughton at MacBookPro in ~/Development/Projects/Learn_Python_The_Hard_Way on exercise-15*
 ➜  python open
python: can't open file 'open': [Errno 2] No such file or directory
```

Personally, I might tend to use something like this more often: ```pydoc open```.

### I used the word "commands" here, but commands are also called "functions" and "methods." You will learn about functions and methods later in the book.
Noted, I'm familiar with this convention and use functions and methods interchangeably at work.

### Get rid of the lines 10-15 where you use ```raw_input``` and run the script again.
Running the script without the prompt section resulted in the script running (i.e., executing the read method on the file) without any further output or input.

### Use only ```raw_input``` and try the script that way. Why is one way of getting the filename better than another?
See ```ex15_alternate.py``` for full details.

Output:
```
(venv)marclaughton at MacBookPro in ~/Development/Projects/Learn_Python_The_Hard_Way/Ex15 on exercise-15*
 ➜  python ex15_alternate.py
Type the name of the file you'd like to open:
> ex15_sample.txt
We are now no longer the Knights who say Ni.
NI.
Shh...
We are now the Knights who say...'Ekki-ekki-ekki-ekki-PTANG. Zoom-Boing, z'nourrwringmm.'
```

In this study drill, abandoning the argv assignment and allowing the filename to be assigned via the ```raw_input``` method feels more modular and less brittle.
With the ```filename``` listed as a param in the argv array, this forces the user either know to enter the filename param at script runtime or encounter an error warning - not the best user experience.

Using just the ```raw_input``` makes for a better UX, in my opinion.

### Start ```python``` to start the ```python``` shell, and use ```open``` from the prompt just like in this program. Notice how you can open files and run ```read``` on them from within ```python```?
```
(venv)marclaughton at MacBookPro in ~/Development/Projects/Learn_Python_The_Hard_Way/Ex15 on exercise-15*
 ➜  python
Python 2.7.10 (default, Sep 23 2015, 04:34:14)
[GCC 4.2.1 Compatible Apple LLVM 7.0.0 (clang-700.0.72)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> open('ex15_sample.txt').read()
"We are now no longer the Knights who say Ni.\nNI.\nShh...\nWe are now the Knights who say...'Ekki-ekki-ekki-ekki-PTANG. Zoom-Boing, z'nourrwringmm.'\n"
>>> exit()
```
### Have your script also call ```close()``` on the ```txt``` and ```txt_again``` variables. It's important to close files when you are done with them.
See lines 24 and 25 in ```ex15.py``` and line 10 in ```ex15_alternate.py```.

After encountering an error in the way I was handling the file itself and the content representing its content, I was able to successfully refactor my code.

Original:
```
from sys import argv

script = argv

print 'Type the name of the file you\'d like to open: '
text = raw_input('> ')

print open(text).read()

text.close()
```

Refactor:
```
from sys import argv

script = argv

print 'Type the name of the file you\'d like to open: '
filename = open(raw_input('> '))

file_content = filename.read()

print file_content

filename.close()
```
