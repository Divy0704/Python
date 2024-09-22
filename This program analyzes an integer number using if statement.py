# Summary: This program analyzes an integer number using if statement

'''
Sample Output
    Enter an integer number: 10
    number 10 is a positive number.
    number 10 is an even number.

    Enter an integer number: -10
    number -10 is a negative number.
    number -10 is an even number.

    Enter an integer number: 5
    number 5 is a positive number.
    number 5 is an odd number.

    Enter an integer number: -5
    number -5 is a negative number.
    number -5 is an odd number.
'''

'''
ToDo:
    1. Input an integer number
    2. Print number is positive if it is greater than 0
    3. Print number is negative if it is less than 0
    4. Print number is zero if it is equal to 0
    5. Print number is even if it is divisible by 2
    6. Print number is odd if it is not divisible by 2
'''

# input an integer number
num = int(input( "entre the value"))

# print if the number is a positive number
if num > 0:
    print("num is positive")

# print if the number is a negative number
if num < 0:
    print("num is negative")

# print if the number is a zero
if num == 0:
    print("num is 0")

# print if the number is an even number
if num % 2 == 0:
    print("num is even")


# print if the number is an odd number
else:
    print("num is odd")

