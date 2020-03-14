import unittest
import sorts

class TestSorts(unittest.TestCase):
    def test_bubble_sort(self):
        self.assertEqual(sorts.bubble_sort([3, 4, 1, 8, 9]), [1, 3, 4, 8, 9])
        self.assertEqual(sorts.bubble_sort([3, -1, 1, 0, 3]), [-1, 0, 1, 3, 3])
        self.assertEqual(sorts.bubble_sort([7]), [7])
        self.assertEqual(sorts.bubble_sort([]), [])


    def test_insertion_sort(self):
        self.assertEqual(sorts.insertion_sort([3, 4, 1, 8, 9]), [1, 3, 4, 8, 9])
        self.assertEqual(sorts.insertion_sort([3, -1, 1, 0, 3]), [-1, 0, 1, 3, 3])
        self.assertEqual(sorts.insertion_sort([7]), [7])
        self.assertEqual(sorts.insertion_sort([]), [])

    def test_selection_sort(self):
        self.assertEqual(sorts.selection_sort([3, 4, 1, 8, 9]), [1, 3, 4, 8, 9])
        self.assertEqual(sorts.selection_sort([3, -1, 1, 0, 3]), [-1, 0, 1, 3, 3])
        self.assertEqual(sorts.selection_sort([7]), [7])
        self.assertEqual(sorts.selection_sort([]), [])

    def test_pigeon_hole_sort(self):
        self.assertEqual(sorts.pigeon_hole_sort([3, 4, 1, 8, 9]), [1, 3, 4, 8, 9])
        self.assertEqual(sorts.pigeon_hole_sort([3, -1, 1, 0, 3]), [-1, 0, 1, 3, 3])
        self.assertEqual(sorts.pigeon_hole_sort([7]), [7])
        self.assertEqual(sorts.pigeon_hole_sort([]), [])

    def test_merge_sort(self):
        self.assertEqual(sorts.merge_sort([3, 4, 1, 8, 9]), [1, 3, 4, 8, 9])
        self.assertEqual(sorts.merge_sort([3, -1, 1, 0, 3]), [-1, 0, 1, 3, 3])
        self.assertEqual(sorts.merge_sort([7]), [7])
        self.assertEqual(sorts.merge_sort([]), [])

    def test_quick_sort(self):
        self.assertEqual(sorts.quick_sort([3, 4, 1, 8, 9]), [1, 3, 4, 8, 9])
        self.assertEqual(sorts.quick_sort([3, -1, 1, 0, 3]), [-1, 0, 1, 3, 3])
        self.assertEqual(sorts.quick_sort([7]), [7])
        self.assertEqual(sorts.quick_sort([]), [])

    def test_bogo_sort(self):
        self.assertEqual(sorts.bogo_sort([3, 4, 1, 8, 9]), [1, 3, 4, 8, 9])
        self.assertEqual(sorts.bogo_sort([3, -1, 1, 0, 3]), [-1, 0, 1, 3, 3])
        self.assertEqual(sorts.bogo_sort([7]), [7])
        self.assertEqual(sorts.bogo_sort([]), [])
        

if __name__ == '__main__':
    unittest.main()