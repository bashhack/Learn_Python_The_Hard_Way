"""
This script calculates the:
(1) Total cost of the mortage
(2) The monthly payment amount

The equation I am using for the basis of this program is:

c = (rP / (1 - (1 + r)^-N)) = (rP(1 + r)^N) / (((1 + r)^N) - 1)

Here, P is the principal, r is the monthly interest rate,
and N the number of monthly payments.

NOTE: This equation borrowed from Robert Kohn's work:
"A capital budgeting model of the supply and demand of loanable funds",
Journal of Macroeconomics 12, Summer 1990, pp. 427-436 (p. 430)
"""

from __future__ import division
# here, the above import isn't totally necessary since rate is already float
# but wanted to include for completeness

# TODO: I should likely turn this into a short command line application,
# prompting user input for the values and returning the result or saving
# to txt file output on system...

mortage_amount = 250000
interest_rate = 3.92
mortage_period = 30

p = mortage_amount
r = ((interest_rate / 12) / 100)
n = (mortage_period * 12)

res = ((r * p) / (1 - ((1 + r)**(-n))))

print '$', round(res, 2)
