numberMap = {
    0: 'zero', 1: 'one', 2: 'two', 3: 'three',
    4: 'four', 5: 'five', 6: 'six', 7: 'seven',
    8: 'eight', 9: 'nine'}
phoneNumber = input('please input your phone number: ')
for i in phoneNumber:
    print(numberMap[int(i)], ' ', end='')
