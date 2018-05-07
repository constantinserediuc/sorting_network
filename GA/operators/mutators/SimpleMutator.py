import copy

from GA.Population import *
from GA.Utils import Info
from SortingNetwork.RandomSortingNetworkFactory import RandomSortingNetworkFactory


class SimpleMutator(object):
    def __init__(self, population):
        self.mutation_rate = Info.MUTATION_RATE
        self.population = population

    def mutate(self):
        population = copy.deepcopy(self.population)
        for chromosome in population.chromosomes:
            for i in range(chromosome.get_sorting_network().get_nr_comparators()):
                r = random.uniform(0, 1)
                if r < self.mutation_rate:
                    chromosome.get_sorting_network().set_comparator(i,
                                                                    RandomSortingNetworkFactory().get_random_comparator(
                                                                        Info.NR_WIRES))
        return population
