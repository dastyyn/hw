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

    def __str__(self):
        return (f"Прозвище: {self.nickname}\n"
                f"Суперспособность: {self.superpower}\n"
                f"Здоровье: {self.health_points}")

    def __len__(self):
        return len(self.catchphrase)


hero = SuperHero(name='Питер Паркер', nickname='Человек-паук', superpower='Паутина',
                 health_points=100, catchphrase='С большой силой приходит большая ответственность')

print(hero.name_print())
hero.health_x2()
print(str(hero))
print(f'Длина фразы: {len(hero.catchphrase)}')
