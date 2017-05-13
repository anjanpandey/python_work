import random
import sys
import os


def addNumber(fNum, lNum):
    #sumNum is out of scope
    sumNum = fNum + lNum
    return sumNum


print(addNumber(1,4))

print("What is your name?")

name = sys.stdin.readline()

print("Hello ", name)


long_string = "I'll catch you if you fall - The Floor"
print(long_string[0:4])

print(long_string[-5:])

print(long_string[:-5])

print(long_string[:4] + " be there")


print("%c is my %s letter and my number %d number is %.5f" %
      ('X', 'favorite', 1, .14 ))

print(long_string.capitalize()) #Capitalize the first word

print(long_string.find("Floor")) #index of the floor, case sensative

print(long_string.isalnum()) #check to see if all are alphabets

print(long_string.isalpha()) #check to see if all are numbers

print(long_string.replace("Floor", "Ground")) #replace floor with ground

#take a long string and store it in the form of list
quote_list = long_string.split(" ")

print(quote_list)






