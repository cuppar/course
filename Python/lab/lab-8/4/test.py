from dealcards import Deck, Poker, Decker
from gamerules import Player, bomb, sum_pokers, who_win


def start_game():
    print('game start!')
    decker = Decker()
    player = Player(decker.deal())
    print('your base poker is', player.get_base_poker().get_description())
    ai = Player(decker.deal())
    game_over = False

    def show_pokers(player, name, show_base):
        base = 'base'
        if show_base == True:
            base = player.get_base_poker().get_description()
        print(name, ': '+base+' ', end='')
        for poker in player.get_open_pokers():
            print(poker.get_description()+' ', end='')
        print()

    def show():
        show_pokers(player, 'you', True)
        show_pokers(ai, 'ai', False)

    while not game_over:
        player_stop = True
        ai_stop = True
        # 玩家回合
        show()
        option = input('your turn :: do you want add a poker?(y/n) :')
        if option == 'y':
            player.add_poker(decker.deal())
            player_stop = False
        else:
            print('your turn :: you stop!')

        # 电脑回合
        show()
        if sum_pokers(ai.get_open_pokers()) \
                < sum_pokers(player.get_open_pokers())\
                and not bomb(sum_pokers(player.get_open_pokers())):
            ai.add_poker(decker.deal())
            print('ai turn :: add a poker')
            ai_stop = False
        else:
            print('ai turn :: ai stop')

        if player_stop and ai_stop:
            game_over = True
            print('you and ai both stop!')
            print('###### final battle ######')
            player_iswin, ai_iswin = who_win(sum_pokers(player.get_all_pokers()),
                                             sum_pokers(ai.get_all_pokers()))
            show_pokers(player, 'you', True)
            show_pokers(ai, 'ai', True)
            print('your sum:', sum_pokers(player.get_all_pokers()))
            print('ai sum:', sum_pokers(ai.get_all_pokers()))
            if player_iswin and not ai_iswin:
                print('winner is you!')
            elif not player_iswin and ai_iswin:
                print('winner is ai')
            elif not player_iswin and not ai_iswin:
                print('平局')


if __name__ == '__main__':
    start_game()
