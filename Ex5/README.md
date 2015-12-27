# Exercise 5: More Variables and Printing
## Study Drills
### Change all the variables so there is no ```my_``` in front of each one. Make sure you change the name everywhere, not just where you used ```=``` to set them.
Modified script:
```
name = 'Marc Laughton'
age = 29
height = 75
weight = 220
eyes = 'Brown'
favorite_color = 'Blue'
other_favorite_color = 'Green'
hair = 'Brown'

print 'Let\'s talk about %s.\n' % name
print 'He\'s %d inches tall.\n' % height
print 'He weighs %d pounds.\n' % weight
print 'He was asked to play football in high school and college,\n\
but instead played jazz guitar, wrote poetry, and tinkered with code.\n'
print 'He\'s got %s eyes and %s hair.\n' % (eyes, hair)
print 'His favorite color is usually %s, unless it\'s Friday,\
in which case it\'s %s.\n' % (favorite_color, other_favorite_color)

print 'If I add %d, %d, and %d I get %d.' % (age, height, weight,
                                             age + height + weight)
```
### Try to write some variables that convert the inches and pounds to centimeters and kilograms. Do not just type in the measurements. Work out the math in Python.

Oh, shoot - I didn't read the instructions carefully enough - I was thinking Zed was doing an homage to K&R 'The C Programming Language' opening chapters. I'll leave these in here anyway....
```
# Celsius to Fahrenheit
celsius = 30
print 'If it is %d degrees Celsius, then it is %d Fahrenheit' % (celsius, ((celsius * (9 / 5)) + 32))

# Fahrenheit to Celsius
fahrenheit = 86
print 'If it is %d degrees Celsius, then it is %d Fahrenheit' % (fahrenheit, ((fahrenheit - 32) * (5 / 9)))
```

Here are the actual drill assignments then...NOTE: I included ```from __future__ import division```, but had I not I would have simply written ```9.0/5.00``` and ```5.0/9.00```, respectively.
```
# Inches to Centimeters
my_height_in_centimeters = (float(height) * 2.54)
print 'My non-metric doppelganger is %d cm tall.' % my_height_in_centimeters

# Pounds to kilograms
my_weight_in_kilograms = (float(weight) / 2.2046)
print 'My non-metric doppelganger weighs %d kg.' % my_weight_in_kilograms
```

### Search online for all of the Python format characters.

| Conversion | Meaning                                                          |
|------------|------------------------------------------------------------------|
| d          | Signed integer decimal                                           |
| i          | Signed integer decimal                                           |
| o          | Unsigned octal                                                   |
| u          | Unsigned decimal                                                 |
| x          | Unsigned hexadecimal (lowercase)                                 |
| X          | Unsigned hexadecimal (uppercase)                                 |
| e          | Floating point exponential format (lowercase)                    |
| E          | Floating point exponential format (uppercase)                    |
| f          | Floating point decimal format                                    |
| F          | Floating point decimal format                                    |
| g          | Same as e if exponent is greater than -4 or less, f otherwise    |
| G          | Same as E if exponent is greater than -4 or less, F otherwise    |
| c          | Single character (accepts integer or single character string)    |
| r          | String (converts any python object using repr())                 |
| s          | String (converts any python object using str())                  |
| %          | No argument is converted, results in a % character in the result |

```
# d - Signed integer decimal
print 'Our poodle, Geddy, is %d years old.' % (3)
# i - Signed integer decimal
print 'He gets to go to the local dog park %i days a week.' % (5)
# o - Unsigned octal
print 'I am %d years old in base-10 but %o in base-8.' % (29, 35)
# u - Unsigned decimal
print 'It\'s already %u degrees Fahrenheit outside in Minnesota' % (-32)
# x - Unsigned hexadecimal (lowercase)
print 'I am %d years old in base-10 but %x in hexadecimal format' % (29, 1d)
# X - Unsigned hexadecimal (uppercase)
print 'I am %d years old in base-10 but %x in hexadecimal format' % (29, 1D)
# e - Floating point exponential format (lowercase)
print '{:.2e}'.format(float(1.2))
# E - Floating point exponential format (uppercase)
print '{:.2E}'.format(float(1.2))
# f - Floating point decimal format
print 'The interest rate is %.4f%%.' % (3.9245)
# F - Floating point decimal format
print 'The cashier gave us $%.2F in change.' % (10.50)
# g - Same as e if exponent is greater than -4 or less, f otherwise
print '{:.2g}'.format(float(1.2))
# G - Same as E if exponent is greater than -4 or less, F otherwise
print '{:.2G}'.format(float(1.2))
# c - Single character (accepts integer or single character string)
print '%c is the last letter of the English alphabet' % ('Z')
# r - String (converts any python object using repr())
print '%s and %r' % ('apple', 'apple')
# s - String (converts any python object using str())
print 'A %s is a man\'s best friend' % ('poodle')
# % - No argument is converted, results in a % character in the result
print 'This will just print a percent sign %'
print 'I will need to type an extra %% in if I have any instance of substitution in the %s' % ('sentence')
```
### Try more format characters. ```%r``` is a very useful one. It's like saying "print this no matter what."
Ah, like ```console.dir``` when I program in JavaScript, I have found this useful for quick debugging in Python. It has always been my understanding that using this essentially
 converts the object in question using the function ```repr()```. Per the Python docs, this function will ```return a string containing a printable representation of an object.```

A very well-constructed example of its use is show here ([source](http://stackoverflow.com/questions/6005159/when-to-use-r-instead-of-s-in-python/6005180#6005180):
```
>>> import datetime
>>> d = datetime.date.today()
>>> str(d)
'2011-05-14'
>>> repr(d)
'datetime.date(2011, 5, 14)'
```

In addition to the above use case, per Zed's comment, it might sometimes be used like this:
```
format_character = '%r'
print 'The raw data value of the variable "format_character" is %s.' % format_character
print 'The raw data value of the variable "format_character" is %r.' % format_character
```

Which produces the following output:
```
(venv)marclaughton at MacBookPro in ~/Development/Projects/Learn_Python_The_Hard_Way/Ex5 on develop*
 ➜  python
Python 2.7.10 (default, Sep 23 2015, 04:34:14)
[GCC 4.2.1 Compatible Apple LLVM 7.0.0 (clang-700.0.72)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> format_character = '%r'
>>> print 'The raw data value of the variable "format_character" is %s.' % format_character
The raw data value of the variable "format_character" is %r.
>>> print 'The raw data value of the variable "format_character" is %r.' % format_character
The raw data value of the variable "format_character" is '%r'.
```

Notice that in the instance where we use the ```%r``` format character we see the variable's raw data (i.e., that it is a string object).
