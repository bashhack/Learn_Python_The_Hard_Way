from sys import argv

script = argv

print 'We\'re going to create and interact with a file you create: '
print 'If you don\'t want that, hit CTRL-C (^C).'
print 'If you do want that, hit RETURN.'

print 'Type the name of the file you\'d like to create and open: '
filename = raw_input('> ')

file_content = open(filename, 'w+')

print 'Now I\'m going to ask you to write a haiku:'
line1 = raw_input('line of 5 syllables: ')
line2 = raw_input('line of 7 syllables: ')
line3 = raw_input('line of 5 syllables: ')
lines = (line1, line2, line3)

nl = '\n'

print 'Now I am going to write these to the file.\n'
file_content.writelines(nl.join(lines))
file_content.write('\n')

file_content.close()

file_content = open(filename)

print 'Here is your poem, wonderful work!'
print file_content.read()

print 'And finally, we close it.'
file_content.close()
