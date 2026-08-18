import unittest

from selection_sort import selection_sort, selection_sort_steps


class SelectionSortTest(unittest.TestCase):
    def test_sorts_unsorted_values(self) -> None:
        self.assertEqual(selection_sort([5, 1, 4, 2, 8]), [1, 2, 4, 5, 8])

    def test_keeps_already_sorted_values(self) -> None:
        self.assertEqual(selection_sort([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_sorts_duplicate_values(self) -> None:
        self.assertEqual(selection_sort([3, 1, 2, 3, 1]), [1, 1, 2, 3, 3])

    def test_sorts_negative_values(self) -> None:
        self.assertEqual(selection_sort([0, -3, 2, -1]), [-3, -1, 0, 2])

    def test_sorts_empty_list(self) -> None:
        self.assertEqual(selection_sort([]), [])

    def test_sorts_single_element_list(self) -> None:
        self.assertEqual(selection_sort([7]), [7])

    def test_does_not_mutate_input(self) -> None:
        values = [4, 2, 3, 1]

        result = selection_sort(values)

        self.assertEqual(result, [1, 2, 3, 4])
        self.assertEqual(values, [4, 2, 3, 1])

    def test_steps_show_each_selection_pass(self) -> None:
        self.assertEqual(
            selection_sort_steps([5, 1, 4, 2, 8]),
            [
                [1, 5, 4, 2, 8],
                [1, 2, 4, 5, 8],
                [1, 2, 4, 5, 8],
                [1, 2, 4, 5, 8],
                [1, 2, 4, 5, 8],
            ],
        )

    def test_steps_empty_list(self) -> None:
        self.assertEqual(selection_sort_steps([]), [])

    def test_steps_single_element_list(self) -> None:
        self.assertEqual(selection_sort_steps([7]), [[7]])

    def test_steps_do_not_mutate_input(self) -> None:
        values = [3, 2, 1]

        selection_sort_steps(values)

        self.assertEqual(values, [3, 2, 1])


if __name__ == "__main__":
    unittest.main()