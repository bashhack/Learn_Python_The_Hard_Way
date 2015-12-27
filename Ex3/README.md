# Exercise 3: Numbers and Math
## Study Drills
### Above each line, use the ```#``` to write a comment to yourself explaining what the line does.
See ```ex3.py``` for completed code comments.
### Remember in Exercise 0 when you started ```python```? Start ```python``` this way again and using the math operators, use Python as a calculator.
```
(venv)marclaughton at MacBookPro in ~/Development/Projects/Learn_Python_The_Hard_Way on develop*
 ➜  python
Python 2.7.10 (default, Sep 23 2015, 04:34:14)
[GCC 4.2.1 Compatible Apple LLVM 7.0.0 (clang-700.0.72)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 4 + 2
6
>>> 654 - _
648
>>> 24853 / _
38
>>> 2 * _
76
>>> _ % 3
1
>>> _ < 5
True
>>> 1 > 5
False
>>> 1 <= 1
True
>>> 1 >= 2
False
```
### Find something you need to calculate and write a new ```.py``` file that does it.
Please see ```calculate_mortage.py``` for my program code.

Output:
```
(venv)marclaughton at MacBookPro in ~/Development/Projects/Learn_Python_The_Hard_Way/Ex3 on develop*
 ➜  python calculate_mortage.py
$ 1182.04
```
### Notice the math seems "wrong"? There are no fractions, only whole numbers. You need to use a "floating point" number, which is a number with a decimal point, as in 10.5, or 0.89, or even 3.0.
This is primarily evident in the program when we encounter ```1 / 4``` and the result is ```0``` rather than the float ```0.25```. The Python interpreter (in my case, I am running a virtual environment at 2.7.10) is simply truncating the decimal values.

In Python3, we can simply get the expected result without having to utilize the two workarounds (so - that's good news, huzzah!) available to us in Python <= 2.7:

- Workaround 1 - convert either the dividend or divisor value
    - float(num1)/num2 || num1/float(num2)
- Workaround 2 - import division class from future library
    - include ```import __future__ from division

### Rewrite ```ex3.py``` to use floating point numbers so it's more accurate. 20.0 is floating point.
See ```ex3_float_rewrite.py``` for complete code.

The output of ```ex3.py``` is shown here:
```
(venv)marclaughton at MacBookPro in ~/Development/Projects/Learn_Python_The_Hard_Way/Ex3 on develop*
 ➜  python ex3.py
I will now count the guitars:
Fenders 3
Gibsons 97
Now I will count the strings:
7
Is it true that 3 + 2 < 5 - 7?
False
What is 3 + 2 5
What is 5 - 7 -2
Of course that's why it's FALSE.
How about some more?
Is it greater? True
Is it greater or equal? True
Is it less or equal? False
```
The output of ```ex3_float_rewrite.py``` is shown here:
```
(venv)marclaughton at MacBookPro in ~/Development/Projects/Learn_Python_The_Hard_Way/Ex3 on develop*
 ➜  python ex3_float_rewrite.py
I will now count the guitars:
Fenders 3.66666666667
Gibsons 97.0
Now I will count the strings:
6.75
Is it true that 3 + 2 < 5 - 7?
False
What is 3 + 2 5.0
What is 5 - 7 -2.0
Of course that's why it's FALSE.
How about some more?
Is it greater? True
Is it greater or equal? True
Is it less or equal? False
```
