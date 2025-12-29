class Player:
    def __init__(self, energy, type, weapon):
        self.energy = energy
        self.type = type
        self.weapon = weapon
    def attack(self):
        print('WAPAK!')
        self.energy -= 10

user = Player(200, 'Mage', 'Wand')
print(f'User is a {user.type}, has {user.energy} mana, and uses {user.weapon} as weapon of choice.')
print('User attacked!')
user.attack()
print(f'-{200 - user.energy} mana.')
