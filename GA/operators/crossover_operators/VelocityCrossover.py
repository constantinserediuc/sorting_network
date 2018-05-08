import copy

from GA.Population import *
from GA.Utils import Info


class VelocityCrossover(object):
    def __init__(self, population, global_best):
        self.population = population
        self.global_best = global_best
        self.crossover_rate = Info.CROSSOVER_RATE

    def do_crossover_2_parents(self, p1, p2):
        split_index = int(random.uniform(1, len(p1) - 1))
        p1[split_index:] = p2[split_index:]
        sn_1 = SortingNetwork()
        sn_1.set_comparators(p1)
        return Chromosome(sn_1)

    def do_crossover_3_parents(self, p, global_parent, local_parent):
        comparators = []
        for i in range(len(p)):
            r = random.uniform(0, 1)
            if r < 0.5:
                comparators.append(global_parent[i])
            elif r < 0.8:
                comparators.append(local_parent[i])
            else:
                comparators.append(p[i])
        sn = SortingNetwork()
        sn.set_comparators(comparators)
        return Chromosome(sn)

    def do_crossover(self, c):
        chromosome_sn_comparators = c.get_sorting_network().get_comparators()
        global_best_sn_comparators = self.global_best.get_sorting_network().get_comparators()
        local_best_sn_comparators = c.best_so_far["chromosome"]
        if local_best_sn_comparators is None:
            return self.do_crossover_2_parents(chromosome_sn_comparators, global_best_sn_comparators)
        else:
            return self.do_crossover_3_parents(chromosome_sn_comparators, global_best_sn_comparators,
                                               local_best_sn_comparators.get_comparators())

    def crossover(self):
        chromosomes_after_crossover = []
        chromosomes = self.population.chromosomes
        for i in range(self.population.pop_size):
            r = random.uniform(0, 1)
            if r <= self.crossover_rate:
                t = self.do_crossover(chromosomes[i])
                chromosomes_after_crossover.append(t)
            else:
                chromosomes_after_crossover.append(copy.deepcopy(chromosomes[i]))
        return Population(chromosomes_after_crossover)
