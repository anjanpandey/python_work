# Anjan Pandey

names = ['kaith', 'marie', 'skylar', 'aryas', 'aayush', 'rosh', 'kymber']
print(names[0].title())
print(names[1].title())
print(names[2].title())
print(names[3].title())
print(names[-3].title())
print(names[-2].title())
print(names[-1].title()+"\n")

print("My friend "+names[0].title()+" is a nice human being.")
print("My friend "+names[1].title()+" is a nice human being.")
print("My friend "+names[2].title()+" is a nice human being.")
print("My friend "+names[3].title()+" is a nice human being.")
print("My friend "+names[-3].title()+" is a nice human being.")
print("My friend "+names[-2].title()+" is a nice human being.")
print("My friend "+names[-1].title()+" is a nice human being.")

motorcycles = ['VR', 'Harley', 'Indian']
print("\nMy Business Communication project was to compare two bikes: "
+motorcycles[1].title()+" and "+motorcycles[2].title()+".\n")

print(motorcycles)

motorcycles[0] = 'Sanchez'
print(motorcycles)

#append : adds items to the end of the lists

motorcycles.append('VR')
print(motorcycles)

foods = []

foods.append('Chicken')
foods.append('Veggies')
foods.append('Salad')

print(foods)

#insert : position,item is the best and the easiest way to insert items on list
foods.insert(1, 'Fries')
print(foods)

#del: if you know the position of the item you want to remove, use del
#no longer access the value that was removed 

del foods[1]

print(foods)

popped_food = foods.pop()
print(popped_food)

#pop removes last item from the list, but it gives you privilage to
#access it later. 
#pop can remove any items from the list if the position of that item
#is identified or mentioned. foods.pop(1) - removes the second item
print(foods)

foods.append('Mushroom')
foods.insert(0, 'Pickles')

print(foods)

#removing item by valuem, you can access that value later

foods.remove('Veggies')
print(foods)

not_food = 'Pickles'
foods.remove(not_food)
print(foods)

#accessing the value that was removed
print("I hate "+not_food+".")







