# Create list without looping
number_list = []
number_list.append(1)
number_list.append(2)
number_list.append(3)
number_list.append(4)
number_list.append(5)

print(number_list)

print("=" * 5)

# Create list with range an iterator
number_list = []
for number in range(1, 6):
    number_list.append(number)

print(number_list)

print("=" * 5)

# with range
number_list = list(range(1, 6))
print(number_list)

print("=" * 5)

# another try
number_list = [number for number in range(1, 6)]
print(number_list)

print("=" * 5)

# for more
number_list = [number-1 for number in range(1, 6)]
print(number_list)