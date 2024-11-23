from dataclasses import dataclass
import random

@dataclass
class Character:
    name: str
    player_class: str
    health: int
    attack_power: int
    attack_modifier: int = 1
    shield: bool = False
    sleep: int = 0
    
    class_abilities = {
        "Warrior": ["Shield Block", "EMPTY"],
        "Mage": ["Focus Magical Energy", "EMPTY"],
        "Druid": ["Wild Shape", "EMPTY"],
        "Bard": ["Cast Sleep", "EMPTY"]
    }
    
    def __post_init__(self):
        self.max_health = self.health
        
    def attack(self, opponent):
        total_attack = random.randint(1, (self.attack_power * self.attack_modifier))
        
        if opponent.shield == True:
            total_attack = total_attack / 2
            total_attack = int(total_attack)
            opponent.health -= total_attack
        else:
            total_attack = int(total_attack)
            opponent.health -= total_attack
    
        print(f"{self.name} attacks {opponent.name} for {total_attack} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
                

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power * self.attack_modifier}")
        
    def heal(self):
        add_health = random.randrange(10, 20, 5)
        self.health += add_health
        if self.health > self.max_health:
            self.health = self.max_health
            print(f"You've healed to max health! Health: {self.health}/{self.max_health}")
        else:    
            print(f"You healed {add_health}HP! Health: {self.health}/{self.max_health}")
            
    def special_abilities(self, opponent):
        option = 1
        abilities = self.class_abilities.get(self.player_class, []) # get the list of special abilities based on the player's class. Returns an empty list in case class is unknown.
        
        for a in abilities:
            print(f"{option} - {a}")
            option += 1
        
        try:    
            selection = int(input("Choose an ability: "))
            
            if abilities[selection - 1] == "Shield Block":
                self.shield_block()
            elif abilities[selection - 1] == "EMPTY":
                pass
            elif abilities[selection - 1] == "Focus Magical Energy":
                self.focus_energy()
            elif abilities[selection - 1] == "":
                pass
            elif abilities[selection - 1] == "Wild Shape":
                self.wild_shape()
            elif abilities[selection - 1] == "":
                pass
            elif abilities[selection - 1] == "Cast Sleep":
                self.cast_sleep()
            elif abilities[selection - 1] == "":
                pass
            else:
                pass
        except ValueError:
            print("Invalid input. Please enter a number.")
            return
            

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=40, player_class = "Warrior")
        
    def shield_block(self):
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
        super().__init__(name, health=100, attack_power=30, player_class = "Mage")
        
    def special_ability(self, opponent):
        self.attack_modifier += .5
        print("You feel magical energy building within you...")
        
    def attack(self, opponent):
        result = super().attack(opponent) # store the result of the attack
        
        self.attack_modifier = 1 # reset the modifer to 1
        
        return result # then return the original result before the modifer was changed

class Druid(Character):
    def __init__(self, name, wild_shape = False):
        super().__init__(name, health=120, attack_power=30, player_class = "Druid")
        self.wild_shape = wild_shape
        
    def special_ability(self, opponent):
        if self.wild_shape == True:
            print("You've shifted back into your human form...")
            self.wild_shape = False
        else:
            self.wild_shape = True
            print("Your form shifts and forms to become a massive bear! Lets see how the wizard will handle this...")
            
    def attack(self, opponent):
        if self.wild_shape == True:
            self.attack_modifier = 1.5
            return super().attack(opponent)
        else:
            self.attack_modifier = 1
            return super().attack(opponent)
        
class Bard(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=30, player_class = "Bard")
        
    def special_ability(self, opponent):
        if opponent.sleep <= 0:
            opponent.sleep += 2
            print("You pluck the strings of your lute and sing a soothing song to the wizard. He's now fast asleep...")
        else:
            print("The wizard is already asleep, your song doesn't affect your opponent...")
            return
        
# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15, player_class = None)

    def regenerate(self):
        add_health = random.randrange(5, 10, 5)
        
        if self.health + add_health < self.max_health:
            self.health += add_health
            print(f"{self.name} regenerates {add_health}HP! Current health: {self.health}HP")
        else:
            self.health = self.max_health
            print(f"{self.name} has regenerated to full health! Current health: {self.health}HP")
            
    def attack(self, opponent):
        if self.sleep > 0:
            self.sleep -= 1
            print("The wizard is sleeping and cannot attack...")
            return
        else:
            return super().attack(opponent)