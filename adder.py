# Add two predefined numbers and a user-provided number

# Define two variables ('num1' and 'num2') with pre-defined values
num1 = 2
num2 = 5

# Ask the user to input an integer; Python will initially store it as text
print ('Enter an integer:')
user_input = input()

# Change the type of the user input from text to an actual integer, so that we
# can add it in the next step
num3 = int(user_input)

# Add the three numbers and store the result in the new variable 'sum'
sum = num1 + num2 + num3

print('The sum of {0} and {1} and {2} is {3}'.format(num1, num2, num3, sum))
