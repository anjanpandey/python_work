pizzas = ['Chicken Ranchero', 'Chicken Pineapple', 'Italian Bread']

print(pizzas[1:3])
#prints the elements from index 1 and 2, 3 is not included

for pizza in pizzas:
    print("I like "+pizza+" pizza.\n")

print("I like pizza. The combination of bread, meat, and vegetable is just amazing.")

animals = ['Dog', 'Cat', 'Rabbit', 'Mouse']

for animal in animals:
    print(animal)
    print(animal+" is one of my favorite animals.\n")

print("These animals will make a great pet")

#range is the most easiest way to print the numbers list
#it does not print the last value
for value in range(1,10):
    print(value)

print("5+2=", 5+2)

multi_line_quote = '''
Hey how are you
I hope you are fine...'''

print(multi_line_quote)

#print five new lines
print('\n' * 5)

#this will prevent causing the next line to print on new line
print("I don't like ", end="")
print("newlines")

#You can merge two lists
new_list = [pizzas, animals]

print(new_list)

print(new_list[1][0])
'''this prints first item from the second list
, very very helpful, 1 indicates the second list
and 0 indicates its first item !!!!
'''
second_list = pizzas+animals

print(len(second_list))

print(max(second_list))
#max is the highest value alphabetically

print(min(second_list))
#min is the lowest value alphabetically

#you cannot modify the values of the tuple once created
pi_tuple = (3,1,4,1,5,9)

#you can convert a tuple to list but that is not done normally

new_tuple = list(pi_tuple)
new_list_tuple = tuple(new_tuple)

len(pi_tuple)
min(pi_tuple)
max(pi_tuple)

print(pi_tuple)

#cannot join dictionaries with + sign

super_villains = {'Fiddler' : 'Isaac Bowin',
                  'Captain Cold' : 'Leonard Snart',
                  'Weather Wizard' : 'Mark Mardon'}
#use {} key followed by : and value,

print(super_villains['Captain Cold'])

#delete from the map
del super_villains['Fiddler']

#replaces or add the entries to the map or dicitionaries
super_villains['Pied Piper'] = 'Hartley Rathaway'

print(len(super_villains))

print(super_villains.get("Pied Piper"))

print(super_villains.keys())

print(super_villains.values())








