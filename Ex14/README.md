# Exercise 14: Prompting and Passing
## Study Drills
### Find out what Zork and Adventure were. Try to find a copy and play it.
OMG - wow, these brings back memories - great text-based CLI games.

Zork, in particular, is a favorite of mine. Collosal Cave Adventure is also good,
and there's a great port of it to Python3 here [Python Package](https://pypi.python.org/pypi/adventure/1.3)

For ease of install, I used pip: ```pip install adventure```
### Change the ```prompt``` variable to something else entirely.
See ```prompt_extended.py```, where I updated the prompt to look like this:

```
Please enter your response here, I'm waiting:

     (~'~~'~~'~~)
      |        |
      |        |
      |       ~|~                         _ __
      |-------())                        ||  |
      (        _)                      .'~\  /.
      |        |                     ()()__\/ ".
      |        |                     /*        "
      ''..     |                     |     //  |
      |'..'---_/\                    |    ()   |
     /    ''---|| /\                 ".       ."
    /     \    \/\/                   "..  ."\
    |  \  /     \_/                      || |  ^
    |   \/\    | \-ABG                 ((__)-ABG

==================================================
>
```

### Add another argument and use it in your script, the same way you did in the previous exercise with ```first, second = ARGV```.
See ```prompt_extended.py```.

Output below:
```
(venv)marclaughton at MacBookPro in ~/Development/Projects/Learn_Python_The_Hard_Way/Ex14 on develop*
 ➜  python prompt_extended.py Marc 'Software Developer'
Hi Marc-Software Developer, I'm the prompt_extended.py script.
I'd like to ask you a few questions.
Do you like me, Marc?
Please enter your response here, I'm waiting:

     (~'~~'~~'~~)
      |        |
      |        |
      |       ~|~                         _ __
      |-------())                        ||  |
      (        _)                      .'~\  /.
      |        |                     ()()__\/ ".
      |        |                     /*        "
      ''..     |                     |     //  |
      |'..'---_/\                    |    ()   |
     /    ''---|| /\                 ".       ."
    /     \    \/\/                   "..  ."\
    |  \  /     \_/                      || |  ^
    |   \/\    | \-ABG                 ((__)-ABG

==================================================
> Yeah, you're the best!
Where do you live, Marc?
> Austin, TX
What kind of computer do you have?
> Macbook Pro

Which operating system do you fancy?
Type (1) for Mac OSX
Type (2) for Windows
Type (3) for Linux (any distro)

Please enter your response here, I'm waiting:

     (~'~~'~~'~~)
      |        |
      |        |
      |       ~|~                         _ __
      |-------())                        ||  |
      (        _)                      .'~\  /.
      |        |                     ()()__\/ ".
      |        |                     /*        "
      ''..     |                     |     //  |
      |'..'---_/\                    |    ()   |
     /    ''---|| /\                 ".       ."
    /     \    \/\/                   "..  ."\
    |  \  /     \_/                      || |  ^
    |   \/\    | \-ABG                 ((__)-ABG

==================================================
> 1
Hey, excellent choice!

Alright, so you said "Yeah, you're the best!" about liking me.
You live in 'Austin, TX'. Not sure where that is.
And you have a 'Macbook Pro' computer. Nice.
```
### Make sure you understand how I combined a ```"""```` style multiline string with the ```%``` format activator as the last print.
Yes, this makes sense - as before, we can incorporate string interpolation with any string (multiline or otherwise). Doing so allows
us to pass any number of params for an equal number of string formatters within the body of the string.

Output shown below:
```
(venv)marclaughton at MacBookPro in ~/Development/Projects/Learn_Python_The_Hard_Way/Ex14 on develop*
 ➜  python ex14.py Marc
Hi Marc, I'm the ex14.py script.
I'd like to ask you a few questions.
Do you like me, Marc?
> sure, well enough I suppose
Where do you live, Marc?
> Austin, TX
What kind of computer do you have?
> Macbook Pro and a Macbook Air

Alright, so you said 'sure, well enough I suppose' about liking me.
You live in 'Austin, TX'. Not sure where that is.
And you have a 'Macbook Pro and a Macbook Air' computer. Nice.
```
