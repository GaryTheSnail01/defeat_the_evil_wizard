import random

def shield_block(self):
    if self.shield == False:
        self.shield = True
        print('You raise your shield high, bracing for an attack!')
    else:
        print("Your shield is already raised!")
        return
        
def focus_magical_energy(self):
    self.attack_modifier += .5
    print("You feel the might of your magical energy building within you...")
    
def wild_shape(self):
    if self.wild_shape == True:
        self.wild_shape = False
        self.attackmodifer = 1
        print("You've shifted back into your human form...")
    else:
        self.wild_shape = True
        self.attackmodifer = 1.5
        print("Your form shifts and forms to become a massive bear! Lets see how the wizard will handle this...")
        
def cast_sleep(opponent):
    if opponent.sleep <= 0:
        opponent.sleep += random.randint(2, 3)
        print("You pluck the strings of your lute and sing a soothing song to the wizard. He's now fast asleep...")
    else:
        print("The wizard is already asleep, your song doesn't affect your opponent...")
        return
    
def dazzling_flurry(opponent):
    pass # attack twice in a brilliant dance of blows

def battle_cry(self):
    pass # boost damage by 50% and reduce incoming damage by 25%

def mana_shield(self):
    pass # reduce incoming damage by 50%

def thorn_armor(opponent):
    pass # deal 25% of damage delt to you from your opponent

