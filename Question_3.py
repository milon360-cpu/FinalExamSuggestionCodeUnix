'''
Question3:
Write a python script to declare a list of 10 numbers and print the list after removing all odd numbers. [5]
'''
number = [1,2,3,4,5,6,7,8,9,10]
temp = []
for x in number:
    if x%2==0:
        temp.append(x)

number = temp 
print(number)
