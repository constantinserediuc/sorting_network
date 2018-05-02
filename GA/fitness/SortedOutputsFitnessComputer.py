from GA.Utils import Info


class SortedOutputsFitnessComputer(object):
    def __init__(self):
        self.nr_wire = Info().NR_WIRES
        self.seq_to_sort = []
        self.max_sequence_to_check = 2 ** self.nr_wire

    def set_seq_to_sort(self):
        for i in range(0, self.nr_wire + 1):
            bits = "0" * i + "1" * (self.nr_wire - i)
            self.seq_to_sort.append(int(bits, 2))

    def get_fitness(self, sorting_network):
        fails = 0
        self.set_seq_to_sort()
        for i in range(1, self.max_sequence_to_check):
            if sorting_network.sort_binary_sequence(i) not in self.seq_to_sort:
                fails += 1

        return 1 - (fails / self.max_sequence_to_check)
