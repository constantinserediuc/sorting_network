class SortingNetwork:
    def __init__(self):
        self.comparators = []
        self.nr_wires = 0

    def can_comparator_be_added(self, comparator):
        if len(comparator) != 2 or comparator[0] >= comparator[1]:
            return False
        if len(self.comparators) == 0:
            return True
        last_comparator = self.comparators[-1]
        if comparator[0] == last_comparator[0] and comparator[1] == last_comparator[1]:
            return False
        return True

    def add_comparator(self, comparator):
        """ a comparator [x,y] must have:
            x<y and
            [x,y] != self.comparators[-1]
        """
        self.comparators.append(comparator)

    def get_comparators(self):
        return self.comparators

    def get_nr_comparators(self):
        return len(self.comparators)

    def set_comparators(self, comparators):
        self.comparators = comparators

    def set_comparator(self, index, comparator):
        self.comparators[index] = comparator

    def sort_binary_sequence(self, sequence):
        result = sequence
        for c in self.comparators:
            if (result >> c[0]) & 1 < (result >> c[1]) & 1:
                result = (result - 2 ** c[1]) | 2 ** c[0]
        return result
