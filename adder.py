#! /usr/bin/env python3
# 
# Add two predefined numbers and a user-provided number

# Define two variables ('num1' and 'num2') with pre-defined values
num1 = 2
num2 = 5

# Create the 'num3' variable, but initially give it the special 'None' value,
# since it doesn’t yet have the user’s integer input
num3 = None
# Keep running the following block of code until the user submits an integer
while num3 is None:
    # Prompt the user; Python will initially store the input as text
    print ('Enter an integer:')
    user_input = input()
    # Try to convert 'user_input' to integer, but guard against bad input
    try:
        num3 = int(user_input)
    except ValueError:
        print (user_input + ' is not an integer.')

# Add the three numbers and store the result in the new variable 'sum'
sum = num1 + num2 + num3

print('The sum of {0} and {1} and {2} is {3}'.format(num1, num2, num3, sum))
