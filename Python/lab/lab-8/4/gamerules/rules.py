def bomb(num):
    if num > 21:
        return True
    elif num >= 0 and num <= 21:
        return False
    else:
        raise Exception('扑克牌的和值应该为非负整数。')


def sum_pokers(pokers_list):
    sum = 0
    for poker in pokers_list:
        poker_num = poker.get_number()
        if poker_num > 10:
            poker_num = 10
        elif poker_num == -1:
            poker_num = 0
        sum += poker_num
    return sum


def who_win(n1, n2):
    p1_bomb = bomb(n1)
    p2_bomb = bomb(n2)
    who_win = [False, False]
    if not p1_bomb and p2_bomb:
        who_win[0] = True
    elif not p2_bomb and p1_bomb:
        who_win[1] = True
    elif not p1_bomb and not p2_bomb:
        if n1 > n2:
            who_win[0] = True
        elif n2 > n1:
            who_win[1] = True
    return who_win

if __name__=='__main__':
    print('bomb(21)', bomb(21))
    # print('bomb(0)', bomb(0))
    # print('bomb(-1)', bomb(-1))
    print('bomb(22)', bomb(22))

    print('bomb(21)', bomb(21))
    
    