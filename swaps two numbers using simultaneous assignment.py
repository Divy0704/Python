# Summary: This program swaps two numbers using simultaneous assignment

# ToDo:
# 1. Input two numbers
# 2. Print numbers before swapping
# 3. Swap numbers using simultaneous assignment
# 4. Print numbers after swapping

'''
Sample Output
Enter first number: 10
Enter second number: 20
Before swapping:
First number:  10
Second number:  20
After swapping:
First number:  20
Second number:  10

'''


# Input two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Print numbers before swapping
print("Before swapping: ")
print("First number: ", num1)
print("Second number: ", num2)

# Swap numbers
num1,num2=num2,num1

# Print numbers after swapping
print("After swapping: ")
print("First number: ", num1)
print("Second number: ", num2)

