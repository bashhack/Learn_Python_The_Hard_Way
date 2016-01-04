# Exercise 17: More Files
## Study Drills
### This script is really annoying. There's no need to ask you before doing the copy, and it prints too much out to the screen. Try to make the script more friendly to use by removing features.
The original script can be found in ```ex17.py```. Interacting with the original script is shown here:
```
(venv)marclaughton at MacBookPro in ~/Development/Projects/Learn_Python_The_Hard_Way/Ex17 on exercise-17*
 ➜  echo 'This is a test file.' > test.txt
(venv)marclaughton at MacBookPro in ~/Development/Projects/Learn_Python_The_Hard_Way/Ex17 on exercise-17*
 ➜  cat test.txt
This is a test file.
(venv)marclaughton at MacBookPro in ~/Development/Projects/Learn_Python_The_Hard_Way/Ex17 on exercise-17*
 ➜  python ex17.py test.txt new_file.txt
Copying from test.txt to new_file.txt
The input file is 21 bytes long.
Does the output file exist? False
Ready, hit RETURN to continue, or CTRL-C to abort.

Alright, all done.
```
### See how short you can make the script. I could make this one line long.
### Notice at the end of the What You Should See I used something called ```cat```? It's an old command that "con*cat*enates" files together, but mostly it's just an easy way to print a file to the screen. Type ```man cat``` to read about it.
### Find out why you had to write ```out_file.close()``` in the code.
### Go read up on Python's ```import``` statement, and start ```python``` to try it out. Try importing some things and see if you can get it right. It's alright if you do not.
