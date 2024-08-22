list1 = []
def is_zugi(x:int) -> bool:
    if x % 2 == 0:
        list1.append(x)
        return True
    else:
        return False



print("filter", list(filter(is_zugi, [2, 10, 15, 20, 60])))
print("filter", list(filter(lambda x: True if x % 2 == 0 else False, [2, 10, 15, 20, 60])))
