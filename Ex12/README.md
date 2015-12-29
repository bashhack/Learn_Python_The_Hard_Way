# Exercise 12: Prompting People
## Study Drills
### In Terminal where you normally run ```python``` to run your scripts, type ```pydoc raw_input```. Read what it says. If you're on Windows try ```python -m pydoc raw_input``` instead.
Oh, thank goodness! Pydoc is to Python as the man-pages project is to Linux! I can't believe I've been going to my browser bookmark by habit when there was a CLI the whole time (and I love CLI for faster workflow).

```
Help on built-in function raw_input in module __builtin__:

raw_input(...)
    raw_input([prompt]) -> string

    Read a string from standard input.  The trailing newline is stripped.
    If the user hits EOF (Unix: Ctl-D, Windows: Ctl-Z+Return), raise EOFError.
    On Unix, GNU readline is used if enabled.  The prompt string, if given,
    is printed without a trailing newline before reading.
```

Also, how cool is this? ```pydoc -p {xxxx}``` where {xxxx} is a port param also hosts a local Python web server with the docs.

![mind-blown](http://media0.giphy.com/media/EldfH1VJdbrwY/giphy.gif)
### Get out of pydoc by typing ```q``` to quit.
Gotcha - makes sense!
### Look online for what the ```pydoc``` command does.
See previous answer provided above - however, let me also add that per the docs, ```pydoc``` also seems to pull up the docs relevant to your current environment/path.
If I'm running a virtual environment with Python3, and have already run ```source venv/bin/activate```, the ```pydoc``` command will show Python3 docs.
### Use pydoc to also read about ```open```, ```file```, ```os```, and ```sys```. It's alright if you do not understand those; just read through and take notes about interesting things.
While reading the docs on ```file```, the following was helpful to remember:

```
The mode can be 'r', 'w' or 'a' for reading (default), writing or appending.
```

```
The preferred way to open a file is with the builtin open() function.
```

While reading the docs on ```open```, it's good to be reminded that there is a param for ```buffering``` which I have never used. Taking the opportunity to read up on how this works lead
to a great exploration of POSIX system architecture, which was very cool!

Finally, reading the docs on ```sys``` was helpful as I've been working on C programming lately, and some of the same commands which I might find useful to investigate the state of the currently
running script are all here (i.e., things like ```path```, ```module```, and ```argv```). Additionally, the quick and easy access to some really useful static objects available in sys was helpful.
