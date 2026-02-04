class Fara:
    def __init__(self,name,health):
        self.name = name
        self.health = health
        self.attack_power = health * 50
    def attack(self,enemy):
        enemy.health -= self.attack_power
        print(f"{self.name} attacked {enemy.name} with {self.attack_power} damage") 

class Bro:
    def __init__(self,name,health):
        self.name = name
        self.health = health
        self.attack_power = health * 30
    def attack(self,enemy):
        enemy.health -= self.attack_power
        if self.health <= 0:
            print(f"{self.name} attacked {enemy.name} with {self.attack_power} damage,but {self.name} died from the damage received")

f = Fara("fara",50)
b = Bro("bro",30)
f.attack(b)
b.attack(f)
