from typing import List

import numpy as np


class DasDennis:
    def __init__(self, h, m):
        self.h = h
        self.m = m

    def __get_first_level(self, h: int) -> List:
        return [_ for _ in np.linspace(0, 1, h + 1)]

    def __get_generic_level(self, first_level, previous_level):
        next_level = []
        for ind0, i in enumerate(previous_level):
            for ind1, j in enumerate(i[1]):
                values = [first_level[_] for _ in range(len(first_level) - ind1 - ind0)]
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

        last_level = self.__get_last_level(previous_level)
        result = [last_level[i][0] for i in range(len(last_level))]
        return result

    def save_to_file(self, file_name, weight_vectors, separator=" "):
        with open(file_name, 'w+') as output_file:
            for vector in weight_vectors:
                output_string = ""
                for value in vector:
                    output_string += str(value) + separator
                output_string = output_string[:-1]
                output_string += "\n"
                output_file.write(output_string)

    def __factorial(self, n:int):
        if (n == 0 or n == 1):
            return 1
        else: 
            return n * self.__factorial(n-1)

    def __binomial_coefficient(self, n, k):
        return self.__factorial(n) / (self.__factorial(k) * self.__factorial(n - k))

    def get_number_of_points(self):
        return int(self.__binomial_coefficient(self.h + self.m - 1, self.m - 1))



if __name__ == "__main__":
    H = 12
    m = 3

    das_dennis_weight_generator = DasDennis(H, m)

    weight_vectors = das_dennis_weight_generator.get_weight_vectors()

    print("Number of vectors: " + str(len(weight_vectors)))
    print("Number of vectors: " + str(das_dennis_weight_generator.get_number_of_points()))
    for i in weight_vectors:
        print(i)

    das_dennis_weight_generator.save_to_file("W" + str(m) + "D_" + str(len(weight_vectors)) + ".dat", weight_vectors)
