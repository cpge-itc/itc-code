class PriorityList:
    def __init__(self, elements, priorities) -> None:
        self.d = dict(zip(elements, priorities))
    
    def update(self, element, priority):
        self.d[element] = priority

    def add(self, element, priority):
        self.d[element] = priority

    def take_min(self):
        k_min = None
        for k in self.d:
            if k_min is None or self.d[k] < self.d[k_min]:
                k_min = k
        return k_min, self.d.pop(k_min)
