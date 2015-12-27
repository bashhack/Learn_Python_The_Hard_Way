# Exercise 6: Strings and Text
## Study Drills
### Go through this program and write a comment above each line explaining it.
See ```ex6.py``` for details.
### Find all the places where a string is put inside a string. There are four places.
We have the following occurrences:
```
y = 'Those who know %s and those who %s.' % (binary, do_not)    # (1, 2)
```

```
print 'I said: %r.' % x    # (3)
```

```
print 'I also said: %s.' % y    # (4)
```
### Are you sure there are only four places? How do you know? Maybe I like lying.
Strictly speaking, the four instances I noted above are the places where a string object is nested
 within another string object. It should be noted that the following line still counts because
 ```print 'I said: %r.' % x``` the string formatter ```%r``` returns a string, just like ```%s``` does.
### Explain why adding the two strings ```w``` and ```e``` with ```+``` makes a longer string.
Adding these two vars (which happen to be of object type ```str```) results in the creation of
 a longer string of the same type as we are concatenating their respective values.

I have included a short example to demonstrate this further. Note that the interpreter throws an
 error if we attempt to concatenate an object of type ```str``` with an object of type ```int```.

```
(venv)marclaughton at MacBookPro in ~/Development/Projects/Learn_Python_The_Hard_Way/Ex6 on develop*
 ➜  python
Python 2.7.10 (default, Sep 23 2015, 04:34:14)
[GCC 4.2.1 Compatible Apple LLVM 7.0.0 (clang-700.0.72)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> w = 'This is a string'
>>> e = '...this is another string'
>>> print w + e
This is a string...this is another string
>>> type(w)
<type 'str'>
>>> type(e)
<type 'str'>
>>> type(w + e)
<type 'str'>
>>> e = 7
>>> print w + e
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: cannot concatenate 'str' and 'int' objects
```
