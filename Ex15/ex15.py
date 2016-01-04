# Import argv definition/statement from sys module
from sys import argv

# Assign script to argv[0] and name of the file to be read as argv[1]
script, filename = argv

# Open the file and assign result to txt
txt = open(filename)

# Print the name of the file and the contents
print 'Here\'s your file %r' % filename
print txt.read()

# Prompt the user for the name of the file and assign it to file_again
print 'Type the filename again:'
file_again = raw_input('> ')

# As before, open the file (this time from the user input) and assign result
txt_again = open(file_again)

# Print the result of using the read method on the file
print txt_again.read()

txt.close()
txt_again.close()
