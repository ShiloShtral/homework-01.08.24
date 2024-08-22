city = ["Tokyo", "New York", "Paris", "London", "Sydney", "Dubai", "Shanghai"]

print(sorted(city, key=lambda word: len(word)))

print(sorted(city, key=lambda word: word[-1]))

print(list(map(lambda x: x[::-1], city)))

city_with_info =["Tokyo,5760,Asia", "New York,5690,North America", "Paris,2050,Europe", "London,2240,Europe", "Sydney,8780,Australia", "Dubai,1300,Asia", "Shanghai,4920,Asia"]

print(sorted(city_with_info, key=lambda x: int(x.split(',')[1])))

print(sorted(city_with_info, key=lambda x: int(x.split(',')[1]), reverse=True))

print(sorted(city_with_info, key=lambda x: x.split(',')[2]))

print(sorted(city_with_info, key=lambda x: (x.split(',')[2], int(x.split(',')[1]))))