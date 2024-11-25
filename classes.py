from dataclasses import dataclass
from abilities import shield_block, focus_magical_energy, wild_shape, cast_sleep
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
        "Warrior": ["Shield Block", "Battle Cry"],
        "Mage": ["Focus Magical Energy", "Mana Shield"],
        "Druid": ["Wild Shape", "Thorn Armor"],
        "Bard": ["Cast Sleep", "Dazzling Flurry"]
    }
    
    def __post_init__(self):
        self.max_health = self.health
        
    def attack(self, opponent):
        max_attack = int(self.attack_power * self.attack_modifier)
        total_attack = random.randint(1, max_attack)
        
        if opponent.shield == True:
            opponent.shield = False
            total_attack = int(total_attack / 2)
            opponent.health -= total_attack
        else:
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
                shield_block(self)
            elif abilities[selection - 1] == "EMPTY":
                pass
            elif abilities[selection - 1] == "Focus Magical Energy":
                focus_magical_energy(self)
            elif abilities[selection - 1] == "":
                pass
            elif abilities[selection - 1] == "Wild Shape":
                wild_shape(self)
            elif abilities[selection - 1] == "":
                pass
            elif abilities[selection - 1] == "Cast Sleep":
                cast_sleep(opponent)
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

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=30, player_class = "Mage")
     
    def attack(self, opponent):
        if self.attack_modifier > 1:
            result = super().attack(opponent) # store the result of the attack
            self.attack_modifier = 1 # reset the modifer to 1
            print("The power of your focused energy adds to your magical blast!")
            return result # then return the original result before the modifer was changed
        else:
            return super().attack(opponent)

class Druid(Character):
    def __init__(self, name, wild_shape = False):
        super().__init__(name, health=120, attack_power=30, player_class = "Druid")
        self.wild_shape = wild_shape
            
    def attack(self, opponent):
        if self.wild_shape == True:
            print("You swipe at the wizard with your massive bear claws!")
            return super().attack(opponent)
        else:
            return super().attack(opponent)
        
class Bard(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=30, player_class = "Bard")
        
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