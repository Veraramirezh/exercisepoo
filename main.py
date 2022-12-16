#henrique vera ramirez
# exercise a faire
#1
class StringFoo:
    def __init__(self):
        self.chaise = str

    def set_string(self, parametre):
        self.chaise = parametre

    def print_string(self):
        print(self.chaise)

objet = StringFoo()
objet.set_string('femme')
objet.print_string()
#2
class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle: width={self.width}, height={self.height}"

    def air(self):
        return self.width * self.height

    def afficher_infos (self)
        return air
#3
class Circle:
    def __init__(self, radius: int):
        self.radius = radius

    def __str__(self):
        return f"Circle: radius={self.radius}"

    def air(self):
        return pi * self.radius ** 2

    def circumference(self):
        return pi * self.radius ** 2
#4
class Hero:

    def __init__(self, name:str, level, force: int, defense: int):
        self.nom = nom
        self.level = level
        self.force = force
        self.vie = vie
        self.defense = defense
