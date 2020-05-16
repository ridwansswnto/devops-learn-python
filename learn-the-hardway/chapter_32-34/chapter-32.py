the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'avocado']
change = [1, 'pennies', 2, 'dimes', 3, 'quartes']

# This first kind of for-loop goes through a list
for number in the_count:
    print(f"This is count {number}")

for fruit in fruits:
    print(f"A fruits of type: {fruit}")

for i in change:
    print(f"i got {i}")

# Build list, first start with an empty one
elements = []

# Then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print(f"Adding{i} to the list.")
    elements.append(i)

# Now we can print them out too
for i in elements:
    print(f"Elements was: {i}")