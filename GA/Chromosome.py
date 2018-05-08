class Chromosome(object):
    def __init__(self, sorting_network):
        self.sorting_network = sorting_network
        self.best_so_far = {'fitness': 0, 'chromosome': None}

    def get_sorting_network(self):
        return self.sorting_network
