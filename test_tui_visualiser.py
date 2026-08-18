import unittest
from unittest.mock import patch
from tui_visualiser import (
    align_algorithm_steps,
    format_side_by_side_frame,
    run_selection_visualization,
    run_visualization,
)


class TuiVisualiserTest(unittest.TestCase):
    def test_align_algorithm_steps_equal_lengths(self) -> None:
        steps_a = [[2, 1], [1, 2]]
        steps_b = [[1, 2], [1, 2]]
        aligned = align_algorithm_steps(steps_a, steps_b)
        self.assertEqual(len(aligned), 2)
        self.assertFalse(aligned[0]["done_a"])
        self.assertFalse(aligned[0]["done_b"])
        # At index 1 (the final step of both), neither has exceeded its length yet,
        # so done is False until index >= len.
        self.assertFalse(aligned[1]["done_a"])
        self.assertFalse(aligned[1]["done_b"])

    def test_align_algorithm_steps_different_lengths(self) -> None:
        steps_a = [[2, 1, 3], [1, 2, 3]]
        steps_b = [[2, 3, 1], [2, 1, 3], [1, 2, 3]]
        aligned = align_algorithm_steps(steps_a, steps_b)
        self.assertEqual(len(aligned), 3)
        # At index 2, side A (len 2) has finished (index 2 >= 2), so done_a is True.
        self.assertTrue(aligned[2]["done_a"])
        self.assertFalse(aligned[2]["done_b"])
        self.assertEqual(aligned[2]["state_a"], [1, 2, 3])

    def test_align_algorithm_steps_empty(self) -> None:
        self.assertEqual(align_algorithm_steps([], []), [])

    def test_align_algorithm_steps_one_sided_empty(self) -> None:
        steps = [[3, 1], [1, 3]]
        expected_non_empty_side = [
            {
                "state_a": [],
                "state_b": [3, 1],
                "pass_a": 0,
                "pass_b": 1,
                "done_a": True,
                "done_b": False,
            },
            {
                "state_a": [],
                "state_b": [1, 3],
                "pass_a": 0,
                "pass_b": 2,
                "done_a": True,
                "done_b": False,
            },
        ]
        self.assertEqual(align_algorithm_steps([], steps), expected_non_empty_side)

        expected_empty_side = [
            {
                "state_a": [3, 1],
                "state_b": [],
                "pass_a": 1,
                "pass_b": 0,
                "done_a": False,
                "done_b": True,
            },
            {
                "state_a": [1, 3],
                "state_b": [],
                "pass_a": 2,
                "pass_b": 0,
                "done_a": False,
                "done_b": True,
            },
        ]
        self.assertEqual(align_algorithm_steps(steps, []), expected_empty_side)

    def test_format_side_by_side_frame(self) -> None:
        formatted = format_side_by_side_frame(
            "Bubble Sort",
            state_a=[1, 2, 4, 5, 8],
            pass_a=1,
            done_a=False,
            name_b="Split Sort",
            state_b=[1, 5, 4, 2, 8],
            pass_b=1,
            done_b=False,
            unit_a="Pass",
            unit_b="Step",
        )
        self.assertIn("Bubble Sort", formatted)
        self.assertIn("Split Sort", formatted)
        self.assertIn("[1, 2, 4, 5, 8]", formatted)
        self.assertIn("[1, 5, 4, 2, 8]", formatted)

    @patch("tui_visualiser.time.sleep")
    def test_run_visualization_renders_completion_and_results(self, sleep) -> None:
        with patch("builtins.print") as print_mock:
            run_visualization([5, 1, 4, 2, 8], delay=0)

        output = "\n".join(str(call.args[0]) for call in print_mock.call_args_list)
        self.assertIn("Bubble Sort passes: 3 | Split Sort merge steps: 4", output)
        self.assertIn("[4/4] Bubble Sort (Done)", output)
        self.assertIn("Split Sort (Step 4)", output)
        self.assertIn("Bubble Sorted: [1, 2, 4, 5, 8]", output)
        self.assertIn("Split Sorted:  [1, 2, 4, 5, 8]", output)
        sleep.assert_not_called()

    @patch("tui_visualiser.time.sleep")
    def test_run_selection_visualization_renders_completion_and_results(self, sleep) -> None:
        with patch("builtins.print") as print_mock:
            run_selection_visualization([5, 1, 4, 2, 8], delay=0)

        output = "\n".join(str(call.args[0]) for call in print_mock.call_args_list)
        self.assertIn("Selection Sort passes: 5 | Split Sort merge steps: 4", output)
        self.assertIn("[5/5] Selection Sort (Pass 5)", output)
        self.assertIn("Split Sort (Done)", output)
        self.assertIn("Selection Sorted: [1, 2, 4, 5, 8]", output)
        self.assertIn("Split Sorted:  [1, 2, 4, 5, 8]", output)
        sleep.assert_not_called()


if __name__ == "__main__":
    unittest.main()
