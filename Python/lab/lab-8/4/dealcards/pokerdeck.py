"""
扑克牌组模块
"""
import random


class Poker:
    """
    扑克牌类
    _is_special: 0->普通牌 1->小鬼 2->大鬼
    _description: 牌面描述
    _assortment:  -1->大小鬼 0->黑桃 1->红心 2->梅花 3->方块
    _number: 牌面大小 A->1 J->11 Q->12 K->13 大小鬼->-1
    """

    def _generate_description(self):
        assortments = {0: '黑桃', 1: '红心', 2: '梅花', 3: '方块'}
        numbers = {1: 'A', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6',
                   7: '7', 8: '8', 9: '9', 10: '10', 11: 'J', 12: 'Q', 13: 'K'}
        if self._is_special == 1:
            return '小鬼'
        if self._is_special == 2:
            return '大鬼'
        return assortments[self._assortment]+numbers[self._number]

    def __init__(self, _assortment=0, _number=3, *, _is_special=0):
        if _is_special != 0:
            if _is_special == 1 or _is_special == '小鬼':
                self._is_special = 1
                self._assortment = -1
                self._number = -1
                self._description = self._generate_description()
                return
            if _is_special == 2 or _is_special == '大鬼':
                self._is_special = 2
                self._assortment = -1
                self._number = -1
                self._description = self._generate_description()
                return
        self._is_special = 0
        self._assortment = _assortment
        self._number = _number
        self._description = self._generate_description()

    def toString(self):
        return '*'*10+self._description+'*'*10+'\n'\
            + 'is special: '+str(self._is_special) + '\n'\
            + 'assortment: '+str(self._assortment) + '\n'\
            + 'number: '+str(self._number) + '\n'\
            + 'description: '+self._description + '\n'\
            + '*'*25+'\n'

    def get_description(self):
        return self._description

    def get_number(self):
        return self._number

    def get_assortment(self):
        return self._assortment

    def get_is_special(self):
        return self._is_special


class Deck:
    def __init__(self):
        self.deck = []
        for i in range(4):
            for j in range(1, 14):
                self.deck.append(Poker(i, j))
        self.deck.append(Poker(_is_special='小鬼'))
        self.deck.append(Poker(_is_special='大鬼'))

    def choice(self):
        return random.choice(self.deck)

    def list_poker(self):
        return self.deck


if __name__ == '__main__':
    # poker1 = Poker(_is_special=1)
    # poker2 = Poker(_is_special=2)
    # poker3 = Poker(_is_special='小鬼')
    # poker4 = Poker(_is_special='大鬼')
    # poker5 = Poker(0, 7)

    # print(poker1.toString())
    # print(poker2.toString())
    # print(poker3.toString())
    # print(poker4.toString())
    # print(poker5.toString())

    def list_poker(deck):
        count = 0
        for poker in deck.list_poker():
            count += 1
            print(count)
            print(poker.get_description())
    deck = Deck()
    list_poker(deck)
    print('#'*50)
    print('choice:', deck.choice().toString())
    print('#'*50)
    list_poker(deck)
    print('#'*50)
    print('choice:', deck.choice().toString())
    print('#'*50)
    list_poker(deck)
    print('#'*50)
    print('choice:', deck.choice().toString())
    print('#'*50)
    list_poker(deck)
    print('#'*50)
    print('choice:', deck.choice().toString())
    print('#'*50)
    list_poker(deck)
