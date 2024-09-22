# Summary: Accept a 3-digit integer and print sum of it's digits

# ToDo:
# 1. Ask user for number and store in variable
# 2. Copy original number temp
# 3. Prepare sum variable
# 4. Calculate sum of digits algorithm - work with temp
# 5. Print Original number and sum of digits

'''
Sample Output
Enter a 3-digit number: 123
Sum of digits of 123 is 6
'''



num = int(input("entre the 3 digit number: "))
temp = num
su = 0
ld = temp % 10
su = su + ld
temp = temp // 10
ld = temp % 10
su = su + ld
temp = temp // 10
ld = temp % 10
su = su + ld
temp = temp // 10
print(" sum of digit :" , su)

