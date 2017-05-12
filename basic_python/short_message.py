#Name: Anjan Pandey
#Date: 05/11/2017
#Discription: Learning Basic Python


first_name = "John"
last_name = "McSon"

print("Hello! "+first_name+" "+last_name+".What's up?")

print(first_name.upper()+" "+last_name.upper())
print(first_name.lower()+" "+last_name.lower())

print((first_name+" "+last_name).title())

famous_person = "Albert Einstein"
message = '"A person who never made a mistake never tried anything new."'

print(famous_person+" once said, "+message)

person_name = " \n Kaith McDarling \t"

print(person_name.lstrip())
print(person_name.rstrip())
print(person_name.strip())

age = 23
message = "Happy "+str(age)+"rd birthday!!!!"
print(message)

operation_1 = 5+3
operation_2 = 4*2
operation_3 = 10-2
operation_4 = 16/2

#8.0 meaning the operation must be division
#8 means simple addition, substraction, and multiplication

print("All of my answers are equal to "+str(operation_1)+
		", my second answer is also "+str(operation_2)+
		", my third answer is also "+str(operation_3)+
		", and my final operation is also equal to "+str(operation_4))
		
print(operation_1)
