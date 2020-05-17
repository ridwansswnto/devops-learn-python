nama = "Ridwan"
total_huruf1 = len(nama)
print(total_huruf1)

nama_tengah = "Dwi"
total_huruf2 = len(nama_tengah)
print(total_huruf2)

nama_akhir = "Siswanto"
total_huruf3 = len(nama_akhir)
print(total_huruf3)

total_huruf = total_huruf1 + total_huruf2 + total_huruf3
print(total_huruf)

nama = "Ridwan Dwi Siswanto"
total = len(nama)
print(total)

nama = "Ridwan Dwi Siswanto"
whitespace = nama.count(' ')
total = len(nama) - nama.count(' ')
print(whitespace)
print(total)

# Remove with strip
setup = 'a duck goes into a bar..........'
print_setup = setup.strip('.')
print(setup)
print(print_setup)

#Capital
cap_setup = setup.capitalize()
title_setup = setup.title()
upper_setup = setup.upper()

print(cap_setup)
print(title_setup)
print(upper_setup)