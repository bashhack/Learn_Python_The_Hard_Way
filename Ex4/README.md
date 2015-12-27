# Exercise 4: Variables and Names
## Study Drills
### Explain this error in your own words, make sure you use line numbers and explain why
```
Traceback (most recent call last):
  File "ex4.py", line 8, in <module>
    average_passengers_per_car = car_pool_capacity / passenger
NameError: name 'car_pool_capacity' is not defined
```

In line 7 of Zed's script, the variable ```carpool_capacity``` was defined initially. When used on line 8 (in this example),
 the variable was misspelled, leading the interpreter to throw an undefined error.
### I used 4.0 for ```space_in_a_car```, but is that necessary? What happens if it's just 4?
Original output(with float):
```
(venv)marclaughton at MacBookPro in ~/Development/Projects/Learn_Python_The_Hard_Way/Ex4 on develop*
 ➜  python ex4.py
There are 100 cars available.
There are only 30 drivers available.
There will be 70 empty cars today.
We can transport 120.0 people today.
We have 90 to carpool today.
We need to put about 3 in each car.
```

Revised output(without float):
```
(venv)marclaughton at MacBookPro in ~/Development/Projects/Learn_Python_The_Hard_Way/Ex4 on develop*
 ➜  python ex4.py
There are 100 cars available.
There are only 30 drivers available.
There will be 70 empty cars today.
We can transport 120 people today.
We have 90 to carpool today.
We need to put about 3 in each car.
```

In this case, because the values we are dealing with are integer values to begin with that will result in integer values, it's not necessary.
However, if we were dealing with values that could include floats (as it is now, something like 100.5 cars available wouldn't make much sense, of course!) or return floats, it would be of benefit.
### Remember that 4.0 is a ```floating point``` number. It's just a number with a decimal point, and you need 4.0 instead of just 4 so that it is floating point.
Duly noted, though it should be mentioned that we could also write:

```
cars = 100
space_in_a_car = float(4)
# Code continues after this....
```
### Write comments above each of the variable assignments.

### Make sure you know what ```=``` is called (equals) and that it's making names for things.
Of course, ```=``` is used as a means of assignment while ```==``` is a means of checking for equality.
### Remember that ```_``` is an underscore character.
In addition to its use in throwaway variable names, in the Python interpreter it stores the result of the last executed statement in the session (see README file for Exercise 4).
### Try running ```python``` from the Terminal as a calculator like you did before and use variable names to do your calculations. Popular variable names are also ```i```, ```x```, and ```j```.
```
(venv)marclaughton at MacBookPro in ~/Development/Projects/Learn_Python_The_Hard_Way/Ex4 on develop*
 ➜  python
Python 2.7.10 (default, Sep 23 2015, 04:34:14)
[GCC 4.2.1 Compatible Apple LLVM 7.0.0 (clang-700.0.72)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> x = 5
>>> j = 4
>>> j + x
9
>>> x - j
1
>>> i = -3
>>> i * x / j
-4
>>> j / i + x
3
```
