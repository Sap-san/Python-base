import random


class Barrel:
    def __init__(self):
        self.barrel_nums = random.sample(range(1, 91), 90)
        self.barrel = 0
        self.right = 0

    def barrel_open(self):
        self.barrel = self.barrel_nums.pop()
        print(f'Выбран бочонок: {self.barrel}')


class Card:
    def __init__(self):
        self.start_nums = random.sample(range(1, 91), 15)
        self.card_nums = self.gen_list()
        self.right = 0

    def gen_list(self):
        card_nums = [sorted(self.start_nums[:5]), sorted(self.start_nums[5:10]), sorted(self.start_nums[10:15])]
        for i in range(3):
            gap_gen = sorted(random.sample(range(9), 4))
            for g in gap_gen:
                card_nums[i].insert(g, '  ')
        return card_nums

    def print_card(self, card_nums):
        print('-' * 35)
        for row in card_nums:
            print(*row, sep='\t')
        print('-' * 35)

    def line(self, barrel):
        row = self.start_nums.index(barrel) // 5
        self.card_nums[row][self.card_nums[row].index(barrel)] = '--'
        self.right += 1


class PlayerCard(Card):
    def choice(self, barrel):
        while True:
            answer = input('Выберите зачеркнуть(нажмите - 1) или продолжить(нажмите - 0): ')
            if answer in ('0', '1'):
                break
            print('Некорректный ответ')
        if answer == '1' and barrel in self.start_nums:
            self.line(barrel)
            return True
        elif (answer == '1' and barrel not in self.start_nums) or (answer == '0' and barrel in self.start_nums):
            return False
        else:
            return True


class CompCard(Card):
    def new_barrel(self, barrel):
        if barrel in self.start_nums:
            self.line(barrel)


bar = Barrel()
pl = PlayerCard()
comp = CompCard()

pl.print_card(pl.card_nums)
comp.print_card(comp.card_nums)
result = True
while result:
    bar.barrel_open()
    result = pl.choice(bar.barrel)
    print(result)
    comp.new_barrel(bar.barrel)
    if pl.right == 15 and comp.right == 15:
        print('Ничья')
        break
    elif pl.right == 15:
        print('Поздравляем, вы победили!')
        break
    elif comp.right == 15:
        print('К сожалению, победил компьютер.')
        break
    if not result:
        print('Вы ошиблись и проиграли.')
    else:
        pl.print_card(pl.card_nums)
        comp.print_card(comp.card_nums)
