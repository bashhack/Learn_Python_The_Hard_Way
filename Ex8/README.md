# Exercise 8: Printing, Printing
## Study Drills
### Do your checks, write down your mistakes, and try not to make the same mistakes on the next exercise.
Again, here I did not encounter any errors either in review or at runtime.
### Notice that the last line of output uses both single-quotes and double-quotes for individual pieces. Why do you think that is?
Because of the ```%r``` string format specifier (again, this returns a string literal object using the ```repr()``` function),
when the Python interpreter encounters an instance where it might need to escape a character (in this case the apostrophe
in the word *don't*) it will choose the path of least resistance and print the result in such a way that it avoids unnecessary
escaping. In this case, it is more efficient for the interpreter to print this:

```
"But it didn't sing."
```

...rather than this...

```
'But it didn\'t sing.'
```
