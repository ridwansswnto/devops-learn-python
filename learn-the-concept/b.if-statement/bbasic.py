color = "mauve"

if color == "red":
    print("It's an apple")
elif color == "green":
    print("It's green pepper")
elif color == "been purple":
    print("I don't know what it is, but only bees can see it")
else:
    print("I've never heard of the color", color)

print("=" * 8)

# it is true?
some_list = []
if some_list:
    print("There's something in here.")
else:
    print("Heyy!, it's empty!!")

print("=" * 8)

# it is true?
some_list = [""]
if some_list:
    print("There's something in here.")
else:
    print("Heyy!, it's empty!!")

print("=" * 8)

# multiple comparisons
letter = str(input("masukan huruf: "))
if letter == 'a' or letter =='e' or letter == 'i' \
    or letter == 'o' or letter == 'u':
    print(letter, 'is a vowel')
else:
    print(letter, 'it not a vowel')

print("=" * 8)

#checking value is not in a list
vowel_set = {'a', 'e', 'i', 'o', 'u'}
letter = str(input("masukkan huruf: "))
display = letter in vowel_set
print(display)