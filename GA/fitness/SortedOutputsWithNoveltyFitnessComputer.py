from GA.Utils import Info
from SortingNetwork.GreenFilter import *
from GA.fitness.SortedOutputsFitnessComputer import SortedOutputsFitnessComputer
import numpy


class SortedOutputsWithNoveltyFitnessComputer(object):
    def __init__(self):
        self.nr_wire = Info.NR_WIRES
        self.sorted_seq = []
        self.max_sequence_to_check = 2 ** self.nr_wire
        self.fitness_per_chromosome = []
        self.fitness_computer = SortedOutputsFitnessComputer()
        self.FITNESS_WEIGHT = 0.7
        self.NOVELTY_WEIGHT = 0.3

    def compute_fitness_for_population(self, population):
        for chromosome in population.chromosomes:
            self.fitness_per_chromosome.append(self.fitness_computer.get_fitness(chromosome.get_sorting_network()))
        return self.get_novelty_fitness_for_population(population)

    def get_novelty_fitness_for_population(self, population):
        novelty_fitness = []
        for c in population.chromosomes:
            distances = []
            for c2 in population.chromosomes:
                distances.append(self.get_distance_between(c.get_sorting_network().novelty,
                                                           c2.get_sorting_network().novelty))
            novelty_fitness.append(sum(distances)/len(distances))
        total_fitness = [self.fitness_per_chromosome[i] * self.FITNESS_WEIGHT + novelty_fitness[i] * self.NOVELTY_WEIGHT
                         for i in range(len(novelty_fitness))]
        return total_fitness

    def get_distance_between(self, v1, v2):
        v = [i - j for i, j in zip(v1, v2)]
        return numpy.linalg.norm(v)
