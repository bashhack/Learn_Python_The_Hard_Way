from sys import argv

script, programming_language, favorite_adjective = argv

print 'The script is called:', script
print 'Python is so cool! And %s is %s.' % (programming_language,
                                            favorite_adjective)
