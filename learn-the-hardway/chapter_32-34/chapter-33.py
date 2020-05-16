i = 0
numbers = []

while i < 3:
    print("+======+")
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("-----")
    print("Numbers now: ", numbers)
    print("-----")
    print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)