empty_tuple = ()
print(empty_tuple)

print("=" * 5)
name = ("Ridwan", "Dwi", "Siswanto")
print(name)
nama_pertama, nama_tengah, nama_akhir = name

print("=" * 5)
print(nama_pertama)
print(nama_tengah)
print(nama_akhir)

print("=" * 5)
name_list = ["Ridwan", "Dwi", "Siswanto"]
name_tuple = tuple(name_list)
print(name_list)
print(name_tuple)

#Accessing element in tuple
print(name_list[0])
print(name_list[0], name_list[1])
