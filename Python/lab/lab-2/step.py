result = []
for i in range(10000):
    if i % 2 == 1\
            and i % 3 == 2\
            and i % 4 == 3\
            and i % 5 == 4\
            and i % 6 == 5\
            and i % 7 == 0:
        result.append(i)
j = 0
for i in result:
    print(i, ', ', end=' ')
    j = j+1
    if j % 5 == 0:
        print()
