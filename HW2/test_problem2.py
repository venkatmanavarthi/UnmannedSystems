import unittest
from problem2 import Obstacle, is_valid


class TestProblem2(unittest.TestCase):

    def setUp(self) -> None:
        self.obs = Obstacle(4, 4, 0.25)
        self.obs_pos = [(1, 1), (4, 4), (3, 4), (5, 0), (5, 1),
               (0, 7), (1, 7), (2, 7), (3, 7)]
        self.obs_list = [Obstacle(each_ob[0], each_ob[1], 0.25)
                for each_ob in self.obs_pos]
        

    def test_is_inside(self):
        self.assertEqual(self.obs.is_inside(2, 2), False)
        self.assertEqual(self.obs.is_inside(4, 4), True)

    def test_is_valid(self):
        self.assertEqual(is_valid(self.obs_list, 0, 0, 10, 10, 2, 2, 0.25), True)
        self.assertEqual(is_valid(self.obs_list, 0, 0, 10, 10, 1.16, 1, 0.25), False)

if __name__ == "__main__":
    unittest.main()
