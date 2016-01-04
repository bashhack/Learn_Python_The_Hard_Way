# Exercise 16: Reading and Writing Files
## Study Drills
### If you do not understand this, go back through and use the comment trick to get it squared away in your mind. One simple English comment above each line will help you understand or at least let you know what you need to research more.
For comments, please see ```ex16_extended.py```.

For output, please see ```test.txt```.

### Write a script similar to the last exercise that uses ```read``` and ```argv``` to read the file you just created.
Please see ```ex16_alternate.py``` for details.

Output (```poem.txt```):
```
(venv)marclaughton at MacBookPro in ~/Development/Projects/Learn_Python_The_Hard_Way/Ex16 on exercise-16*
 ➜  python ex16_alternate.py
We're going to create and interact with a file you create:
If you don't want that, hit CTRL-C (^C).
If you do want that, hit RETURN.
Type the name of the file you'd like to create and open:
> poem.txt
Now I'm going to ask you to write a haiku:
line of 5 syllables: spam spam spam spam spam
line of 7 syllables: spam spam spam spam spam spam spam
line of 5 syllables: spam spam spam spam spam
Now I am going to write these to the file.

Here is your poem, wonderful work!
spam spam spam spam spam
spam spam spam spam spam spam spam
spam spam spam spam spam

And finally, we close it.
```

### There's too much repetition in this file. Use strings, formats, and escapes to print out ```line1```, ```line2```, and ```line3``` with just one ```target.write()``` command instead of six.
I really wanted to get the hang of not only ```write()``` but also ```writelines()```. Please see ```ex16_extended.py``` for my five variations on this idea.

### Find out why we had to pass a ```'w'``` as an extra parameter to ```open```. Hint: ```open``` tries to be safe by making you explicitly say you want to write a file.
Per my original comments in the README for ```Exercise 12```, ```w``` and its variant ```w+``` are optional mode params on the ```open``` method.

Additional modes include ```a``` and ```r```: append and read, respectively.

### If you open the file with ```'w'``` mode, then do you really need the ```target.truncate()```? Read the documentation for Python's ```open``` function and see if that's true.
No we do not, per my comment on line 41:

```
# NOTE: I do find it confusing, however, that we are calling the method
# as it has been my understanding that passing the write flag to open()
# overwrote/truncated the file by default - perhaps Zed has us
# doing this for a teachable moment?
```
