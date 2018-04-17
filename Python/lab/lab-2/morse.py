morseMap = {}
file = open("morse.txt")
try:
    for line in file:
        key, value = line.split('  ')
        morseMap[key] = value
finally:
    file.close()
eng = input('please input english: ')
for i in eng:
    print(morseMap[i])
