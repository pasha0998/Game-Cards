class Warrior:
    def __init__(self, health = 100, stamina = 100):
        self.__health = health
        self.__stamina = stamina

    def get_health(self):
        return self.__health

    def set_health(self, points):
        self.__health += points
        if self.__health > 100:
            self.__health = 100
        elif self.__health < 0:
            self.__health = 0
#рассказ героя о себе
    def introduces(self):
        print("---------")
        print(f"Class: {self.__class__.__name__}")
        print(f"Health: {self.get_health()}")
        print(f"Stamina:{self.__stamina}")
        print("---------")
#лечение героев
    def heals(self, target):
        print("---------")
        print(f"{self.__class__.__name__} накладывает повязку из лечебных трав"
              f" {target.__class__.__name__}")
        if self.__stamina >= 20:
            target.set_health (10)
            self.__stamina -= 20
            print(f"Здоровье у {target.__class__.__name__} увеличилось до {target.get_health()}")
            print(f"У {self.__class__.__name__} осталось {self.__stamina} единиц магии")
        else:
            print("Недостаточно сил")
            print("---------")
#атака героя
    def attacks(self, target):
        print("---------")
        print(f"{self.__class__.__name__} наносит урон мечом"
              f" {target.__class__.__name__}")
        if target.get_health() > 3:
            target.set_health(-3)
            print(f"Здоровье у {target.__class__.__name__} понижено до {target.get_health()}")
        else:
            print(f"{target.__class__.__name__} покидает отряд")
        print("---------")

class Mage:
    def __init__(self, health = 100, mana = 100):
        self.__health = health
        self.__mana = mana

    def get_health(self):
        return self.__health

    def set_health(self, points):
        self.__health -= points
        if self.__health > 100:
            self.__health = 100
        elif self.__health < 0:
            self.__health = 0
#рассказ героя о себе
    def introduces(self):
        print("---------")
        print(f"Class: {self.__class__.__name__}")
        print(f"Health: {self.get_health()}")
        print(f"Mana.{self.__mana}")
        print("---------")
#лечение героев
    def heals(self, target):
        print("---------")
        print(f"{self.__class__.__name__} применяет заклинание лечения"
              f" к {target.__class__.__name__}")
        if self.__mana >= 20:
            target.set_health(10)
            self.__mana -= 20
            print(f"Здоровье у {target.__class__.__name__} увеличилось до {target.get_health()}")
            print(f"У {self.__class__.__name__} осталось {self.__mana} единиц магии")
        else:
            print("Недостаточно магии")
        print("---------")
#атака героя
    def attacks(self, target):
        print("---------")
        print(f"{self.__class__.__name__} наносит урон магией"
              f" {target.__class__.__name__}")
        if target.get_health() > 3:
            target.set_health(-3)
            print(f"Здоровье у {target.__class__.__name__} понижено до {target.get_health()}")
        else:
            target.set_health(-3)
            print(f"{target.__class__.__name__} покидает отряд")
        print("---------")


unit1 = Warrior(1, 10)
#print("Warrior:",unit1.__dict__)

unit2 = Warrior()
#print("Warrior:",unit2.__dict__)

unit3 = Mage(1, 10)
#print("Mage:", unit3.__dict__)

unit4 = Mage()
#print(unit4.get_health())
#print("Mage:", unit4.__dict__)

#рассказ героя о себе
#unit1.introduces()

#рассказ героя о себе
#unit2.introduces()

#рассказ героя о себе
#unit3.introduces()

#рассказ героя о себе
#unit4.introduces()

#лечение mage
#unit1.heals(unit3)

#лечение mage
#unit3.heals(unit1)

#атака warrior
#unit1.attacks(unit3)

#атака mage
#unit3.attacks(unit1)

#unit2.heals(unit1)
#unit2.attacks(unit3)

#unit1 = Warrior (50, 50)
#unit2 = Mage(50, 50)

#unit1.heals(unit2)
#unit2.heals(unit1)

#unit1.attacks(unit2)
#unit2.attacks(unit1)
