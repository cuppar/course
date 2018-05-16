def fib(n):
    if n == 0:
        return ''
    if n == 1:
        return '0,'
    if n == 2:
        return '0,1,'
    else:
        last = fib(n-1)
        return last+str(int(last.split(',')[n-3])+int(last.split(',')[n-2]))+','


print('fib(20) = ')
print(fib(20))
