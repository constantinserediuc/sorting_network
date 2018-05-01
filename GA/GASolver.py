from GA.fitness.SortedOutputsFitnessComputer import SortedOutputsFitnessComputer
from GA.operators.crossover_operators.OnePointCrossoverOperator import *
from GA.operators.mutators.SimpleMutator import *
from GA.operators.selectors.RouletteWheelSelector import RouletteWheelSelector


class GASolver:
    def __init__(self, pop=100, iterations=500):
        self.POP_SIZE = pop
        self.GENERATIONS = iterations
        self.NR_WIRES = Info.NR_WIRES
        self.q = 2
        self.C = 0

    def fitness(self, state):
        pass

    def get_best_solution_from(self, population):
        fitness_computer = SortedOutputsFitnessComputer()
        fitness_per_chromosome = []
        for chromosome in self.population.chromosomes:
            fitness_per_chromosome.append(fitness_computer.get_fitness(chromosome.get_sorting_network()))
        max_fitness = max(fitness_per_chromosome)
        return {"chromosome": fitness_per_chromosome.index(max_fitness), "fitness": max_fitness}

    def get_worst_solution_from(self, population):
        pass

    def solve(self):
        population = Population.get_random_population_with_Green_filter(self.POP_SIZE, self.NR_WIRES)
        global_best_solution = {'fitness': 0, 'chromosome': None}
        for generation in range(self.GENERATIONS):
            selector = RouletteWheelSelector(population, SortedOutputsFitnessComputer())
            descendant_population = selector.select()
            # best_solution_from_population = self.get_best_solution_from(descendant_population)

            crossover_operator = OnePointCrossOverOperator(copy.deepcopy(descendant_population))
            population_after_crossover = crossover_operator.crossover()

            mutator = SimpleMutator(population_after_crossover)
            population_after_mutation = mutator.mutate()

            # hybridator = HillClimbingHybrid()
            #
            # population_after_hybridation = hybridator.apply_hill_climbing(population_after_mutation)

            # population_c = copy.deepcopy(population_after_mutation.chromosomes[:-1])
            # population_c.append(best_solution_from_population['chromosome'])
            # population = Population(copy.deepcopy(population_c))

            best_solution_from_population = self.get_best_solution_from(population_after_mutation)

            # if best_solution_from_population['fitness'] > global_best_solution['fitness']:
            #     global_best_solution = copy.deepcopy(best_solution_from_population)
            #
        print(best_solution_from_population)
