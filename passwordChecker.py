#!/bin/python3
import string
password =input("enter the password you want to check....")

upper_Case = any([1 if c in string.ascii_uppercase else 0 for c in password ])
lower_Case = any([1 if c in string.ascii_lowercase else 0 for c in password ])
special_charcter = any([1 if c in string.punctuation else 0 for c in password ])
digits = any([1 if c in string.digits else 0 for c in password ])
#print(string.punctuation)
characters = [upper_Case,lower_Case,special_charcter,digits]
score = 0 
length = len(password) 
with open('passwords.txt','r') as f :
    common=f.read().splitlines()

if password in common:
    print("password was found in common list . score 0/7")
    exit()


if length > 8:
    score +=1
if length > 12:
    score +=1
if length > 17:
    score +=1
if length > 20: 
    score +=1

print(f"passworf length is {str(length)},adding {str(score)} points!")

if sum(characters) >1:
    score+=1
if sum(characters) >2:
    score+=1
if sum(characters) >3:
    score+=1
print(f"password has {str(sum(characters))} different characters type! adding{str(sum(characters)-1)} points")

if score < 4:
    print(f"the password is quit weak ! score: {str(score)}/7")
elif score ==4:
     print(f"the password is ok! score: {str(score)}/7")
elif score > 4 and score < 6:
    print(f"the password is good! score:{str(score)}")

elif score >= 6:
    print("the password is strong")

