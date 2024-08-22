import random

random_numbers = [random.randint(1, 100) for num in range(50)]

print("Filter", list(filter(lambda x: True if x > 50 else False, random_numbers)))

print("Filter", list(filter(lambda x: True if x % 7 == 0 else False, random_numbers)))

print("Filter", list(filter(lambda x: True if x >= 10 else False, random_numbers)))

print("Filter", list(filter(lambda x: True if 10 < x < 100 and x // 10 == x % 10 else False, random_numbers)))

print("Filter" ,list(filter(lambda x: 10 <= x < 100 and (x // 10) + (x % 10) == 9, random_numbers)))

average = sum(random_numbers) / len(random_numbers)

print("Filter", list(filter(lambda x: True if x > average else False, random_numbers)))

half_max = max(random_numbers) / 2

print("Filter", list(filter(lambda x: True if x > half_max else False, random_numbers)))
