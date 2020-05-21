animals = ["cat", "dog", "rabbit", "penguin"]
print("Slice")
print(animals[0:3])
print(animals[::2])
print(animals[::-2])

print("=" * 5)

# Add data with append
add_ani1 = animals.append("elepthant")
print("Append elephant to list")
print(animals)

print("=" * 5)

# Add data with insert
add_ani2 = animals.insert(1, "tiger")
print("Add data with insert")
print(animals)

print("=" * 5)

#Duplicate animals
duplicate_animals = animals * 2
print("Duplicate animals")
print(duplicate_animals)

print("=" * 5)

#Remove element animals di del
print("Before delete")
print(animals)
print("After delete")
del animals[0]
print(animals)

print("=" * 5)

#Remove element with pop
print("Before Remove")
print(animals)
poped_animal = animals.pop(1)
print("animals after popped")
print(animals)
print("popped to var")
print(poped_animal)

