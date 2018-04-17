leapYears = []
j = 0
for i in range(2000, 2501):
    if i % 100 != 0 and i % 4 == 0 or i % 400 == 0:
        leapYears.append(i)
for i in leapYears:
    print(i, ', ', end='')
    j = j+1
    if j % 8 == 0:
        print()
