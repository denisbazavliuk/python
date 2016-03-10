# -*- coding:utf-8 -*-
import sys
import random

# main game class, includes hero and dragon attributes and chest calculation
class HeroesDragons():
    hero = {
        'hp': 1000,
        'defense': 100,
        'strength': 120,
        'weapon': 250,
        'shield': 150
    }
    dragon = {
        'hp': 2000,
        'defense': 120,
        'strength': 150,
        'weapon': 0
    }

    def chest_random(self):      # chest calculation, 1 is for + 100 hp, 2 is for - 1000 hp (game over), other - empty
        self.chest = random.randint(1, 5)
        self.chest = str(self.chest)
        if self.chest == '1':
            print u'Выпало оружие +100 к удару'
            self.hero['weapon'] += 100
        elif self.chest == '2':
            self.hero['hp'] -= 10000
            sys.exit('Тебе пиздец. Game Over')
        elif self.chest == '3' or '4' or '5':
            print u'Тебе ничего не досталось'

    def yesorno(self):    # yes or no for chest opening
        print u'ПОМНИТЕ ! В СУНДУКЕ МОЖЕТ ЛЕЖАТЬ ВАШЕ СПАСЕНИЕ, СМЕРТЬ ИЛИ ВООБЩЕ НИЧЕГО'
        self.yesOrNo = str(raw_input('Вы уверены ? yes или no: '))
        if self.yesOrNo == 'yes':
            print self.chest_random()
        elif self.yesOrNo == 'no':
            print u'Ну как хотите'


# hero class, includes hero attacking, hero defending and chest opening
class Hero(HeroesDragons):
    def hero_attack(self):
        self.choose = str(raw_input('Выбери действие героя: att,def, shield или сундук chest: '))
        if self.choose == 'att':
            print u'====Атака героя===='
            self.attack = self.hero['strength'] + self.hero['weapon']
            self.attackResult = self.attack - self.dragon['defense']
            self.dragon['hp'] = self.dragon['hp'] - self.attackResult
            print u'Урон составил - %s, у дракона осталось - %s HP'% (self.attackResult, self.dragon['hp'])
        elif self.choose == 'def':
            print u'Герой не будет атаковать, но получит + 100 к HP'
            self.hero['hp'] += 100
        elif self.choose == 'shield':
            self.hero['defense'] += self.hero['shield']
            print u'У героя теперь улучшенная броня - %s'% (self.hero['defense'])
        elif self.choose == 'chest':
            print self.yesorno()
        elif self.choose != 'def' or 'att' or 'shield':
            print u'Неправильный ввод, пропуск хода, будьте внимательны'

        if self.dragon['hp'] <= 0:
            sys.exit('Game Over: Hero Wins')
        else:
            pass


# dragon class, includes dragon attacking and defending
class Dragon(Hero, HeroesDragons):
    def dragon_attack(self):
            self.choose = str(raw_input('Выбери действие дракона: att или def: '))
            if self.choose == 'att':
                print u'====Атака дракона===='
                self.attack = self.dragon['strength'] + self.dragon['weapon']
                self.attackResult = self.attack - self.hero['defense']
                self.hero['hp'] -= self.attackResult
                print u'Урон составил - %s, у героя - %s HP' % (self.attackResult, self.hero['hp'])
            elif self.choose == 'def':
                print u'Дракон не будет атаковать, но получит + 100 HP'
                self.dragon['hp'] += 100
            elif self.choose != 'att' or 'def':
                print u'Неправильный ввод, пропуск хода, будьте внимательны'

            if self.hero['hp'] <= 0:
                sys.exit('Game Over: Dragon Wins')
            else:
                pass

# game constructor, forces infinite loop till hero or dragon ['hp'] will <= 0
class Game(HeroesDragons, Hero, Dragon):
    def __init__(self):
        while True:
            print self.hero_attack()
            print '================'
            print self.dragon_attack()
            continue

a = Game()
print a