place = ['Baluran', 'Banda Neira', 'Rinjani', 'Lake Como', 'Makkah', 'Manchaster', 'Oslo', 'Japan']

print("Here is the original list:")
print(place)

print("\nHere is the sorted list:")
print(sorted(place))

print("\nHere is the original list again:")
print(place)

print("\nHere is the reverse sorted list:")
print(sorted(place, reverse=True))

print("\nHere is the original list again:")
print(place)

print("\nHere is the reverse list:")
place.reverse()
print(place)

print("\nHere is the original list again:")
place.reverse()
print(place)

print("\nHere is the sort alphabetical list:")
place.sort()
print(place)

print("\nHere is the sort reverse-alphabetical list:")
place.sort(reverse=True)
print(place)
