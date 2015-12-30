from sys import argv

script, meat, condiment1, condiment2, fruit, bread, cheese = argv

sandwhich = meat, condiment1, condiment2, bread, cheese

print 'The sandwhich making script is called:', script
print 'Your meat is:', meat
print 'Your first condiment is:', condiment1
print 'Your second condiment is:', condiment2
print 'Your side of fruit is:', fruit
print 'Your bread is:', bread
print 'Your cheese is:', cheese
print 'Your %s sandwhich sounds tasty. \
Especially with a side of %s.' % ((', ').join(sandwhich), fruit)
