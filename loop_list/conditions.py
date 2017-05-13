import random
import sys
import os

#if else elif == != > >= < <=

age = 21

if age > 16:
    print("You are old enough to drive")
else:
    print("You are not old enough to drive.")

if age >= 21:
    print("You can drink legally.")

else:
    print("You may not drink at all.")

#and or not

if((age >= 1 and (age<=18))):
    print("....")
elif (age==21 or age >=65):
    print("You are adult.")
elif not(age==30):
    print("You..")
else:
    print("Welcome to the party")

for x in range(0,10):
    print(x,' ',end="")
print('\n')


for x in [2,4,6,8,10]:
    print(x)

num_list = [[1,2,3], [10,20,30], [100,200,300]]

for x in range(0,3):
    for y in range(0,3):
        print(num_list[x][y])



#while loop when you have no idea how many times you need to loop

random_num = random.randrange(0,100)
#generate a random number

while(random_num!=15):
    print(random_num)
    random_num = random.randrange(0,100)

i = 0;

while(i <= 20):
    if(i%2 == 0):
        print(i)
    elif (i ==9):
        break
    else:
        i += 1 #i= i+1
        continue

    i += 1


