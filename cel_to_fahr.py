#! /usr/bin/env python3
# 
# Simple Celcius to Fahrenheit converter
# 
# Usage: cel_to_fahr.py <A_TEMP>
# Example: cel_to_fahr.py 0
# 
# The above example should return '32'
import sys

# Parse the source degrees F from the command line’s first parameter, and
# convert it to an integer
if len(sys.argv) is 2 and sys.argv[1].lstrip('-').isnumeric():
    degrees_c = int(sys.argv[1])
else:
    sys.exit('Usage: python cel_to_fahr.py <int>')

# Disallow temperatures lower than absolute zero
MIN_C = -273.15
if degrees_c < MIN_C:
    sys.exit('Lowest possible Celcius temperature is {0}'.format(MIN_C))

# Convert degrees Celcius to Fahrenheit
degrees_f = degrees_c * 9/5 + 32

# Print the result
print('{0}°C is {1}°F'.format(degrees_c, round(degrees_f, 1)))
