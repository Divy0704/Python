 Summary: This program converts seconds to duration

# ToDo:
# 1. Ask user for seconds and store in variable
# 2. Calculate hours, minutes, and seconds and store in variables
# 3. Print duration as hh:mm:ss

'''
Sample Output
Enter seconds: 10000
Duration is:  2 : 46 : 40
'''

num = int(input("entre the num"))
hour = num // 3600
hour1 = num % 3600
minute = hour1 // 60
second = hour1 % 60
print(hour , "hours" , minute , "minutes" , second , "seconds")

