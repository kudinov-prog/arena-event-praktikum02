from random import randint


def main():

    NAMES = ["Джон Сноу", "Дейнерис", "Тирион", "Лорд Бейлиш", "Арья Старк", 
            "Бриенна", "Григор Клиган", "Вонючка", "Санса Старк", "Джейме",
            "Король Ночи", "Бран", "Ходор", "Красная женщина", "Серсея",
            "Мергери", "Варис", "Сем Тарли", "Яра", "Кхал Дрого"]

    CLASSES = ["Paladin", "Warrior"]

    heroes = []

    things = []


    class Thing:

        def __init__(self, name, protection, attack, life_amount):
            self.name = name
            self.protection = protection
            self.attack = attack
            self.life_amount = life_amount
            print (f'Создана вещь {self.name} c характеристиками: '
                   f'процент защиты = {self.protection}, атака = {self.attack}, '
                   f'жизнь = {self.life_amount}')


    class Person:
        
        def __init__(self, name, hp_amount, base_attack, base_protection):
            self.name = name
            self.hp_amount = hp_amount
            self.base_attack = base_attack
            self.base_protection = base_protection
            self.attack_damage = base_attack
            self.final_protection = base_protection
            self.person_things = []

        def setThings(self, things):
            for thing in things:
                self.person_things.append(thing)
                self.attack_damage += thing.attack
                self.final_protection += thing.protection
                self.final_protection = round(self.final_protection, 2)
                self.hp_amount += thing.life_amount

        def attacks(self, defender):
            pass
        
        def defend(self, defender):
            pass


    class Paladin(Person):
        def __init__(self, name, hp_amount, base_attack, base_protection):
            super().__init__(name, hp_amount, base_attack, base_protection)
            self.hp_amount = hp_amount*2
            self.base_protection = round(base_protection*2, 2)
            print (f'Cоздан новый персонаж - Паладин {self.name} '
                   f'с характеристиками: здоровье = {hp_amount},'
                   f'атака = {base_attack},'
                   f'защита = {base_protection}')


    class Warrior(Person):
        pass


    def create_things():
        for new_thing in range(0, 30):
            thing = Thing(name=f'Item_{new_thing}', protection=round(0.01*randint(0, 10), 2),
                        attack=randint(5, 15), life_amount=randint(1, 20))
            things.append(thing)      

    def create_heroes():
        for new_hero in range(1, 10):
            hero_class = CLASSES[randint(0, 1)]
            if hero_class == "Paladin":
                pass
            else:
                pass


    def equip_heroes():
        pass

    def fight():
        pass
    create_things()

if __name__ == "__main__":
    main()
