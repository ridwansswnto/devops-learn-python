animals = ["cat", "dog", "rabbit", "penguin"]
print(animals[0:3])
print(animals[::2])
print(animals[::-2])

# Add data with append
add_ani1 = animals.append("elepthant")
print(animals)

# Add data with insert
add_ani2 = animals.insert(1, "tiger")
print(animals)

duplicate_animals = animals * 2
print(duplicate_animals)