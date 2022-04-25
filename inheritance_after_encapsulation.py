import random

from encapsulation import Warrior, Mage

class Knight(Warrior):
    def __init__(self, health = 100, stamina = 80, armor = 20):
        super().__init__(health, stamina)
        self.armor = armor

    def set_health(self, points):
        if points > 0:
            super().set_health(points)
        elif points < 0:
            if self.armor > abs(points):
                self.armor += points
                print(f"броня у {self.__class__.__name__} понижена до {self.armor}")
            elif self.armor < abs(points) and self.armor > 0:
                self.armor = 0
                print("Броня уничтожена")
            else:
                super().set_health(points)

    def __crtical_hit(self, target):
        target.set_health(-10)
        print("Сработал критический урон")
        print(f"Здоровье у {target.__class__.__name__} понижено до {target.get_health()}")

    def attacks(self, target):
        if random.randint(1, 100) in range (1, 41):
            self.__crtical_hit(target)
        else:
            super().attacks(target)


class Wizard(Mage):
    def __init__(self, health = 100, mana = 100, barrier = 20):
        super().__init__(health, mana)
        self.barrier = barrier

    def set_health(self, points):
        if points > 0:
            super().set_health(points)
        elif points < 0:
            if self.barrier > abs(points):
                self.barrier += points
                print(f"Магический барьер у {self.__class__.__name__} понижен до {self.barrier}")
            elif self.barrier < abs(points) and self.barrier > 0:
                self.barrier = 0
                print("Магический барьер уничтожен")
            else:
                super().set_health(points)

    def __fireball(self, target):
        target.set_health(-15)
        print("Сработал fireball")
        print(f"Здоровье у {target.__class__.__name__} понижено до {target.get_health()}")

    def attacks(self, target):
        if random.randint(1, 100) in range (1, 21):
            self.__fireball(target)
        else:
            super().attacks(target)


unit1 = Knight(100, 80, 1)
unit2 = Warrior(100, 80)
unit3 = Wizard (100, 100, 20)
#unit1.heals(unit2)
#unit2.attacks(unit1)
#unit3.attacks(unit1)
