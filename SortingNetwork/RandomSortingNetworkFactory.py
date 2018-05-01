import random

from SortingNetwork.SortingNetwork import SortingNetwork


class RandomSortingNetworkFactory:
    @staticmethod
    def get_sorting_network_with(nr_wires, nr_comparators):
        """ ???
        nu este mai ok sa generz y = randint(0,nr_wires-1), fiindca asa ar fi 'mai random'
        """
        network = SortingNetwork()
        while len(network.get_comparators()) != nr_comparators:
            x = random.randint(0, nr_wires - 2)
            y = random.randint(x + 1, nr_wires - 1)
            if network.can_comparator_be_added([x, y]):
                network.add_comparator([x, y])
        return network

    @staticmethod
    def get_random_comparator(nr_wires):
        x = random.randint(0, nr_wires - 2)
        y = random.randint(x + 1, nr_wires - 1)
        return [x, y]
