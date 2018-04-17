vowels = ('a', 'i', 'u', 'e', 'o')
vowelsMap = {
    'a': 0,
    'i': 0,
    'u': 0,
    'e': 0,
    'o': 0
}
message = input('please input message: ')
for letter in message:
    if letter in vowels:
        vowelsMap[letter] += 1
for key in vowelsMap.keys():
    print(key, '-->', vowelsMap[key])
