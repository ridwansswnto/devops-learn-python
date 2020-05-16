import json
# Create a mapping of state to abbreviation
states = {
    'Jawa Barat': 'JABAR',
    'Jawa Tengah': 'JATENG',
    'Jawa Timur': 'JATIM',
    'Sumatera Barat': 'SUMBAR',
    'Sumatera Selatan': 'SUMSEL'
}

# Create a basic set of statese and some cities in them
cities = {
    'SUMSEL': 'Palembang',
    'JATIM': 'Surabaya',
    'JABAR': 'Bandung'
}

# Tambah beberapa kota
cities['JATENG'] = 'Semarang'
cities['SUMBAR'] = 'Padang'

# Print out some cities
print('=' * 5)
print("Ibukota Provinsi SUMSEL: ", cities['SUMSEL'])
print("Ibukota Provinsi JATIM: ", cities['JATIM'])

# Print out some states
print('=' * 5)
print("Sumatera Selatan memiliki singkatan: ", states['Sumatera Selatan'])
print("Jawa Barat memiliki singkatan: ", states['Jawa Barat'])

# Do it by using the state then cities dict
print('=' * 5)
print("Sumatera selatan memiliki: ", cities[states['Sumatera Selatan']])
print("Jawa Barat memiliki: ", cities[states['Jawa Barat']])

# Print every state abbreviation
print("=" * 5)
for state, abbrev in list(states.items()):
    print(f"{abbrev} singkatan dari {state}")

# Print every city in state
print("=" * 5)
for abbrev, city in list(cities.items()):
    print(f"Ibukota {abbrev} adalah {city}")

# now do both at the same time
print("=" * 5)
for state, abbrev in list(states.items()):
    print(f"Provinsi {state} memiliki singkatan {abbrev}")
    print(f"dan Ibukota {cities[abbrev]}")

print("=" * 5)
state = states.get('Jakarta')

if not state:
    print("Maaf, Tidak ada Jakarta")

# Get a city with a default value
city = cities.get('JKT', 'Does Not Exist')
print(f"The city for the state 'JKT' is: {city}")

json_state = json.dumps(states, indent=4)
json_cities = json.dumps(cities, indent=4)

print(states)
print(json_state)
print("=" * 5)
print(cities)
print(json_cities)