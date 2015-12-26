print 'I will now count the guitars:'

# Here this is treated like this by the interpreter:
# 1 + (8 / 3)
# 1 + (2)
# 3
print 'Fenders', 1.0 + 8.0 / 3.0

# Per PEMDAS (i.e., order of operations) the line below will evaluate as
# 100 - ((25 * 3) % 4)
# 100 - (75 % 4) => 75 / 4 = 18.75 => 18 * 4 = 72 => 75 - 72 = 3
# 100 - 3 = 97
print 'Gibsons', 100.0 - 25.0 * 3.0 % 4.0

print 'Now I will count the strings:'

# Again, per PEMDAS:
# (((((3 + 2) + 1) -5) + 0) - (1 / 4)) + 6
# ((((5 + 1) - 5) + 0) - (1 / 4) + 6)
# (((6 - 5) + 0) - (1 / 4) + 6)
# ((1 + 0) - (1 / 4) + 6)
# (1 - 0) + 6
# 7
print 3.0 + 2.0 + 1.0 - 5.0 + 4.0 % 2.0 - 1.0 / 4.0 + 6.0

print 'Is it true that 3 + 2 < 5 - 7?'    # This should be FALSE, as -2 is < 5

print 3.0 + 2.0 < 5.0 - 7.0

print 'What is 3 + 2', 3.0 + 2.0    # 5
print 'What is 5 - 7', 5.0 - 7.0    # -2
print 'Of course that\'s why it\'s FALSE.'

print 'How about some more?'

print 'Is it greater?', 5.0 > -2.0    # This should be TRUE
print 'Is it greater or equal?', 5.0 >= -2.0    # This should be TRUE
print 'Is it less or equal?', 5.0 <= -2.0    # This should be FALSE
