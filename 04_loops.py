#!/usr/bin/env python3

import math

# Move the triple quotes downward to uncover each segment of code

"""

# The 'for' loop is one of the most common loop constructs you will use
# Note the indentation of the print(i) statement
# Code 'inside' loops must be indented
# Note that Python starts counting from 0 not 1

for i in range(3):
	print(i)
print('-')

# The above is really a shortcut for the following code

for i in range(0, 3):
	print(i)
print('--')

# But the second construct allows you to set where the loop starts

for i in range(1, 3):
	print(i)
print('---')

# And also the steps between iterations

for i in range(1, 10, 3):
	print(i)
print('----')

# You can iterate over the characters of a string

s = 'ACGT'
for c in s:
	print(c)
print('-----')

# An alternate way to do the same thing
# It's absolutely critical you understand this code!

for i in range(len(s)):
	print(i, s[i])
print('------')

# Everything that is tabbed-over is within the same loop
# Try removing the tab in front of i += 1 below

i = 0
for c in s:
	print(i, c)
	i += 1
print('-------')

# The real power begins with loops inside of loops

for i in range(0, 4):
	for j in range(i, 4):
		print(i, j)
print('--------')

# Just some fun with loops and math!

precision = 10
e = 0
for n in range(0, precision):
	e += 1/math.factorial(n)
	print(e, math.e - e)

"""
