import copy

from GA.Population import *
from GA.Utils import Info


class OnePointCrossOverOperator(object):
    def __init__(self, population):
        self.population = population
        self.crossover_rate = Info().CROSSOVER_RATE

    def do_crossover(self, c1, c2):
        a = c1.get_sorting_network().get_comparators()
        b = c2.get_sorting_network().get_comparators()
        split_index = int(random.uniform(1, min(
            [len(a), len(b)]) - 1))
        a[split_index:], b[split_index:] = b[split_index:], a[split_index:]
        sn_a, sn_b = SortingNetwork(), SortingNetwork()
        sn_a.set_comparators(a)
        sn_b.set_comparators(b)
        return [Chromosome(sn_a), Chromosome(sn_b)]

    def crossover(self):
        chromosomes_after_crossover = []
        chromosomes = self.population.chromosomes
        number_of_chosen_chromosome = 0
        first_chromosome_for_crossover = None
        for i in range(self.population.pop_size):
            r = random.uniform(0, 1)
            if r <= self.crossover_rate:
                number_of_chosen_chromosome += 1
                if number_of_chosen_chromosome % 2 == 0:
                    t = self.do_crossover(first_chromosome_for_crossover, chromosomes[i])
                    chromosomes_after_crossover.extend(t)
                else:
                    first_chromosome_for_crossover = copy.deepcopy(chromosomes[i])
            else:
                chromosomes_after_crossover.append(copy.deepcopy(chromosomes[i]))
        if number_of_chosen_chromosome % 2 == 1:
            chromosomes_after_crossover.append(copy.deepcopy(first_chromosome_for_crossover))
        return Population(chromosomes_after_crossover)
