import random



# Base Character class
class Character:
    def __init__(self, name, health, attack_power, attack_modifier = 1):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health
        self.attack_modifier = attack_modifier  

    def attack(self, opponent):
        total_attack = self.attack_power * self.attack_modifier
        total_attack = int(total_attack) # if total_attack becomes a float, convert back to an int
        opponent.health -= total_attack
        self.attack_modifier = 1 # if attack_modifer > 1, reset to 1
        
        if self.attack_modifier == 1:
            print(f"{self.name} attacks {opponent.name} for {total_attack} damage!")
            if opponent.health <= 0:
                print(f"{opponent.name} has been defeated!")
        else:
            print(f"{self.name} attacks {opponent.name} with a concentrated strike, dealing {total_attack} damage!")
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
        super().__init__(name, health=140, attack_power=35)
        
    def special_ability(self):
        pass # shield ability, halves player damage

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=25)
        
    def special_ability(self):
        self.attack_modifier += .5
        print("You feel magical energy building within you...")
        
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
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=25)
        
    def special_ability(self):
        pass # sing the wizard to sleep, skips a turn

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        add_health = random.randrange(2, 10, 1)
        
        if self.health + add_health < self.max_health:
            self.health += add_health
            print(f"{self.name} regenerates {add_health}HP! Current health: {self.health}HP")
        else:
            pass
        
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Druid") 
    print("4. Bard")  

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Druid(name)
    elif class_choice == '4':
        return Bard(name)
    else:
        print("Invalid choice. Please try again.")
        return create_character()

def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            player.special_ability()
        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice. Try again.")

        if choice == '4':
            continue
        elif wizard.health > 0 and choice == '1' or '2' or '3':
            wizard.attack(player)
            wizard.regenerate()
            

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")

def main():
    player = create_character()
    wizard = EvilWizard("The Evil Wizard")
    battle(player, wizard)

main()