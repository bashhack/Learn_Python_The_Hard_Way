favorite_number = int(raw_input('Type your favorite number: '))
multiplier = int(raw_input('What would you like to multiply your \
favorite number %d by?\n--> ' % (favorite_number)))
res = favorite_number * multiplier

print 'The result of the operation is %d.' % (res)
