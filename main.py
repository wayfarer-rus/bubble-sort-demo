import sys
from tui_visualiser import run_selection_visualization, run_visualization


DEFAULT_VALUES = [5, 1, 4, 2, 8]
DEFAULT_MODE = "bubble-split"
MODES = {
    "bubble": "bubble-split",
    "bubble-split": "bubble-split",
    "selection": "selection-split",
    "selection-split": "selection-split",
}


def _print_mode_error(mode: str) -> None:
    print(f"Error: Unsupported mode '{mode}'.")
    print("Usage: python3 main.py [--mode bubble-split|selection-split] [num1 num2 ...]")


def _parse_args(args: list[str]) -> tuple[str, list[int]]:
    mode = DEFAULT_MODE
    value_args = []
    index = 0

    while index < len(args):
        arg = args[index]
        if arg == "--mode":
            if index + 1 >= len(args):
                _print_mode_error("")
                sys.exit(1)
            mode = MODES.get(args[index + 1], "")
            if not mode:
                _print_mode_error(args[index + 1])
                sys.exit(1)
            index += 2
            continue
        if arg.startswith("--"):
            _print_mode_error(arg)
            sys.exit(1)
        value_args.append(arg)
        index += 1

    if not value_args:
        return mode, DEFAULT_VALUES.copy()

    try:
        values = [int(arg) for arg in value_args]
    except ValueError:
        print("Error: All arguments must be integers.")
        print("Usage: python3 main.py [num1 num2 ...]")
        sys.exit(1)

    return mode, values


def main() -> None:
    mode, values = _parse_args(sys.argv[1:])

    if mode == "selection-split":
        run_selection_visualization(values, delay=0.2)
    else:
        run_visualization(values, delay=0.2)


if __name__ == "__main__":
    main()
