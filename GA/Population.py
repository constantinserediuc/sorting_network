import random

from GA.Chromosome import *
from SortingNetwork.GreenFilter import *
from SortingNetwork.RandomSortingNetworkFactory import RandomSortingNetworkFactory


class Population(object):
    def __init__(self, chromosomes):
        self.pop_size = len(chromosomes)
        self.chromosomes = chromosomes

    @staticmethod
    def get_random_population_with_Green_filter_as_prefix(pop_size, nr_wires, nr_comparators):
        green_filter = GreenFilter.get_filter(Info.NR_WIRES)
        chromosomes = []
        for _ in range(pop_size):
            sn = RandomSortingNetworkFactory.get_sorting_network_with(nr_wires, nr_comparators)
            sorting_network = SortingNetwork()
            sorting_network.set_comparators(green_filter.get_comparators() + sn.get_comparators())
            chromosomes.append(Chromosome(sorting_network))
        # i = random.randint(0, pop_size)
        # chromosomes[i] = Chromosome(GreenFilter.get_filter(nr_wires))
        pop = Population(chromosomes)
        return pop

    @staticmethod
    def get_random_population_with_Green_filter(pop_size, nr_wires, nr_comparators):
        nr_comparators_green = GreenFilter.get_nr_comparators_for(nr_wires)
        nr_comparators = nr_comparators - nr_comparators_green
        chromosomes = []
        for _ in range(pop_size):
            sn = RandomSortingNetworkFactory.get_sorting_network_with(nr_wires, nr_comparators)
            chromosomes.append(Chromosome(sn))
        # i = random.randint(0, pop_size)
        # chromosomes[i] = Chromosome(GreenFilter.get_filter(nr_wires))
        pop = Population(chromosomes)
        return pop
