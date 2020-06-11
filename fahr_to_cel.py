# Simple Fahrenheit to Celcius converter
# 
# Usage: python fahr_to_cel.py <A_TEMP>
# Example: python fahr_to_cel.py 32
# 
# The above example should return '0'
import sys

# Parse the source degrees F from the command line’s first parameter, and
# convert it to an integer
if len(sys.argv) is 2 and sys.argv[1].lstrip('-').isnumeric():
    degrees_f = int(sys.argv[1])
else:
    sys.exit('Usage: python fahr_to_cel.py <int>')

# Disallow temperatures lower than absolute zero
MIN_F = -459.67
if degrees_f < MIN_F:
    sys.exit('Lowest possible Fahrenheit temperature is {0}'.format(MIN_F))

# Convert degrees Fahrenheit to Celcius
degrees_c = (degrees_f - 32) * 5/9

# Print the result
print('{0}°F is {1}°C'.format(degrees_f, round(degrees_c, 1)))
