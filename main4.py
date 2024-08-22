fruits = ["Apple", "Banana", "Orange", "Mango", "Strawberry", "Pineapple", "Grapes", "Watermelon"]

print(list(map(lambda x: x[::-1], fruits)))

print(list(map(lambda x: x[0::-1], fruits)))

print(list(map(lambda x: x.upper(), fruits)))

print(list(map(lambda x: len(x), fruits)))

