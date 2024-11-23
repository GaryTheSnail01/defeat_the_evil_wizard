import random
from classes import Warrior, Druid, Mage, Bard, EvilWizard
        
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
            player.special_abilities(wizard)
        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.display_stats()
            continue
        else:
            print("Invalid choice. Try again.")
            continue

        if wizard.health > 0:
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