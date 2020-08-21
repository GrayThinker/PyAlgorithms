from src.sort import *
import unittest
"""
TODO:
Even number of elements
odd number of elements
empty list
single elements
only letters
only integers (+ve)
only floats (+ve)
mix of floats and integers (+ve)
mix of floats and letters (+ve)
mix of floats, letters, and integers (+ve)

only integers (+ve)
only floats (+ve)
mix of floats and integers (+ve)
mix of floats and letters (+ve)
mix of floats, letters, and integers (+ve)
symbols
"""
class TestSorts(unittest.TestCase):
    def test_bubble_sort(self):
        self.assertEqual(bubble_sort([3, 4, 1, 8, 9]), [1, 3, 4, 8, 9])
        self.assertEqual(bubble_sort([3, -1, 1, 0, 3]), [-1, 0, 1, 3, 3])
        self.assertEqual(bubble_sort([7]), [7])
        self.assertEqual(bubble_sort([]), [])


    def test_insertion_sort(self):
        self.assertEqual(insertion_sort([3, 4, 1, 8, 9]), [1, 3, 4, 8, 9])
        self.assertEqual(insertion_sort([3, -1, 1, 0, 3]), [-1, 0, 1, 3, 3])
        self.assertEqual(insertion_sort([7]), [7])
        self.assertEqual(insertion_sort([]), [])

    def test_selection_sort(self):
        self.assertEqual(selection_sort([3, 4, 1, 8, 9]), [1, 3, 4, 8, 9])
        self.assertEqual(selection_sort([3, -1, 1, 0, 3]), [-1, 0, 1, 3, 3])
        self.assertEqual(selection_sort([7]), [7])
        self.assertEqual(selection_sort([]), [])

    def test_pigeon_hole_sort(self):
        self.assertEqual(pigeon_hole_sort([3, 4, 1, 8, 9]), [1, 3, 4, 8, 9])
        self.assertEqual(pigeon_hole_sort([3, -1, 1, 0, 3]), [-1, 0, 1, 3, 3])
        self.assertEqual(pigeon_hole_sort([7]), [7])
        self.assertEqual(pigeon_hole_sort([]), [])

    def test_merge_sort(self):
        self.assertEqual(merge_sort([3, 4, 1, 8, 9]), [1, 3, 4, 8, 9])
        self.assertEqual(merge_sort([3, -1, 1, 0, 3]), [-1, 0, 1, 3, 3])
        self.assertEqual(merge_sort([7]), [7])
        self.assertEqual(merge_sort([]), [])

    def test_quick_sort(self):
        self.assertEqual(quick_sort([3, 4, 1, 8, 9]), [1, 3, 4, 8, 9])
        self.assertEqual(quick_sort([3, -1, 1, 0, 3]), [-1, 0, 1, 3, 3])
        self.assertEqual(quick_sort([7]), [7])
        self.assertEqual(quick_sort([]), [])

    def test_bogo_sort(self):
        self.assertEqual(bogo_sort([3, 4, 1, 8, 9]), [1, 3, 4, 8, 9])
        self.assertEqual(bogo_sort([3, -1, 1, 0, 3]), [-1, 0, 1, 3, 3])
        self.assertEqual(bogo_sort([7]), [7])
        self.assertEqual(bogo_sort([]), [])
        
    def test_cocktail_sort(self):
        self.assertEqual(cocktail_sort([3, 4, 1, 8, 9]), [1, 3, 4, 8, 9])
        self.assertEqual(cocktail_sort([3, -1, 1, 0, 3]), [-1, 0, 1, 3, 3])
        self.assertEqual(cocktail_sort([7]), [7])
        self.assertEqual(cocktail_sort([]), [])

if __name__ == '__main__':
    unittest.main()