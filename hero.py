class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def name_print(self):  # Вывод имени героя
        return f'Имя героя: {self.name}'

    def health_x2(self):  # Умножение здоровья на 2
        self.health_points *= 2
        return self.health_points

    def __str__(self):
        return (f"Прозвище: {self.nickname}\n"
                f"Суперспособность: {self.superpower}\n"
                f"Здоровье: {self.health_points}")

    def __len__(self):
        return len(self.catchphrase)

    def Crit(self):
        self.damage **= 2
        return self.damage


class AirHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def health_x2(self):
        self.health_points **= 2
        self.fly = True
        return self.health_points, self.fly

    def Fact(self):
        return 'Супермен медленнее Флеша '


class SpaseHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def health_x2(self):
        self.health_points **= 2
        self.fly = True
        return self.health_points, self.fly

    def NewPhrase(self):
        return 'True in the True_phrase'

    def Fact(self):
        return 'Герой "Зеленый фонарь" какое-то время был злодеем '

class Villain(AirHero):
    SuperHero.people = 'monster'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase, damage, fly)

    def gen_x(self):
        pass



spider_man = SuperHero('Питер Паркер', 'Человек-паук', 'Паутина',
                 100, 'С большой силой приходит большая ответственность')

superman = AirHero('Кларк Кент', 'Супермен', 'Лазер из глаз',
                1000, 'Смотри, в небо!', 1000)

green_lantern = SpaseHero('Хэл Джордан', 'Зелёный Фонарь', 'Кольцо силы', 100,
                  'Во тьме ночной, при свете дня, злу не укрыться от меня!', 150)

joker = Villain(None, "Джокер", "Хитрость и химия", 50,
                "хи-хи-хи", 50)


def print_hero_info(hero_instance):
    print(hero_instance.name_print())
    hero_instance.health_x2()
    print(str(hero_instance))
    print(f'Длина фразы: {len(hero_instance.catchphrase)}\n')


print_hero_info(spider_man)
print_hero_info(superman)
print_hero_info(green_lantern)
print_hero_info(joker)

print(green_lantern.NewPhrase())
print(superman.Fact())
print(green_lantern.Fact())
print(superman.Crit())
print(green_lantern.Crit())
print(joker.Crit())