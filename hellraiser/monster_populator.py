from random import randint

from dice import DiceClass, Dice
from monster import Monster


class MonsterPopulator:

    def __init__(self, challenge_raiting):
        self.challenge_raiting = challenge_raiting

    def initial_population(self, population_quantity = 15):
        #TODO: use a probability function in the future
        population = []
        for i in range(population_quantity):
            p = randint(0, 100)
            if p < 70:
                population.append(Monster('o', (170, 255, 128), Dice(DiceClass._1D2), 0, 1, 0))
                print('orc')
            elif p >= 70 and p < 90:
                population.append(Monster('o', (255, 51, 153), Dice(DiceClass._1D4), 1, 2, 1))
                print('orc boss')
            elif p >= 90:
                population.append(Monster('T', (51, 51, 0), Dice(DiceClass._1D6), 2, 3, 2))
                print('troll')

        return population


    def populate(self):
        pass
