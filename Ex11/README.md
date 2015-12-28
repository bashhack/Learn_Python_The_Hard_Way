# Exercise 11: Asking Questions
## Study Drills
### Go online and find out what Python's raw_input does.
Per the Python documentation:

>If the prompt argument is present, it is written to standard output without a
trailing newline. The function then reads a line from input, converts it to a
string (stripping a trailing newline), and returns that. When EOF is read,
<code>EOFError</code> is raised.

### Can you find other ways to use it? Try some of the samples you find.
In ```get_input.py```, I am showing how I might convert the user input to
type ```int``` for later processing and handling.

Output:
```
(venv)marclaughton at MacBookPro in ~/Development/Projects/Learn_Python_The_Hard_Way/Ex11 on develop*
 ➜  python get_input.py
Type your favorite number: 7
What would you like to multiply your favorite number 7 by?
--> 47
The result of the operation is 329.
```
### Write another "form" like this to ask some other questions.
See ```get_info.py``` for more details.

Output:
```
(venv)marclaughton at MacBookPro in ~/Development/Projects/Learn_Python_The_Hard_Way/Ex11 on develop*
 ➜  python get_info.py
What is your name? Marc
Where were you born? San Francisco
What is your favorite sport? hockey
So, your name is Marc, born in San Francisco, and you like hockey
```
### Related to escape sequences, try to find out why the last line has '6\'2"' with that \' sequence. See how the single-quote needs to be escaped because otherwise it would end the string?
Yes, this makes sense given the way the interpreter has been written to handle strings.
