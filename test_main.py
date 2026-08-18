import sys
import unittest
from unittest.mock import patch

import main


class MainTest(unittest.TestCase):
    @patch("main.run_visualization")
    def test_default_mode_runs_bubble_split_visualization(self, run_visualization) -> None:
        with patch.object(sys, "argv", ["main.py"]):
            main.main()

        run_visualization.assert_called_once_with([5, 1, 4, 2, 8], delay=0.2)

    @patch("main.run_selection_visualization")
    def test_selection_mode_runs_selection_split_visualization(
        self, run_selection_visualization
    ) -> None:
        with patch.object(sys, "argv", ["main.py", "--mode", "selection", "9", "2"]):
            main.main()

        run_selection_visualization.assert_called_once_with([9, 2], delay=0.2)

    @patch("main.run_visualization")
    def test_bubble_split_mode_runs_default_visualization(self, run_visualization) -> None:
        with patch.object(sys, "argv", ["main.py", "--mode", "bubble-split", "3", "1"]):
            main.main()

        run_visualization.assert_called_once_with([3, 1], delay=0.2)

    @patch("main.run_visualization")
    @patch("main.run_selection_visualization")
    def test_invalid_mode_prints_usage_and_does_not_visualize(
        self, run_selection_visualization, run_visualization
    ) -> None:
        with patch.object(sys, "argv", ["main.py", "--mode", "unknown"]):
            with patch("builtins.print") as print_mock:
                with self.assertRaises(SystemExit) as error:
                    main.main()

        self.assertEqual(error.exception.code, 1)
        output = "\n".join(str(call.args[0]) for call in print_mock.call_args_list)
        self.assertIn("Error: Unsupported mode", output)
        self.assertIn("--mode", output)
        run_visualization.assert_not_called()
        run_selection_visualization.assert_not_called()

    @patch("main.run_visualization")
    def test_malformed_integer_keeps_existing_error(self, run_visualization) -> None:
        with patch.object(sys, "argv", ["main.py", "4", "not-an-integer"]):
            with patch("builtins.print") as print_mock:
                with self.assertRaises(SystemExit) as error:
                    main.main()

        self.assertEqual(error.exception.code, 1)
        self.assertEqual(
            [call.args[0] for call in print_mock.call_args_list],
            [
                "Error: All arguments must be integers.",
                "Usage: python3 main.py [num1 num2 ...]",
            ],
        )
        run_visualization.assert_not_called()


if __name__ == "__main__":
    unittest.main()