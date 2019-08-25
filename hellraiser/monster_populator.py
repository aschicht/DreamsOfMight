from random import randint

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
                population.append(Monster('o', (170, 255, 128)))
                print('orc')
            elif p >= 70 and p < 90:
                population.append(Monster('o', (255, 51, 153)))
                print('orc boss')
            elif p >= 90:
                population.append(Monster('T', (51, 51, 0)))
                print('troll')

        return population


    def populate(self):
        pass
