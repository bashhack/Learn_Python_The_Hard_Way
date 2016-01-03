from sys import argv

script = argv

print 'Type the name of the file you\'d like to open: '
filename = open(raw_input('> '))

file_content = filename.read()

print file_content

filename.close()
