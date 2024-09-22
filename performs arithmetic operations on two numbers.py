

# Summary: This program performs arithmetic operations on two numbers

# ToDo:
# 1. Ask user for two numbers and store in variables
# 2. Perform arithmetic operations on numbers and store in variables
# 3. Print results

'''
Sample Output
Enter first number: 10
Enter second number: 20
Addition: 30
Subtraction: -10
Multiplication: 200
Division: 0.5
Modulus: 10
Exponent: 100000000000000000000
'''


# Ask user for two numbers and store in variables
num1 = int(input("entre the first number"))
num2 = int(input("entre the second number"))

# Perform arithmetic operations on numbers and store in variables
# add, sub, mul, div, mod, exp
add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2
mod = num1 ** num2


# Print results
print("the ans of add is " , add)
print("the ans of sub is " , sub)
print("the ans of mul is " , mul)
print("the ans of div is " , div)
print("the ans of mod is " , mod)


