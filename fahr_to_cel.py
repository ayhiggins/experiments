# Simple Fahrenheit to Celcius converter
# 
# Usage: python fahr_to_cel.py <A_TEMP>
# Example: python fahr_to_cel.py 32
# 
# The above example should return '0'
import sys

# Parse the source degrees F from the command line’s first parameter
degrees_f = sys.argv[1]

# TODO implement logic to convert degrees Fahrenheit to Celcius

degrees_c = '?'

print(degrees_f + '°F is ' + degrees_c + '°C')
