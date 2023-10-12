import time
import random


def print_pause(string):
    print(string)
    time.sleep(2)


def fight_to_win(animal, weapon):
    print_pause(f"As the {animal} moves to attack,"
    f"you unsheath your {weapon}")
    print_pause(f"The {weapon} shines brightly in"
    "your hand as you brace your self for the attack.")
    print_pause(f"But the {animal} takes one look "
    "at your shiny new weapon and runs away!")
    print_pause(f"You have rid the town of the {animal}. You are victorious!")
    game = input("Would you like to play again? (y/n)")
    if game == 'y':
        intro()
        play_game(animal, weapon)
    else:
        if game == 'n':
            print_pause("GAME OVER\n")
            print_pause("Thanks for playing! See you next time.")


def fight(animal, weapon):
    print_pause("You do your best...")
    print_pause(f"but your dagger is no match for the {animal}.")
    print_pause("You have been defeated!")
    game = input("Would you like to play again? (y/n)")
    if game == 'y':
        intro()
        play_game(animal, weapon)
    else:
        print("Thanks for playing! See you next time.")



def run(animal, weapon):
    print_pause("You run back into the field. Luckily,"
    " you don't seem to have been followed.")
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    play_game(animal, weapon)



def intro():
    print_pause("You find yourself standing in an open"
    " field, filled with grass, and yellow wildflowers.")
    print_pause("Rumor has it that a wicked fairie is somewhere" 
                " around here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty"
    " (but not very effective), dagger.")
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")


def choice_one(animal, weapon):
    print_pause("You approach the door of the house.")
    print_pause(f"You are about to knock when"
    f" the door opens and out step a {animal}.")
    print_pause(f"Eep! This is the {animal}'s house!")
    print_pause(f"The {animal} attacks you!")
    print_pause(f"You feel a bit under-prepared for "
            " this, what with only having a tiny dagger.\n")
    choice = input("Would you like to (1) fight or (2) run away?")
    if choice == '1':
        fight(animal, weapon)
    if choice == '2':
        run(animal, weapon)


def choice_two(animal, weapon):
    print_pause("You peer cautiously into the cave.")
    print_pause("It turns out to be only a very small cave.")
    print_pause("Your eye catches a glint of metal behind a rock.")
    print_pause(f"You have found the magical {weapon}!")
    print_pause(f"You discard your silly old"
                f" dagger and take the {weapon} with you")
    print_pause("You walk back out to the field\n")
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    choice = input("What would you like to do? (Please enter 1 or 2.)")
    if choice == '1':
        print_pause("You approach the door of the house.")
        print_pause(f"You are about to knock when the"
                    f" door opens and out step a {animal}.")
        print_pause(f"Eep! This is the {animal}'s house!")
        print_pause(f"The {animal} attacks you!")
        while True:
            choice = input("Would you like to (1)"
                    "fight or (2) run away?")
            if choice == '1':
                fight_to_win(animal, weapon)
            else:
                if choice == '2':
                    run(animal, weapon)
        return choice
    else:
        choice_two(animal, weapon)
    


def play_game(animal, weapon):
    while True:
        choice = input("What would you like to do? \n (Please enter 1 or 2.)")
        if choice == '1':
            choice_one(animal, weapon)
        else:
            if choice == '2':
                choice_two(animal, weapon)
    return choice

                

def start_game():
    animals = ['dragon', 'gorgon', 'beast', 'snake']
    weapons = ['Sword of Ogoroth!', 'Machine Gun', 'Chainsaw', 'Acid Sprayer']
    animal = random.choice(animals)
    weapon = random.choice(weapons)

    intro()
    play_game(animal, weapon)

start_game()