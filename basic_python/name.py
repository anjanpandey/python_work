name = "ada lovelace"
print(name.title())

print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = first_name+' '+last_name
print("Hello "+full_name.title()+"!!!")

first_program = "Java "
second_program = "HTML"+" "+"CSS"
third_program = " JavaFX "
fourth_program = " Python"

# always add new line first then tab when you are changing line and tabbing. 

print("I know following programming languages: \n \t \t \t"+ first_program.rstrip()+
		"\n \t \t \t" +second_program+"\n \t \t \t" +third_program.strip()+ 
		"\n \t \t \t" +fourth_program.lstrip()) 
		
# r.strip removes right space and l.strip removes left space temporarily 
#if you print first_program as is then it prints it with space. 
