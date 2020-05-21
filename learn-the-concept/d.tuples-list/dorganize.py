cars = ["bwm", "audi", "toyota", "subaru"]
cars.sort()
print(cars)

cars_satu = ["bwm", "audi", "toyota", "subaru"]
cars_satu.sort(reverse=True)
print(cars_satu)

print("=" * 12)

#Temporary with list
cars_dua = ["bwm", "audi", "toyota", "subaru"]
print("Here is the original list:")
print(cars_satu)

print("\nHere is the sorted list:")
print(sorted(cars_dua))

print("=" * 12)

#Reverse list
print("Reverse List")
cars_tiga = ["bwm", "audi", "toyota", "subaru"]
print(cars_tiga)
cars_tiga.reverse()
print(cars_tiga)

print("=" * 12)

#Finding the lenght of list
print("Finding the lenght of list")
cars_tiga = ["bwm", "audi", "toyota", "subaru"]
len_car = len(cars_tiga)
print(cars_tiga)
print(len_car)

print("=" * 12)

#Find an items Offset by Value with index()
cars_empat = ["bwm", "audi", "toyota", "subaru"]
print("Index for Audi : ", cars_empat.index("audi"))

print("=" * 12)

#test value with in
print("Test value in a list")
cars_lima = ["bmw", "audi", "toyota", "subaru"]
print("""1. bmw
2. audi
3. toyota
4. subaru""")
name_car = input(str("Input your cars: "))
if name_car in cars_lima:
    print("Your car is available in our showroom")
else:
    print("Your car not available in our showroom, please visit other")

print("=" * 12)

#count occurences of value with count
car_six = ["bmw", "audi", "toyota", "subaru", "audi", "bmw", "audi", "toyota", "audi"]
audi = car_six.count('audi')
bmw = car_six.count('bmw')
toyota = car_six.count('toyota')
subaru = car_six.count('subaru')
print(f"""
total car bmw in our showroom: {bmw}
total car audi in our showroom: {audi}
total car toyota in our showroom: {toyota}
total car subaru in our showroom: {subaru}
""")