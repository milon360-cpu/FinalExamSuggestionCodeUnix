'''
Question4:
Write a python script to declare a list of 5 numbers with duplicates and print the list after removing the duplicate numbers. [5]
'''
numbers = [1,2,3,1,2]
numbers = set(numbers)
numbers = list(numbers)
print(numbers)
