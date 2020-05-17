cars = ['audi', 'bmw', 'mercy', 'honda', 'vw']

for car in cars:
    if car == 'bmw' or car == "vw":
        print(car.upper())
    else:
        print(car.title())