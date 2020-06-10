# Simple Fahrenheit to Celcius converter
# 
# Usage: python fahr_to_cel.py <A_TEMP>
# Example: python fahr_to_cel.py 32
# 
# The above example should return '0'
import sys

# Parse the source degrees F from the command line’s first parameter, and
# convert it to an integer
degrees_f = int(sys.argv[1])

# Convert degrees Fahrenheit to Celcius
degrees_c = (degrees_f - 32) * 5/9

# Print the result
print('{0}°F is {1}°C'.format(degrees_f, degrees_c))
