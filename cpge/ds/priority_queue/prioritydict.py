class PriorityDict:
    def __init__(self) -> None:
        # self.d = dict(zip(elements, priorities))
        self.d = dict()

    def update(self, element, priority):
        self.d[element] = priority

    def add(self, element, priority):
        self.d[element] = priority

    def take_min(self):
        k_min = None
        for k in self.d:
            if k_min is None or self.d[k] < self.d[k_min]:
                k_min = k
        self.d.pop(k_min)
        return k_min

    def is_empty(self):
        return len(self.d) == 0

    def __contains__(self, element):
        return element in self.d