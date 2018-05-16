import random


def personGet():
    num = int(input('get: '))
    while True:
        if num < 1 or num > 3:
            print('please get 1~3 !')
            num = int(input('get: '))
        else:
            break
    return num


def aiGet(residual):
    if residual <= 0:
        raise 'ERROR: no residual!'
    n = residual % 4
    if n == 1:
        get = int(random.random()*3 + 1)
    elif n == 0:
        get = 3
    else:
        get = n-1
    return get


def gameover(residual):
    if residual <= 0:
        return True
    else:
        return False


def game():
    residual = 16
    print('豆堆游戏，共16粒豆子。两人每次取1-3粒，取到最后一粒的输。您先取。')
    while residual > 0:
        # 用户取豆子
        person_get = personGet()
        if person_get > residual:
            person_get = residual
        residual -= person_get
        print('您取了', person_get, '粒豆子')
        print('豆堆剩余:', residual)
        if gameover(residual):
            print('游戏结束, 您输了。')
            break
        # AI取豆子
        ai_get = aiGet(residual)
        if ai_get > residual:
            ai_get = residual
        residual -= ai_get
        print('电脑取了', ai_get, '粒豆子')
        print('豆堆剩余:', residual)
        if gameover(residual):
            print('太棒啦，您赢啦！')
            break


while True:
    game()
