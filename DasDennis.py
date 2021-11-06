from typing import List

import numpy as np


class DasDennis():
    def __init__(self, h, m):
        self.h = h
        self.m = m

    def __get_first_level(self, h: int) -> List:
        return [_ for _ in np.linspace(0,1,h+1)]

    def __get_generic_level(self, first_level, previous_level):
        next_level = []
        for ind0, i in enumerate(previous_level):
            for ind1, j in enumerate(i[1]):
                values = [first_level[v] for v in range(len(first_level) - ind1 - ind0)]
                next_level.append([i[0] + [i[1][ind1]], values])

        return next_level

    def __get_last_level(self, previous_level):
        last_level = []
        for ind0, i in enumerate(previous_level):
            for ind1, j in enumerate(i[1]):
                last_level.append([i[0] + [j, 1.0 - j - sum(i[0])]])

        return last_level

    def get_weight_vectors(self):
        first_level = self.__get_first_level(self.h)
        previous_level = [[[], first_level]]
        for i in range(1, m - 1):
            next_level = self.__get_generic_level(first_level, previous_level)
            previous_level = next_level

        return self.__get_last_level(previous_level)


H = 12
m = 3

weight_vectors = DasDennis(H,m).get_weight_vectors()

print("Number of points: " + str(len(weight_vectors)))
for i in weight_vectors:
    print(i)
