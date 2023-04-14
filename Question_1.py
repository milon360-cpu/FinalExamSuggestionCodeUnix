'''
Question1: 
Write a python script to assign two string values of multiple words. Find out and print which words are common in both strings. 
''' 

str1 = ["Milon","Jamal","Kamal","Sonia"]
str2 = ["Milon","Jamir","Samir","Sonia"]

set1 = set(str1)
set2 = set(str2)

commonWord = set1.intersection(set2)

if len(commonWord)>0:
    print('The common word are: \t',end='')
    print(commonWord)
else:
    print("Sorry!! There is no common word")

 