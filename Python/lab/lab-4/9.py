def make_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count
    return counter


def make_counter_test():
    mc = make_counter()
    print(mc())
    print(mc())
    print(mc())


make_counter_test()

count = 0


def make_counter2():
    def counter():
        global count
        count += 1
        return count
    return counter


def make_counter_test2():
    mc = make_counter2()
    print(mc())
    print(mc())
    print(mc())


make_counter_test2()
