# Define x as a string with a signed integer decimal string format specifier
x = 'There are %d types of people.' % 10
# Define binary as a string literal
binary = 'binary'
# Define do_not as a string literal
do_not = 'don\'t'
# Define y as a string that takes two formatters (i.e., the previous vars)
y = 'Those who know %s and those who %s.' % (binary, do_not)

# The following two statements print the previously defined vars
print x
print y

# Rather than performing the substitution in a var declaration
# and printing the var, we trigger the substitution within the print statement
print 'I said: %r.' % x
# Again, we perform the substitution using our string format specifier
# within the print statement itself - the difference here, of course,
# being that the former example used the formatter for representing the raw
# data (utilizing the repr() function behind the scenes) and the latter
# using the formatter for representing a string (utilizing the str() function
# behind the scenes)
print 'I also said: %s.' % y

# Define hilarious as a Boolean
hilarious = False
# Define joke_evaluation as a string which includes a formatter without
# also defining the value of the substitution
joke_evaluation = 'Isn\'t that joke so funny?! %r'

# As before, within the print statment we can perform string formatting
# substitution using only our variables (in contrast to our other method
# used on line 2) - this example gives us a sense of how we might make
# our code more flexible, rather than tightly coupled and brittle)
print joke_evaluation % hilarious

# The following two var declarations define their respective
# vars as string literals
w = 'This is the left side of...'
e = 'a string with a right side.'

# Print the concatenated value of the previously defined vars
print w + e
