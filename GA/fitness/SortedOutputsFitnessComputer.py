from GA.Utils import Info
from SortingNetwork.GreenFilter import *


class SortedOutputsFitnessComputer(object):
    def __init__(self):
        self.nr_wire = Info.NR_WIRES
        self.sorted_seq = []
        self.max_sequence_to_check = 2 ** self.nr_wire

    def set_seq_to_sort(self):
        for i in range(0, self.nr_wire + 1):
            bits = "0" * i + "1" * (self.nr_wire - i)
            self.sorted_seq.append(int(bits, 2))

    def get_fitness(self, sorting_network):
        fails = 0
        self.set_seq_to_sort()
        for i in range(1, self.max_sequence_to_check):
            if sorting_network.sort_binary_sequence(i) not in self.sorted_seq:
                fails += 1

        return 1 - (fails / self.max_sequence_to_check)

    def get_fitness_using_green_filter(self, sorting_network):
        fails = 0
        self.set_seq_to_sort()
        for i in Info.seq_to_check_after_using_green_filter:
            if sorting_network.sort_binary_sequence(i) not in self.sorted_seq:
                fails += 1

        return 1 - (fails / len(Info.seq_to_check_after_using_green_filter))

    def get_unsorted_binary_seq(self):
        unsorted = []
        sorting_network = GreenFilter().get_filter(Info.NR_WIRES)
        self.set_seq_to_sort()
        for i in range(1, self.max_sequence_to_check):
            if sorting_network.sort_binary_sequence(i) not in self.sorted_seq:
                unsorted.append(i)
        return unsorted
