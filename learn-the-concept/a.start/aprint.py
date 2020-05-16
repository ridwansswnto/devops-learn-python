print("Hello World")
print("=" * 10, "\n")

print("'Nay!', said naysayer. 'Neigh?' said the horse.")
print("=" * 10, "\n")

print('The rare double quote in capacity: ".')
print("=" * 10, "\n")

print('A "two by four" is actually 1 1/2" x 3 1/2".')
print("=" * 10, "\n")

print("'There's the man that shot my paw!' cried the limping hound.")
print("=" * 10, "\n")

print('''Boom!''')
print("""Boom!""")
print("=" * 10, "\n")

poem = ''' 
Sebuah kota yang indah, Bandung
Terdapat berbagai wisata berada disana.
Seperti suasana yang sejuk di lembang dan ciater.
Serta mall di daerah Cihampelas
'''
print(poem)

#String with str
satu = str(72)
dua = str(1.231)
tiga = str(True)
empat = 72

print("The original string:", satu)
check = isinstance(satu, str)
print("Is variable a string? :", check)
print("=" * 10, "\n")

print("The original string:", dua)
check = type(dua) == str
print("Is variable a string?:", check)
print("=" * 10, "\n")

print("The original string:", tiga)
check = isinstance(tiga, str)
print("Is variable a string?:", check)
print("=" * 10, "\n")

print("The original string:", empat)
check = isinstance(empat, str)
print("Is variable a string? :", check)
print("=" * 10, "\n")