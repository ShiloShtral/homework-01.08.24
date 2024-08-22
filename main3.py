import random
random_numbers = [random.randint(-50, 50) for _ in range(20)]
print(random_numbers)

print(list(map(lambda x: x ** 2 , random_numbers)))

print(list(map(lambda x: x % 10 , random_numbers)))

print(list(map(lambda x: x * 9/5 + 32 , random_numbers)))

print(list(map(lambda x: "Positive" if x > 0 else "Negative" , random_numbers)))


max_number = max(random_numbers)
min_number = min(random_numbers)
print(list(map(lambda x: "max" if x == max_number else ("min" if x == min_number else x), random_numbers)))

