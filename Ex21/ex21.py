def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b


def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b


def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b


def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b


print "Let's do some math with just functions:"

age = add(25, 5)
height = subtract(81, 6)
weight = multiply(5, 50)
fingers = divide(100, 10)

print ("Age: %d, Height: %d, Weight: %d, Fingers: %d"
       % (age, height, weight, fingers))

# A puzzle for the extra credit, type it in anyway
print "Here is a puzzle"

what = add(age, subtract(height, multiply(weight, divide(fingers, 2))))

print "That becomes: ", what, "Can you do it by hand?"
