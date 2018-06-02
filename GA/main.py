from SortingNetwork.SVGConvertor import svg
from GA.GASolver import *
from GA.fitness.SortedOutputsFitnessComputer import SortedOutputsFitnessComputer

solver = GASolver()
best = solver.solve()
# green_filter = GreenFilter.get_filter(Info.NR_WIRES)
# partial_sorting_network = best['chromosome'].get_sorting_network()
# sorting_network_comparators = green_filter.get_comparators() + partial_sorting_network.get_comparators()
# sorting_network = SortingNetwork()
# sorting_network.set_comparators(sorting_network_comparators)
svg(best['chromosome'].get_sorting_network())
fitness_computer = SortedOutputsFitnessComputer()
print(fitness_computer.get_fitness_using_green_filter(best['chromosome'].get_sorting_network()))
