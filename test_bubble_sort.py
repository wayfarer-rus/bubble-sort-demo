import unittest

from bubble_sort import bubble_sort, bubble_sort_steps


class BubbleSortTest(unittest.TestCase):
    def test_sorts_unsorted_values(self) -> None:
        self.assertEqual(bubble_sort([5, 1, 4, 2, 8]), [1, 2, 4, 5, 8])

    def test_keeps_already_sorted_values(self) -> None:
        self.assertEqual(bubble_sort([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_sorts_duplicate_values(self) -> None:
        self.assertEqual(bubble_sort([3, 1, 2, 3, 1]), [1, 1, 2, 3, 3])

    def test_sorts_negative_values(self) -> None:
        self.assertEqual(bubble_sort([0, -3, 2, -1]), [-3, -1, 0, 2])

    def test_sorts_empty_list(self) -> None:
        self.assertEqual(bubble_sort([]), [])

    def test_sorts_single_element_list(self) -> None:
        self.assertEqual(bubble_sort([7]), [7])

    def test_does_not_mutate_input(self) -> None:
        values = [4, 2, 3, 1]

        result = bubble_sort(values)

        self.assertEqual(result, [1, 2, 3, 4])
        self.assertEqual(values, [4, 2, 3, 1])

    def test_steps_show_each_pass(self) -> None:
        self.assertEqual(
            bubble_sort_steps([5, 1, 4, 2, 8]),
            [
                [1, 4, 2, 5, 8],
                [1, 2, 4, 5, 8],
                [1, 2, 4, 5, 8],
            ],
        )


if __name__ == "__main__":
    unittest.main()