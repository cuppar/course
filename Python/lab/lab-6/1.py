from functools import wraps
import time


def decorater(func):
    @wraps(func)
    def wrapper(*args, **kwords):
        t1 = time.time()
        result = func(*args, **kwords)
        t2 = time.time()
        print('该程序耗时: %f毫秒' % (t2-t1))
        return result
    return wrapper


@decorater
def my_sum100():
    n = 0
    for i in range(101):
        n += i
    return n


@decorater
def my_sum(start=1, end=100, *, stap=1):
    return sum(x for x in range(start, end+1, stap))


if __name__ == '__main__':
    print('1到100的和为:', my_sum100())
    print('1到100的奇数和为:', my_sum(1, 100, stap=2))
