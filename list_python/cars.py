cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

#sort changes the order of the list permanently. 

print(cars[0])

# sorted() maintains original order of the list but present in sorted order

cars = ['bmw', 'audi', 'toyota', 'subaru']

print("\nHere is the original list: ")
print(cars)

print("\nHere is the sorted list: ")
print(sorted(cars))

print("\nHere is the original list again: ")
print(cars) 

print("\nHere is the reverse order:")
#reverse order - changes permanently 
cars.reverse()
print(cars)

#double reverse brings the original list, like - and - = +
print("\nGoing back to original list: ")
cars.reverse()
print(cars)

#length of a list 

print(len(cars))

