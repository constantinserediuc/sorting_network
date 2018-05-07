from SortingNetwork.SortingNetwork import SortingNetwork
from GA.Utils import Info


class GreenFilter:
    @staticmethod
    def get_filter(nr_wires):
        network = SortingNetwork()
        for i in range(0, nr_wires, 2):
            network.add_comparator([i, i + 1])
        for k in range(2):
            for i in range(k, nr_wires - 2, 4):
                network.add_comparator([i, i + 2])
        for k in range(4):
            for i in range(k, nr_wires - 4, 8):
                network.add_comparator([i, i + 4])
        for k in range(8):
            for i in range(k, nr_wires - 8, 16):
                network.add_comparator([i, i + 8])
        for k in range(16):
            for i in range(k, nr_wires - 16, 32):
                network.add_comparator([i, i + 16])
        return network

    @staticmethod
    def get_nr_comparators_for(nr_wires):
        """ TODO
        de calculat direct
        """
        return len([i for i in range(0, nr_wires, 2)]) + \
               len([i for k in range(2) for i in range(k, nr_wires - 2, 4)]) + \
               len([i for k in range(4) for i in range(k, nr_wires - 4, 8)]) + \
               len([i for k in range(8) for i in range(k, nr_wires - 8, 16)]) + \
               len([i for k in range(16) for i in range(k, nr_wires - 16, 32)])
