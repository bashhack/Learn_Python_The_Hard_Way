# Exercise 13: Parameters, Unpacking, Variables
## Study Drills
### Try giving fewer than three arguments to your script. See that error you get? See if you can explain it.
Result of passing fewer arguments than variables assigned to the ```argv```(argument variable) object:
```
(venv)marclaughton at MacBookPro in ~/Development/Projects/Learn_Python_The_Hard_Way/Ex13 on develop*
 ➜  python ex13.py one
Traceback (most recent call last):
  File "ex13.py", line 3, in <module>
    script, first, second, third = argv
ValueError: need more than 2 values to unpack
```

Result of passing more arguments than variables assigned to the ```argv```(argument variable) object:
```
(venv)marclaughton at MacBookPro in ~/Development/Projects/Learn_Python_The_Hard_Way/Ex13 on develop*
 ➜  python ex13.py one two three four
Traceback (most recent call last):
  File "ex13.py", line 3, in <module>
    script, first, second, third = argv
ValueError: too many values to unpack
```
### Write a script that has fewer arguments and one that has more. Make sure you give the unpacked variables good names.
See ```small_argv.py``` and ```large_argv.py``` for details.

The respective outputs:

```
(venv)marclaughton at MacBookPro in ~/Development/Projects/Learn_Python_The_Hard_Way/Ex13 on develop*
 ➜  python small_argv.py Cython magical
The script is called: small_argv.py
Python is so cool! And Cython is magical.
```

```
(venv)marclaughton at MacBookPro in ~/Development/Projects/Learn_Python_The_Hard_Way/Ex13 on develop*
 ➜  python large_argv.py 'roast beef' mayo mustard cherries whole_wheat swiss
The sandwhich making script is called: large_argv.py
Your meat is: roast beef
Your first condiment is: mayo
Your second condiment is: mustard
Your side of fruit is: cherries
Your bread is: whole_wheat
Your cheese is: swiss
Your roast beef, mayo, mustard, whole_wheat, swiss sandwhich sounds tasty. Especially with a side of cherries.
```
### Combine raw_input with argv to make a script that gets more input from a user.
See ```prompt_argv.py``` for more details.

Output show here:
```
(venv)marclaughton at MacBookPro in ~/Development/Projects/Learn_Python_The_Hard_Way/Ex13 on develop*
 ➜  python prompt_argv.py 7.5 5
How many people are coming over? 10
Well, we'll just have 2 sad appleless people.
Or, we could share? That'd be 0.8 for each.
Well, 0.7500 apples per person, to be exact
Hopefully, they will like these 5 pineapples, instead?
```
### Remember that modules give you features. Modules. Modules. Remember this because we'll need it later.
As a programmer and musician, I was pleased to discover some of the awesome built-in modules for working with audio:
[Python Multimedia Services Modules](https://docs.python.org/3/library/mm.html)
