"""
    Didn't get the solution.

    Need to use a combination of array and hashmap

    difficulty 7/10
"""


class RandomizedSet:

    def __init__(self):
        self.random_set = set()

    def insert(self, val: int) -> bool:
        if val not in self.random_set:
            self.random_set.add(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.random_set:
            self.random_set.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        pass