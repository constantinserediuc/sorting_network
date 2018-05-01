import random

from GA.Chromosome import *
from SortingNetwork.GreenFilter import *
from SortingNetwork.RandomSortingNetworkFactory import RandomSortingNetworkFactory


class Population(object):
    def __init__(self, chromosomes):
        self.pop_size = len(chromosomes)
        self.chromosomes = chromosomes

    @staticmethod
    def get_random_population_with_Green_filter(pop_size, nr_wires):
        nr_comparators = GreenFilter.get_nr_comparators_for(nr_wires)
        chromosomes = []
        for _ in range(pop_size):
            sn = RandomSortingNetworkFactory.get_sorting_network_with(nr_wires, nr_comparators)
            chromosomes.append(Chromosome(sn))
        chromosomes.append(GreenFilter.get_filter(nr_wires))
        i = random.randint(0, pop_size)
        chromosomes[i] = Chromosome(GreenFilter.get_filter(nr_wires))
        pop = Population(chromosomes)
        return pop
