import random

class Character:
    def __init__(self, name, health, attack_power, attack_modifier = 1, shield = False):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health
        self.attack_modifier = attack_modifier
        self.shield = shield
        
    def attack(self, opponent):
        total_attack = self.attack_power * self.attack_modifier
        total_attack = int(total_attack) # if total_attack becomes a float, convert back to an int
        
        if opponent.shield == True:
            total_attack = total_attack / 2
            opponent.health -= total_attack
        else:
            opponent.health -= total_attack
    
        print(f"{self.name} attacks {opponent.name} for {total_attack} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
                

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")
        
    def heal(self):
        add_health = random.randrange(2, 15, 1)
        self.health += add_health
        if self.health > self.max_health:
            self.health = self.max_health
            print(f"You've healed to max health! Health: {self.health}/{self.max_health}")
        else:    
            print(f"You healed {add_health}HP! Health: {self.health}/{self.max_health}")

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=40)
        
    def special_ability(self):
        if self.shield == False:
            self.shield = True
            self.attack_modifier = .5
            print('You raise your shield high, prioritizing your defense over damage!')
        else:
            self.shield = False
            self.attack_modifier = 1
            print("You lower your shield, ready to attack at full force!")

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=30)
        
    def special_ability(self):
        self.attack_modifier += .5
        print("You feel magical energy building within you...")
        
    def attack(self, opponent):
        result = super().attack(opponent) # store the result of the attack
        
        self.attack_modifier = 1 # reset the modifer to 1
        
        return result # then return the original result before the modifer was changed

        
class Druid(Character):
    def __init__(self, name, wild_shape = False):
        super().__init__(name, health=120, attack_power=30)
        self.wild_shape = wild_shape
        
    def special_ability(self):
        if self.wild_shape == True:
            print("You've shifted back into your human form...")
            self.wild_shape = False
        else:
            self.wild_shape = True
            print("Your form shifts and forms to become a massive bear! Lets see how the wizard will handle this...")
            
    def attack(self, opponent):
        if self.wild_shape == True:
            self.attack_modifier = 2
            return super().attack(opponent)
        else:
            return super().attack(opponent)
        
class Bard(Character):
    class Mage(Character):
        def __init__(self, name):
            super().__init__(name, health=110, attack_power=30)
            
        def special_ability(self):
            pass
        
# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        add_health = random.randrange(5, 10, 5)
        
        if self.health + add_health < self.max_health:
            self.health += add_health
            print(f"{self.name} regenerates {add_health}HP! Current health: {self.health}HP")
        else:
            self.health = self.max_health
            print(f"{self.name} has regenerated to full health! Current health: {self.health}HP")