import random

def shield_block(self):
    if self.shield == False:
        self.shield = True
        print(f'{self.name} raises their shield high, bracing for an attack!')
    else:
        print(f"{self.name}'s shield is already raised!")
        
def focus_magical_energy(self):
    self.attack_modifier += .5
    print(f"{self.name} feels the might of magical energy building within them, increasing future damage...")
    
def wild_shape(self, opponent):
    if self.wild_shape == True:
        self.wild_shape = False
        self.attackmodifer = 1
        print(f"{self.name} shifted back into their human form...")
    else:
        self.wild_shape = True
        self.attack_modifer = 1.5
        print(f"{self.name}'s form shifts into a massive bear! Lets see how {opponent.name} will handle this...")
        
def cast_sleep(self, opponent):
    if opponent.sleep <= 0:
        opponent.sleep += random.randint(2, 3)
        print(f"{self.name} plucks the strings of their lute and sing a soothing song to {opponent.name}. \nThey're now fast asleep...")
    else:
        print(f"{opponent.name} is already asleep, {self.name}'s song doesn't affect {opponent.name}...")
    
def dazzling_flurry(self, opponent):
    max_attack = int((self.attack_power * self.attack_modifier) * 2)
    total_attack = random.randint(int(max_attack / 2), max_attack)
    opponent.health -= total_attack
    print(f"{self.name} dances with a brilliant display of blows and attacks dealing {total_attack} damage!")

def battle_cry(self, opponent):
    self.attack_modifier = 1.5
    opponent.attack_modifier = .75
    print(f"{self.name} goes into a rage, increasing their damage and reducing any incoming damage!")

def mana_shield(self):
    if self.shield == False:
        self.shield = True
        print(f"A magical barrier forms around {self.name}, reducing incoming damage!")
    else:
        print(f"{self.name}'s mana shield is already up!")

def thorn_armor(self):
    if self.thorn_armor == False:
        self.thorn_armor = True
        print(f"A wild suit of prickely armor forms around {self.name}, dealing damage in retaliation of taking damage.")
    else:
        print(f"There's already a suit of thorn armor protecting {self.name}.")
    

