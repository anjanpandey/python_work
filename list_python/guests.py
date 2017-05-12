guests = ['Alan Turing', 'Ada Lovelace', 'Steve Jobs', 'Rockies Koss']

print("Hello! "+guests[0]+". I will like to invite you for dinner.")
print("Hello! "+guests[1]+". I will like to invite you for dinner.")
print("Hello! "+guests[-2]+". I will like to invite you for dinner.")
print("Hello! "+guests[-1]+". I will like to invite you for dinner.")

not_coming = 'Rockies Koss'

print(not_coming+" is not coming to dinner.")

guests.remove(not_coming)
guests.append('Linna McDarling')

print(guests)

print("Hello! "+guests[0]+". I will like to invite you for dinner.")
print("Hello! "+guests[1]+". I will like to invite you for dinner.")
print("Hello! "+guests[-2]+". I will like to invite you for dinner.")
print("Hello! "+guests[-1]+". I will like to invite you for dinner.")


print("Hello Everyone! I just found a big table for dinner.")

guests.insert(0, 'Paul Wiedemeier')
guests.insert(2, 'Jose Cordova')
guests.append('Lon Smith') 

print("Hello! "+guests[0]+". I will like to invite you for dinner.")
print("Hello! "+guests[1]+". I will like to invite you for dinner.")
print("Hello! "+guests[2]+". I will like to invite you for dinner.")
print("Hello! "+guests[3]+". I will like to invite you for dinner.")
print("Hello! "+guests[-3]+". I will like to invite you for dinner.")
print("Hello! "+guests[-2]+". I will like to invite you for dinner.")
print("Hello! "+guests[-1]+". I will like to invite you for dinner.")

print(guests)

print("Sorry! I can only invite two guests for dinner.")
first_noinvite = guests.pop(0)
print("Sorry! "+first_noinvite+" I can not invite you!")
second_noinvite = guests.pop(0)
print("Sorry! "+second_noinvite+" I can not invite you!")
third_noinvite = guests.pop(0)
print("Sorry! "+third_noinvite+" I can not invite you!")
fourth_noinvite = guests.pop(0)
print("Sorry! "+fourth_noinvite+" I can not invite you!")
fifth_noinvite = guests.pop(1)
print("Sorry! "+fifth_noinvite+" I can not invite you!")

print("You are still on my list, "+guests[0]+".")
print("You are still on my list, "+guests[1]+".")

del guests[0]
del guests[-1]

print(guests)



