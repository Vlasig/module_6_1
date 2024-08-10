class Animal:
    alive = True       # живой
    fed = False        # накормленность

    def __init__(self, alive, fed, name):
        self.alive = alive
        self.fed = fed
        self.name = name

    def eat(self, food):
        if self.edible:
            self.fed = True
            print(f"{self.name} съел {food.name}")
        else:
            self.alive = False
            print(f"{self.name} не стал есть {food.name}")


class Plant:
    edible = False  #съедобность

    def __init__(self, edible, name):
        self.edible = edible
        self.name = name


class Mammal(Animal):
    edible = True

    def __init__(self, name):
        self.name = name


class Predator(Animal):
    edible = False

    def __init__(self, name):
        self.name = name


class Flower(Plant):
    def __init__(self, name):
        self.name = name
        self.edible = False


class Fruit(Plant):
    def __init__(self, name):
        self.name = name
        self.edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a2.name)
print(p2.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
