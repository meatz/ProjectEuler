# Project Euler Problem 34
"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

result = 0
def factorial (x):
    r = 1
    for x in range (1,x+1):
        r *= x
    return r
    
for x in xrange (3,10000000):
    s=str(x)
    sum=0
    for y in s:
        sum += factorial (int(y))
    if x == sum:
        print x
        result +=x
        
print "result: %d" % (result)