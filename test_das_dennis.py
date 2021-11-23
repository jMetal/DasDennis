import unittest

from das_dennis import DasDennis


class DasDennisTestCases(unittest.TestCase):
    def test_should_constructor_create_a_non_null_object(self):
        das_dennis = DasDennis(4, 3)
        self.assertIsNotNone(das_dennis)

    def test_should_constructor_set_the_valid_parameter(self):
        das_dennis = DasDennis(number_of_partitions=4, dimension=3)
        self.assertEqual(4, das_dennis.number_of_partitions)
        self.assertEqual(3, das_dennis.dimension)

    # Case 1: number of partitions = 12, dimension = 3
    def test_should_get_number_of_points_return_the_correct_value_case_1(self):
        das_dennis = DasDennis(number_of_partitions=12, dimension=3)

        self.assertEquals(91, das_dennis.get_number_of_points())

    # Case 2: number of partitions = 5, dimension = 3
    def test_should_get_number_of_points_return_the_correct_value_case_2(self):
        das_dennis = DasDennis(number_of_partitions=5, dimension=3)

        self.assertEquals(21, das_dennis.get_number_of_points())

    # Case 1: number of partitions = 12, dimension = 3
    def test_should_get_weight_vectors_work_properly_case_1(self):
        """ h: number of partitions, m: dimension"""
        das_dennis = DasDennis(number_of_partitions=12, dimension=3)
        points = das_dennis.get_weight_vectors()

        self.assertEquals(91, len(points))
        self.assertEqual([0.0, 0.0, 1.0], points[0])
        self.assertEqual([1.0, 0.0, 0.0], points[90])
        self.assertEqual([0.75, 0.25, 0.0], points[84])

    # Case 2: number of partitions = 5, dimension = 3
    def test_should_get_weight_vectors_work_properly_case_2(self):
        """ h: number of partitions, m: dimension"""
        das_dennis = DasDennis(number_of_partitions=5, dimension=3)
        points = das_dennis.get_weight_vectors()

        self.assertEquals(21, len(points))
        self.assertEqual([0.0, 0.0, 1.0], points[0])
        self.assertEqual([0.8, 0.2, 0.0], points[19])
        self.assertEqual([1.0, 0.0, 0.0], points[20])
