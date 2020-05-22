num_list = [number for number in range(1, 6) if number % 2 == 1]
print(num_list)

print("=" * 5)

# wit litle fix
num_list = []
for number in range(1, 6):
    if number % 2 == 1:
        num_list.append(number)

print(num_list)

print("=" * 5)

# nested loop
rows = range(1, 4)
cols = range(1, 3)
print(rows)
print(cols)
for row in rows:
    for col in cols:
        print(row, col)

print("=" * 5)

# create list
rows = range(1, 4)
cols = range(1, 3)
cells = [(row, col) for row in rows for col in cols]
print(cells)
for cell in cells:
    print(cell)
