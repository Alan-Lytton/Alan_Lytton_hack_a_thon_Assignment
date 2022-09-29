from classes.ninja import Ninja
from classes.pirate import Pirate
import random

michelangelo = Ninja("Michelanglo")

jack_sparrow = Pirate("Jack Sparrow")

both_alive = True

while both_alive == True:
    ran_number = random.randrange(1,11)
    if ran_number == (1 or 2 or 3 or 4 or 5):
        michelangelo.attack(jack_sparrow)
        print(f"{michelangelo.name} attacks {jack_sparrow.name} for with a strength of {michelangelo.strength}. {jack_sparrow.name} has {jack_sparrow.health} health remaining")
    elif ran_number == (6 or 7 or 8):
        jack_sparrow.attack(michelangelo)
        print(f"{jack_sparrow.name} attacks {michelangelo.name} for with a strength of {jack_sparrow.strength}. {michelangelo.name} has {michelangelo.health} health remaining")
    else:
        print(f"{michelangelo.name} and {jack_sparrow.name} both attack but miss. No health is lost.")
    if (michelangelo.health > 0) and (jack_sparrow.health > 0):
        both_alive = True
    else:
        if (michelangelo.health > 0) and (jack_sparrow.health == 0):
            print(f"The winner is {michelangelo.name}")
        else:
            print(f"The winner is {jack_sparrow.name}")
        both_alive = False
