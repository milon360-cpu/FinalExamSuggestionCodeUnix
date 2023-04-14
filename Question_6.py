'''
Question6:
Write a python script to search a particular word in a text file and display how many times that word appeared in the file and the location of the word. [5]
'''

file = open("Q6.txt")
data = file.read().split()

searchingWord = input("Please Enter Your Searching Word:\t")

counter = 0
index = 0
position = []

for x in data:
    if x == searchingWord:
        counter = counter + 1
        position.append(index)
    index = index + 1

print("Total:\t",counter)
print("Index Number",position)