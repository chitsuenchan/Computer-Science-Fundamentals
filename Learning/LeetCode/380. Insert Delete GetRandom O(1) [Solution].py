

import random

class RandomizedSet:

    def __init__(self):
        self.h = {}
        self.lst = []

    def insert(self, val: int) -> bool:
        if val in self.h:
            return False

        self.h[val] = len(self.lst)
        self.lst.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.h:
            return False

        last_element = self.lst[-1]
        val_idx = self.h[val]

        # Swapping last element with element to be removed
        self.lst[val_idx] = last_element
        self.h[last_element] = val_idx

        # Removing the elements
        self.lst.pop()
        self.h.pop(val)

        return True

    def getRandom(self) -> int:
        return random.choice(self.lst)