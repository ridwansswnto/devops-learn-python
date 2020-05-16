palindrome = "A man, \nA plan, \nA canal, \nPanama."
print(palindrome)

tabbing = """
\tabc
a\tbc
ab\tc
"""
# \ is escape everthing charater behind that
print(tabbing)

# combine string using +
nama = ("Ridwan " + "Dwi " + "Siswanto")
print(nama)
print("=" * 10)

fname = "Ridwan"
tname = "Dwi"
lname = "Siswanto"
print(fname + tname + lname)
print(fname, tname, lname)

# Get character
huruf = "abcdefghijklmnopqrstuvwxyz"
print('{} {} {} {} {} {}'.format(huruf[17], huruf[8], huruf[3], huruf[22], huruf[0], huruf[13]))

name = "Ridwan"
replace = name.replace('d', 'f')
print(replace)