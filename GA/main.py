from SortingNetwork.SVGConvertor import svg
from GA.GASolver import *

solver = GASolver()
best = solver.solve()
svg(best['chromosome'].get_sorting_network())
print(best['fitness'])
