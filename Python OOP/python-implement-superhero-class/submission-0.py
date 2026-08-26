class SuperHero:
    """
    A class to represent a superhero.

    Attributes:
        name (str): The superhero's name
        power (str): The superhero's main superpower
        health (int): The superhero's health points
    """

    def __init__(self, name: str, power: str, health: int):
        # TODO: Initialize the superhero's attributes here
        self.name = name
        self.power = power
        self.health = health


# TODO: Create Superhero instances
superhero_01 = SuperHero("Batman", "Intelligence", 100)
superhero_02 = SuperHero("Superman", "Strength", 150)

# TODO: Print out the attributes of each superhero

print(superhero_01.name)
print(superhero_01.power)
print(superhero_01.health)
print(superhero_02.name)
print(superhero_02.power)
print(superhero_02.health)