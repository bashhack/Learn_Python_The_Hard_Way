from __future__ import division

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

print 'If I add %d, %d, and %d I get %d.\n' % (age, height, weight,
                                               age + height + weight)

print '=========================\n'

# Celsius to Fahrenheit
celsius = 30
print 'If it is %d degrees Celsius, \
then it is %d Fahrenheit.' % (celsius, ((celsius * (9 / 5)) + 32))

# Fahrenheit to Celsius
fahrenheit = 32
print 'If it is %d degrees Fahrenheit, \
then it is %d Celsius.' % (fahrenheit, ((fahrenheit - 32) * (5 / 9)))

# Inches to Centimeters
my_height_in_centimeters = (float(height) * 2.54)
print 'My non-metric doppelganger is %d cm tall.' % my_height_in_centimeters

# Pounds to kilograms
my_weight_in_kilograms = (float(weight) / 2.2046)
print 'My non-metric doppelganger weighs %d kg.' % my_weight_in_kilograms

print '=========================\n'

format_character = '%r'

print 'The raw data value of the variable \
"format_character" is %s.' % format_character
print 'The raw data value of the variable \
"format_character" is %r.' % format_character
