import copy
import random

from GA.Population import Population
from GA.fitness.SortedOutputsWithNoveltyFitnessComputer import SortedOutputsWithNoveltyFitnessComputer


class RouletteWheelSelector(object):
    def __init__(self, population, fitness_computer):
        self.population = population
        # self.fitness_computer = fitness_computer
        self.fitness_computer = SortedOutputsWithNoveltyFitnessComputer()
        self.fitness_per_chromosome = []
        self.relative_fitness = []
        self.cumulative_fitness = []

    def compute_fitness_per_chromosome(self):
        self.fitness_per_chromosome = copy.deepcopy(self.fitness_computer.compute_fitness_for_population(self.population))

    def compute_relative_fitness(self):
        total_fitness = sum(self.fitness_per_chromosome)
        for chromosome_fitness in self.fitness_per_chromosome:
            self.relative_fitness.append(chromosome_fitness / total_fitness)

    def compute_cumulative_fitness(self):
        self.cumulative_fitness.append(self.relative_fitness[0])
        for i in range(1, self.population.pop_size):
            self.cumulative_fitness.append(self.cumulative_fitness[i - 1] + self.relative_fitness[i])

    def select(self):
        self.compute_fitness_per_chromosome()
        self.compute_relative_fitness()
        self.compute_cumulative_fitness()
        return Population(self.select_new_population_chromosomes())

    def select_new_population_chromosomes(self):
        chromosomes = []
        for i in range(self.population.pop_size):
            p = random.random()
            if p < self.cumulative_fitness[0]:
                chromosomes.append(copy.deepcopy(self.population.chromosomes[0]))
            else:
                for j in range(self.population.pop_size):
                    if self.cumulative_fitness[j] <= p < self.cumulative_fitness[j + 1]:
                        chromosomes.append(copy.deepcopy(self.population.chromosomes[j + 1]))
        # finesses = [self.fitness_computer.get_fitness(chromosome.get_sorting_network()) for chromosome in chromosomes]
        # print('fitness inainte', self.sum, sum(finesses))
        return chromosomes
