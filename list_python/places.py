places = ['Boston', 'New York' , 'Pittsburgh', 'Miami', 'Seattle']

print(places)

print("Now I am sorting these places.")
print(sorted(places))

print("I still retain my original order of the list.")
print(places)

places.reverse()
print("Now the order of these places are reversed.")
print(places)

places.reverse()
print("Magic!!! I regain my original order.")
print(places)

places.sort()
print("Now it's permanently sorted.")
print(places)

places.sort(reverse=True)
print("Now it's sorted in reverse order.")
print(places)

#loop
for place in places:
	print(place)

