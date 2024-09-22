# Summary: Accept a 3-digit integer and generate it's reverse integer

# ToDo:
# 1. Ask user for number and store in variable
# 2. Copy original number to temp
# 3. Prepare reverse variable
# 4. Calculate reverse of integer algorithm - work with temp
# 5. Print Original number and it's reverse

'''
Sample Output
Enter a 3-digit number: 123
Reverse of 123 is 321
'''


num =  int(input("the 3 digit number"))
temp = num
rev = 0
ld = temp % 10
temp = temp // 10
rev = rev *10 + ld
ld = temp % 10
temp = temp // 10
rev = rev *10 + ld
ld = temp % 10
temp = temp // 10
rev = rev *10 + ld
print("rev value : " , rev)

