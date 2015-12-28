# Exercise 10: What Was That?
## Study Drills
### Memorize all the escape sequences by putting them on flash cards.
| Escape     | What It Does                                                |
|------------|-------------------------------------------------------------|
| \\         | Backslash (\)                                               |
| \'         | Single-quote (')                                            |
| \"         | Double-quote (")                                            |
| \a         | ASCII bell (BEL)                                            |
| \b         | ASCII backspace (BS)                                        |
| \f         | ASCII formfeed (FF)                                         |
| \n         | ASCII linefeed (LF)                                         |
| \N{name}   | Character named name in the Unicode database (Unicode only) |
| \r         | Carriage Return (CR)                                        |
| \t         | Horizontal Tab (TAB)                                        |
| \uxxxx     | Character with 16-bit hex value xxxx (Unicode only)         |
| \Uxxxxxxxx | Character with a 32-bit hex value xxxxxxxx (Unicode only)   |
| \v         | ASCII vertical tab (VT)                                     |
| \ooo       | Character with octal value ooo                              |
| \xhh       | Character with hex value hh                                 |

### Use ```'''``` (triple-single-quote) instead. Can you see why you might use that instead of ```"""```?
I actually tend to favor single-quotes, in general, and similarly prefer triple-single-quotes, as well.

The shorter key stroke command to type ```'``` accomplishes a couple things for me:
* Faster
* Statistically reduced chance of introducing errors in my code via the act of typing
* Leads to a more natural use of non-escaped double-quotes for narrative-driven content


### Combine escape sequences and format strings to create a more complex format.
```
tricky_string_1 = 'This sentence has a backspace\b\n'
tricky_string_2 = 'This sentence has a sound \a\n'
tricky_string_3 = 'This sentence has a set of "double-quotes"\n\
and \'escaped\' single-quotes\'\n'
tricky_string_4 = 'This word needs some space\tfrom this word\
and this number %d\n' % (75)

print 'Here is what I wrote %r and here it is again: %s' % (tricky_string_1,
                                                            tricky_string_1)
print 'These are strings within another string...%s...within a string\
...within a...%s...' % (tricky_string_2 + tricky_string_3, tricky_string_1)
print tricky_string_4
```

Output:
```
Here is what I wrote 'This sentence has a backspace\x08\n' and here it is again: This sentence has a backspace

These are strings within another string...This sentence has a sound
This sentence has a set of "double-quotes"
and 'escaped' single-quotes'
...within a string...within a...This sentence has a backspace
...
This word needs some space  from this wordand this number 75

```
<h3>Remember the <code>%r</code> format? Combine <code>%r</code> with double-quote and single-quote escapes and
print them out. Compare <code>%r</code> with <code>%s</code>. Notice how <code>%r</code> prints it the way you'd write
it in your file, but <code>%s</code> prints it the way you'd like to see it?</h3>
```
string_test = 'This is a test "sentence"'
print 'Using %%r: %r\nUsing %%s: %s' % (string_test, string_test)
```

Output:
```
Using %r: 'This is a test "sentence"'
Using %s: This is a test "sentence"
```
