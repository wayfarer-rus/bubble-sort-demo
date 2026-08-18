import sys
import time
from bubble_sort import bubble_sort, bubble_sort_steps
from selection_sort import selection_sort, selection_sort_steps
from split_sort import split_sort, split_sort_steps


def align_algorithm_steps(
    steps_a: list[list[int]], steps_b: list[list[int]]
) -> list[dict]:
    """Align two algorithm step histories into parallel frames, padding shorter sequences."""
    if not steps_a and not steps_b:
        return []

    len_a = len(steps_a)
    len_b = len(steps_b)
    max_len = max(len_a, len_b)
    aligned = []

    for i in range(max_len):
        idx_a = min(i, len_a - 1) if len_a > 0 else 0
        idx_b = min(i, len_b - 1) if len_b > 0 else 0

        state_a = steps_a[idx_a] if len_a > 0 else []
        state_b = steps_b[idx_b] if len_b > 0 else []

        pass_a = min(i + 1, len_a) if len_a > 0 else 0
        pass_b = min(i + 1, len_b) if len_b > 0 else 0

        done_a = (i >= len_a) if len_a > 0 else True
        done_b = (i >= len_b) if len_b > 0 else True

        aligned.append({
            "state_a": state_a,
            "state_b": state_b,
            "pass_a": pass_a,
            "pass_b": pass_b,
            "done_a": done_a,
            "done_b": done_b,
        })

    return aligned


def format_side_by_side_frame(
    name_a: str,
    state_a: list[int],
    pass_a: int,
    done_a: bool,
    name_b: str,
    state_b: list[int],
    pass_b: int,
    done_b: bool,
    unit_a: str = "Pass",
    unit_b: str = "Step",
) -> str:
    """Format a single side-by-side frame comparing two algorithm states."""
    status_a = " (Done)" if done_a else f" ({unit_a} {pass_a})"
    status_b = " (Done)" if done_b else f" ({unit_b} {pass_b})"

    str_a = f"{name_a}{status_a}: {state_a}"
    str_b = f"{name_b}{status_b}: {state_b}"

    return f"{str_a:<45} | {str_b}"


def _run_visualization(
    name_a: str,
    sort_func_a,
    steps_func_a,
    values: list[int],
    delay: float = 0.3,
    unit_a: str = "Pass",
) -> None:
    if not values:
        print("Empty list provided.")
        return

    print("==================================================")
    print("      SIDE-BY-SIDE SORTING ALGORITHM TUI          ")
    print("==================================================")
    print(f"Original list: {values}\n")

    steps_a = steps_func_a(values)
    s_steps = split_sort_steps(values)
    aligned = align_algorithm_steps(steps_a, s_steps)

    print(f"{name_a} passes: {len(steps_a)} | Split Sort merge steps: {len(s_steps)}")
    print("--------------------------------------------------\n")

    short_name_a = name_a.replace(" Sort", "")

    for idx, frame in enumerate(aligned):
        line = format_side_by_side_frame(
            name_a,
            frame["state_a"],
            frame["pass_a"],
            frame["done_a"],
            "Split Sort",
            frame["state_b"],
            frame["pass_b"],
            frame["done_b"],
            unit_a=unit_a,
            unit_b="Step",
        )
        print(f"[{idx + 1}/{len(aligned)}] {line}")
        if delay > 0:
            time.sleep(delay)

    print("\n--------------------------------------------------")
    print("Visualization finished!")
    print(f"{short_name_a} Sorted: {sort_func_a(values)}")
    print(f"Split Sorted:  {split_sort(values)}")


def run_visualization(values: list[int], delay: float = 0.3) -> None:
    """Run side-by-side TUI visualization comparing bubble sort and split sort steps."""
    _run_visualization("Bubble Sort", bubble_sort, bubble_sort_steps, values, delay, "Pass")


def run_selection_visualization(values: list[int], delay: float = 0.3) -> None:
    """Run side-by-side TUI visualization comparing selection and split sort."""
    _run_visualization("Selection Sort", selection_sort, selection_sort_steps, values, delay, "Pass")
