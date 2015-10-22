#! /usr/bin/python3
import random
import copy
from sorting_network import SortingNetwork, NUM_COMPARATORS, NUM_INPUTS

POPULATION_SIZE = 4 #MUST BE DIVISIBLE BY 2

class Individual:
    def __init__(self):
        """
            Creates a new Individual
        """
        self.network = SortingNetwork()
        self.fitness = 0.0

    def __str__(self):
        return "Fitness: {: >6.2f}, Network: {}".format(self.fitness, self.network)

class Population:

    def __init__(self):
        """
            Creates a random population of individuals of size POPULATION_SIZE
        """
        self.individuals = [Individual() for i in range(POPULATION_SIZE)]

    def __str__(self):
        string = "Population:\n"
        for i in self.individuals:
            string += "   " + str(i) + "\n"
        return string

    def evaluate(self):
        """
            Determine the fitness of each individual in the population.
            Sort the population from high fitness to low fitness.
        """

        ### FILL THIS IN ###
        for ind in self.individuals:
            ind.fitness = ind.network.evaluate()
        self.individuals.sort(key=lambda x: x.fitness, reverse=True)

    def select(self):
        """
            Use Roulette Wheel to select individuals for next generation
            Always propagate the best 2 individuals to the next generation

            WARNING: Remember to deepcopy the individuals so you don't
            have two elements in self.individuals that are pointers to the
            same individual
        """


        ### FILL THIS IN ###
        roulette_wheel = []

        totalfitness = sum(individual.fitness for individual in self.individuals)
        weightfitness = [(self.individuals[individual].fitness/totalfitness)for individual in range(len(self.individuals))]

        for weight in range(len(weightfitness)):
            weight_sum = sum(weightfitness[n] for n in range(weight+1))
            roulette_wheel.append(weight_sum)
        new_population = copy.deepcopy(self.individuals[:2])

        for population in range(POPULATION_SIZE-2):
            pSize = 0
            while pSize < POPULATION_SIZE:
                if random.random() < roulette_wheel[pSize]:
                    new_population.append(copy.deepcopy(self.individuals[pSize]))
                    pSize = POPULATION_SIZE
                pSize += 1


        self.individuals = copy.deepcopy(new_population)

    def crossover(self):
        """
            With probability CROSSOVER_RATE, perform uniform crossover.
            Otherwise, copy parents.

            Always propagate the best 2 individuals to the next generation

            WARNING: Ensure mutated comparators are still legal
                     (see SortingNetwork __init__)
        """
        CROSSOVER_RATE = 0.75
        firstComparator = int(NUM_COMPARATORS * CROSSOVER_RATE)
        new_population = copy.deepcopy(self.individuals)


        for popSize in range(2,POPULATION_SIZE):
            firstParent = random.randint(0,POPULATION_SIZE-1)
            secondParent = random.randint(0,POPULATION_SIZE-1)
            for comparator in range(NUM_COMPARATORS):
                if comparator < firstComparator:
                    new_population[popSize].network.comparators[comparator] = copy.deepcopy(self.individuals[firstParent].network.comparators[comparator])
                if (comparator == firstComparator) and (self.individuals[firstParent].network.comparators[comparator-1] == self.individuals[secondParent].network.comparators[comparator]):
                    new_population[popSize].network.comparators[comparator] = copy.deepcopy(self.individuals[secondParent].network.comparators[comparator-1])
                else:
                    new_population[popSize].network.comparators[comparator] = copy.deepcopy(self.individuals[secondParent].network.comparators[comparator])
        self.individuals = copy.deepcopy(new_population)


    def mutate(self):
        """
            With probability MUTATION_RATE, mutate the individual's network

            WARNING: Ensure mutated comparators are still legal
                     (see SortingNetwork __init__)
        """
        MUTATION_RATE  = 1/NUM_COMPARATORS

        network=[(x, y) for x in range (NUM_INPUTS) for y in range(NUM_INPUTS) if x<y]
        for popSize in range(POPULATION_SIZE):
            if random.random() < MUTATION_RATE:
                pos = random.randint(1, NUM_COMPARATORS-2)
                looFlag = 1
                while looFlag > 0:
                    looFlag = 0
                    self.individuals[popSize].network.comparators[pos] = random.sample(network, 1)[0]
                    if self.individuals[popSize].network.comparators[pos] == self.individuals[popSize].network.comparators[pos-1]\
                            or self.individuals[popSize].network.comparators[pos] == self.individuals[popSize].network.comparators[pos+1]:
                        looFlag = 1

def run_genetic_algorithm():
    """
        Runs a genetic algorithm to find a sorting network with
        NUM_COMPARATORS comparators that sorts all possible arrays
        of size NUM_INPUTS
    """

    ### FILL THIS IN ###
    population = Population()
    population.evaluate()
    print(population)
    result = population.individuals[0].fitness
    while result <1.0:
        population.select()
        population.crossover()
        population.mutate()
        population.evaluate()
        result = population.individuals[0].fitness
        print(population)


if __name__ == "__main__":
    run_genetic_algorithm()
