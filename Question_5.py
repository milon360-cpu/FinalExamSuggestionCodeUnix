'''
Question5:
Write a python script to take an input as password. Check and print “The password is valid”
based on following criteria, otherwise print “invalid password”. [5]
A. Minimum 8 character long.
B. Must contains a special character.
C. Minimum one capital letter, small letter and a number.
'''
import re 
pattern="[!@#$%^&*()_+=\-{}\[\]:;\"'<>,.?/\\|]"

password = input('Please Enter Your Password:\t')

if len(password)>=8 and re.search(pattern,password) and re.search("[A-Z]",password) and re.search("[a-z]",password) and re.search("[0-9]",password):
    print("Valid Password")
else:
    print("Invalid Password")
