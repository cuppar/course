import copy


class Player:
    def __init__(self, base_poker):
        self.base_poker = base_poker
        self.open_pokers = []

    def add_poker(self, poker):
        self.open_pokers.append(poker)

    def get_base_poker(self):
        return self.base_poker

    def get_open_pokers(self):
        return self.open_pokers

    def get_all_pokers(self):
        # return [copy.deepcopy(self.base_poker)].extend(copy.deepcopy(self.open_pokers))
        all_pokers=[]
        all_pokers.append(self.base_poker)
        all_pokers.extend(self.open_pokers)
        return all_pokers
