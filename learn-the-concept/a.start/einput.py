"""Find the minimum of three value"""

number1 = int(input("Enter first integer: "))
number2 = int(input("Enter second integer: "))
number3 = int(input("Enter third integer: "))

minimum = number1

if number2 < minimum:
    minimum = number2

if number3 < minimum:
    minimum = number3

print("Minimum value is", minimum)
print("=" * 8)

minimum_search = min(number1, number2, number3)
maximum_search = max(number1, number2, number3)

print(f"Minimum value between {number1}, {number2}, and {number3} = ", minimum_search)
print(f"Maximum value between {number1}, {number2}, and {number3} = ", maximum_search)
