import random
from sys import argv

script, num1_file, num2_file, to_file = argv


def cheese_and_crackers(cheese_count, boxes_of_crackers):
    """ Defines a function called cheese_and_crackers that
        takes two args representing counts for cheese and crackers"""
    print "You have %d cheeses" % cheese_count
    print "You have %d boxes of crackers" % boxes_of_crackers


# Here, we call the method fully qualified, with two integers
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)


# Here, we abstract the params into variables that prevent
# a too tightly coupled invocation of the method
print "Or, we can use variables from our script:"
amount_of_cheese = 40
amount_of_crackers = 50
# We call the method with our newly set variables
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Here, we illustrate that params can take functions operations
# like (+) in the method call itself
print "We can event do math inside too:"
cheese_and_crackers(50 + 10, 60 + 10)

# Finally, we expand on the previous example, combining
# function calls to (+), variables, and raw int objects
# to shape the method call
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese / 20, amount_of_crackers * 3)


# Study Drill:
def calcSum(a, b):
    sum = a + b
    print "The sum is: %d" % sum
    return sum


# 1
calcSum(1, 2)

# 2
calcSum(a=1, b=2)

# 3
a = 1
b = 2
calcSum(a, b)

# 4
calcSum(1 + 2, 2 + 1)

# 5
calcSum(a + 2, b + 1)

# 6
first_prompt = raw_input("""We're about to sum some nums!
Please enter your first number: """)
second_prompt = raw_input("""How about that second number? Eh?
Type it now, please: """)

calcSum(int(first_prompt), int(second_prompt))

# 7
calcSum(random.randint(1, 14), random.randint(16, 20))


# 8
def setValuesToSum():
    a = 5
    b = 8
    calcSum(a, b)


setValuesToSum()


# 9
def sumFromReadFile():
    out_file = open(to_file, "w")
    in_file_one = open(num1_file)
    in_file_two = open(num2_file)
    num1 = in_file_one.read()
    num2 = in_file_two.read()

    out_file.write(str(calcSum(int(num1), int(num2))))

    in_file_one.close()
    in_file_two.close()
    out_file.close()


sumFromReadFile()


# 10
def slightlyBetterSumFromReadFile(num1_file, num2_file, out_file):
    out_file = open(out_file, "w")
    in_file_one = open(num1_file)
    in_file_two = open(num2_file)
    num1 = in_file_one.read()
    num2 = in_file_two.read()

    out_file.write(str(calcSum(int(num1), int(num2))))

    in_file_one.close()
    in_file_two.close()
    out_file.close()


slightlyBetterSumFromReadFile("num3.txt", "num4.txt", "sum2.txt")
