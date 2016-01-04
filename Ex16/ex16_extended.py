# import argv array variable definition from sys module
from sys import argv

# assign current script and user-inputted filename to argv variable
script, filename = argv

# printing itial user instructions (using string interpolation, again)
print 'We\'re going to erase %r.' % filename
print 'If you don\'t want that, hit CTRL-C (^C).'
print 'If you do want that, hit RETURN.'

# set prompt (using raw_input method) to char ?
raw_input('?')

# print comment to let user know 'where' the script is in the process
print 'Opening the file...'
# declare and assign target variable to the result of opening the file,
# with write access/permissions via the passed w flag/param
# NOTE: there are three main modes (per the pydocs) available to the file
# object (from which, of course, filename is descended and consequently
# inherits its properties)
target = open(filename, 'w+')    # added + to w in order to read and write
target.close()

# closing and reoping using a+ for read and write access with the ability
# to read file while file is being written to...append will move cursor to
# the end of the file - if we had added text prior to the close and then
# reopened, everything we add after before this point will remain and
# everything after this point will be added to the file
target = open(filename, 'a+')

# added to see how tell() works, which is caled just before truncate per
# the pydoc reference on the truncate method
print 'Printing the current file position via tell()'
print target.tell()
# the above printed 0 (as the default start position of the file)

# announce the subsequent truncating (deletion/emptying) of the file
# to the size 0 <= from the tell() method, though I could override this
# by passing a size param as a long int
print 'Truncating the file. Goodbye!'
target.truncate()
# NOTE: I do find it confusing, however, that we are calling the method
# as it has been my understanding that passing the write flag to open()
# overwrote/truncated the file by default - perhaps Zed has us
# doing this for a teachable moment?

# begin prompt to user for lines using raw_input, storing results in separate
# variables to be used later in writing to file
print 'Now I\'m going to ask you for three lines.'

line1 = raw_input('line 1: ')
line2 = raw_input('line 2: ')
line3 = raw_input('line 3: ')

# announcing and printing to target file (newline escape characters between)
print 'Now I am going to write these to the file.'
target.write('Original:\n')
target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

# # variation 1
target.write('Start variation 1\n')
target.write('%s\n%s\n%s\n' % (line1, line2, line3))
target.write('End variation 1\n')

# # variation 2
target.write('Start variation 2\n')
target.write(line1 + '\n' + line2 + '\n' + line3 + '\n')
target.write('End variation 2\n')

# variation 3
target.write('Start variation 3\n')
lines = [line1, '\n', line2, '\n', line3, '\n']
target.writelines(lines)
target.write('End variation 3\n')

# variation 4
target.write('Start variation 4\n')
nl = '\n'
target.writelines(('%s' * 6) % (line1, nl, line2, nl, line3, nl))
target.write('End variation 4\n')

# variation 5
target.write('Start variation 5\n')
lines = (line1, line2, line3)
target.writelines(nl.join(lines))
target.write('\n')
target.write('End variation 5\n')

# as open and close start a buffer (kind of like in Vim, is how I think of it)
# we need to close the buffer to ensure clean handling of memory resources
print 'And finally, we close it.'
target.close()
