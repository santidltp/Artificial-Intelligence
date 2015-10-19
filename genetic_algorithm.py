#! /usr/bin/python3

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
            print (ind)
        self.individuals.sort(key=lambda x:x.fitness,reverse=True)

    def select(self):
        """
            Use Roulette Wheel to select individuals for next generation
            Always propagate the best 2 individuals to the next generation

            WARNING: Remember to deepcopy the individuals so you don't
            have two elements in self.individuals that are pointers to the
            same individual
        """

        ### FILL THIS IN ###
        pass

    def crossover(self):
        """
            With probability CROSSOVER_RATE, perform uniform crossover.
            Otherwise, copy parents.

            Always propagate the best 2 individuals to the next generation

            WARNING: Ensure mutated comparators are still legal
                     (see SortingNetwork __init__)
        """
        CROSSOVER_RATE = 0.75

        ### FILL THIS IN ###

    def mutate(self):
        """
            With probability MUTATION_RATE, mutate the individual's network

            WARNING: Ensure mutated comparators are still legal
                     (see SortingNetwork __init__)
        """
        MUTATION_RATE  = 1/NUM_COMPARATORS

        ### FILL THIS IN ###

def run_genetic_algorithm():
    """
        Runs a genetic algorithm to find a sorting network with
        NUM_COMPARATORS comparators that sorts all possible arrays
        of size NUM_INPUTS
    """

    ### FILL THIS IN ###
    pass

if __name__ == "__main__":
    # run_genetic_algorithm()
    n = Population()
    n.evaluate()
