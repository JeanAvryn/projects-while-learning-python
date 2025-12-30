# RPG
import random

class Character:
    def __init__(self, name, health):
        self.name = name
        self.__health = health
        
    def get_health(self):
        return self.__health
        
    def take_damage(self, amount):
        self.__health -= amount
        print(f'{self.name} took a damage of {amount}! Health remaining: {self.__health}')
        
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, 80)
    
    def attack(self):
        return random.randint(10, 20)
    
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, 80)
    
    def attack(self):
        return random.randint(5, 40)

knight = Warrior("Sir Gallahad")
wizard = Mage("Gandalf")

damage = knight.attack()
wizard.take_damage(damage)
print(f"Final check - {wizard.name}'s health: {wizard.get_health()}")
        
