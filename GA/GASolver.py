from GA.fitness.SortedOutputsFitnessComputer import SortedOutputsFitnessComputer
from GA.operators.crossover_operators.OnePointCrossoverOperator import *
from GA.operators.mutators.SimpleMutator import *
from GA.operators.selectors.RouletteWheelSelector import RouletteWheelSelector
from GA.operators.crossover_operators.VelocityCrossover import *


class GASolver:
    def __init__(self, pop=100, iterations=500):
        self.POP_SIZE = pop
        self.GENERATIONS = iterations
        self.NR_WIRES = Info.NR_WIRES
        self.NR_COMPARATORS = Info.NR_COMPARATORS
        Info.seq_to_check_after_using_green_filter = (SortedOutputsFitnessComputer()).get_unsorted_binary_seq()
        self.global_best_solution = {'fitness': 0, 'chromosome': None}

    def update_best(self, population):
        fitness_computer = SortedOutputsFitnessComputer()
        fitness_per_chromosome = []
        for chromosome in population.chromosomes:
            fitness = fitness_computer.get_fitness_using_green_filter(chromosome.get_sorting_network())
            if chromosome.best_so_far["fitness"] < fitness:
                chromosome.best_so_far["fitness"] = fitness
                chromosome.best_so_far["chromosome"] = chromosome.get_sorting_network()
            fitness_per_chromosome.append(fitness)
        max_fitness = max(fitness_per_chromosome)
        if max_fitness > self.global_best_solution['fitness']:
            self.global_best_solution = {
                "chromosome": copy.deepcopy(population.chromosomes[fitness_per_chromosome.index(max_fitness)]),
                "fitness": max_fitness}

    def solve(self):
        population = Population.get_random_population_with_Green_filter(self.POP_SIZE, self.NR_WIRES,
                                                                        self.NR_COMPARATORS)

        for generation in range(self.GENERATIONS):
            selector = RouletteWheelSelector(population, SortedOutputsFitnessComputer())
            descendant_population = selector.select()
            self.update_best(descendant_population)
            # best_solution_from_population = self.get_best_solution_from(descendant_population)

            # crossover_operator = OnePointCrossOverOperator(copy.deepcopy(descendant_population))
            crossover_operator = VelocityCrossover(copy.deepcopy(descendant_population),
                                                   self.global_best_solution["chromosome"])
            population_after_crossover = crossover_operator.crossover()

            mutator = SimpleMutator(population_after_crossover)
            population_after_mutation = mutator.mutate()
            # hybridator = HillClimbingHybrid()
            #
            # population_after_hybridation = hybridator.apply_hill_climbing(population_after_mutation)

            # population_c = copy.deepcopy(population_after_mutation.chromosomes[:-1])
            # population_c.append(best_solution_from_population['chromosome'])
            population = copy.deepcopy(population_after_mutation)

        return self.global_best_solution
