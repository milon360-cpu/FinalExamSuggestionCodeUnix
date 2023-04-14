'''
Question2: 
Write a python script to take any number of 10 digits as command-line argument and find the
addition of all even digits and the multiplication of all odd digits.
For example:
Input: 8775258553
Output: Addition : 8 + 2 =10
Multiplication : 7 * 5 * 3 =105
''' 
number = int(input("Please Enter Any Number of 10 Digits:\t"))


reminder = 0
addition = 0
multiplication = 1
temp = []
while(number > 0):
    reminder = int(number % 10 )
    temp.append(reminder)
    number = int(number / 10)

set1 = set(temp)
newNumbers = list(set1)

for x in newNumbers:
    if x%2==0:
        addition = addition + x 
    else:
        multiplication = multiplication * x 

print("Addition:\t",addition)
print("Multiplication:\t",multiplication)