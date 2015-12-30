from __future__ import division
from sys import argv

script, num_of_apples, num_of_pineapples = argv

people_who_want_apples = float(raw_input('How many people are coming over? '))

appleless_people = people_who_want_apples - float(num_of_apples)
apples_if_we_share = float(num_of_apples) / people_who_want_apples

print 'Well, we\'ll just have %d sad appleless people.' % appleless_people

print 'Or, we could share? \
That\'d be', round(apples_if_we_share, 1), 'for each.'

print 'Well, %.4f apples per person, to be exact' % (apples_if_we_share)

print 'Hopefully, they will like these \
%d pineapples, instead?' % int(num_of_pineapples)
