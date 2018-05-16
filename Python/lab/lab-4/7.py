def fun(list):
    return filter(lambda x: x > 0, list)


print(list(fun([-2, -1, 0, 1, 2])))
