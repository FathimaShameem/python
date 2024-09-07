"""
#Guess the number game
import random
r=random.randint(1,100)

while True:
    num=int(input("Guess the number : "))
    if(num<r):
        print("Your number is too small")
    elif(num>r):
        print("Your number is too big")
    else:
        print("You have guessed the right number")
        break
print("-----GAME OVER-----")    

#random password generator
import random
import string

#print(string.ascii_letters,type(string.ascii_letters))
#print(string.ascii_uppercase)
#print(string.ascii_lowercase)
#print(string.punctuation)
pass_len=int(input("Type the length of the password : "))
charset= string.ascii_letters+string.digits+string.punctuation

password=""
for i in range(pass_len):
    password+=random.choice(charset)
print("Random Password : ",password)
"""
#random password generator list method

import random
import string

pass_len=int(input("Type the length of the password : "))
charset= string.ascii_letters+string.digits+string.punctuation

password=[random.choice(charset)  for i in range(pass_len)]

print("Random Password List : ",password)