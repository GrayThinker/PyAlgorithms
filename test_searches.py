import unittest
import searches

class TestSearches(unittest.TestCase):
    def test_binary_search(self):
        self.assertEqual(searches.binary_search(1, [1, 3, 4, 8, 9]), 0)
        self.assertEqual(searches.binary_search(1, [0, 1, 1, 3, 5]), 1)
        self.assertEqual(searches.binary_search(1, [1, 3, 4, 8, 9]), 0)
        self.assertEqual(searches.binary_search(1, [1, 3, 4, 8, 9]), 0)

    def test_jump_search(self):
        self.assertEqual(searches.jump_search(1, [1, 3, 4, 8, 9]), 0)
    
    def test_interpolation_search(self):
        #TODO: Implement
        pass

    def test_exp_search(self):
        #TODO: Implement
        pass

    def test_fib_search(self):
        #TODO: Implement
        pass

if __name__ == "__main__":
    unittest.main()