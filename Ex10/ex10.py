tabby_cat = '\tI\'m tabbed in.'
persian_cat = 'I\'m split\non a line.'
backslash_cat = 'I\'m \\ a \\ cat'

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat


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

string_test = 'This is a test "sentence"'
print 'Using %%r: %r\nUsing %%s: %s' % (string_test, string_test)
