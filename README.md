# Bubble Sort Demo

[![CI](https://github.com/wayfarer-rus/bubble-sort-demo/actions/workflows/ci.yml/badge.svg)](https://github.com/wayfarer-rus/bubble-sort-demo/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A Python demonstration and side-by-side comparison of sorting algorithms with a terminal user interface (TUI) visualizer.

## Introduction

This project implements three sorting algorithms and shows their progress on the same input. The visualizer compares either Bubble Sort or Selection Sort with Split Sort (Merge Sort), displaying each algorithm's intermediate states side by side in the terminal.

The sorting functions return sorted copies of the input list, so the caller's original list is not modified. The project is intentionally small and is suitable for exploring sorting behavior, algorithm steps, and automated tests.

## Features

- Bubble Sort and Selection Sort implementations with pass-by-pass snapshots.
- Split Sort, a merge-sort implementation, with snapshots after merge steps.
- Side-by-side terminal visualization of Bubble Sort or Selection Sort against Split Sort.
- Automatic alignment of the two algorithms' step histories when they require different numbers of steps.
- A default demonstration input and support for custom integer lists from the command line.
- Input validation for unsupported modes and non-integer values.

## Algorithms

### Bubble Sort

Bubble Sort repeatedly compares adjacent values and swaps them when they are out of order. After each pass, the largest remaining value moves toward the end of the list. The implementation records the list after each pass and stops early when a pass performs no swaps.

### Selection Sort

Selection Sort scans the unsorted portion of the list, finds its minimum value, and places that value at the next position. The implementation records the list after each selection pass.

### Split Sort (Merge Sort)

Split Sort recursively divides the input into smaller sections and merges the sorted sections back together. It records the list after each merge operation. This is the project's merge-sort implementation.

## TUI Visualizer

The visualizer prints a sequence of terminal frames containing:

- The original input list.
- The number of passes for Bubble Sort or Selection Sort and the number of merge steps for Split Sort.
- Numbered, side-by-side frames showing the current state of both algorithms.
- A `Done` status for an algorithm that has finished while the other algorithm continues; the completed algorithm's final state is retained in subsequent aligned frames.
- The final sorted result from both algorithms.

The default command compares Bubble Sort with Split Sort. Selection mode compares Selection Sort with Split Sort. When run through `main.py`, frames are shown with a 0.2-second delay.

## CLI Usage

Run commands from the repository root with Python 3:

```bash
python3 main.py
python3 main.py --mode selection-split 10 3 7 1 4
```

The command syntax is:

```text
python3 main.py [--mode bubble-split|selection-split] [num1 num2 ...]
```

### Modes

| Option | Comparison | Notes |
| --- | --- | --- |
| `--mode bubble-split` | Bubble Sort vs. Split Sort | Default mode |
| `--mode selection-split` | Selection Sort vs. Split Sort | Selects the Selection Sort comparison |

The shorter aliases `bubble` and `selection` are also accepted:

```bash
python3 main.py --mode bubble 8 3 5 1
python3 main.py --mode selection 8 3 5 1
```

If no numbers are supplied, the demo uses the default values `[5, 1, 4, 2, 8]`. The default mode is `bubble-split`, so the following commands use the same mode and input:

```bash
python3 main.py
python3 main.py --mode bubble-split
```

Custom inputs must be space-separated integers:

```bash
python3 main.py --mode bubble-split 9 2 6 1 5
python3 main.py --mode selection-split 10 3 7 1 4
```

Unsupported modes and other unsupported options print an error and usage information, then exit with status 1. If any positional value is not an integer, the command prints an integer-input error and exits with status 1.

## Project Structure

| File | Description |
| --- | --- |
| `main.py` | Parses command-line arguments, selects the comparison mode, and starts the visualizer. |
| `bubble_sort.py` | Bubble Sort and Bubble Sort pass-history functions. |
| `selection_sort.py` | Selection Sort and Selection Sort pass-history functions. |
| `split_sort.py` | Split Sort (Merge Sort) and merge-step history functions. |
| `tui_visualiser.py` | Aligns algorithm histories and renders side-by-side terminal frames. |
| `test_bubble_sort.py` | Tests Bubble Sort behavior and step histories. |
| `test_selection_sort.py` | Tests Selection Sort behavior and step histories. |
| `test_split_sort.py` | Tests Split Sort behavior and merge-step histories. |
| `test_tui_visualiser.py` | Tests history alignment and visualizer frame formatting/output. |
| `test_main.py` | Tests CLI defaults, modes, aliases, and invalid input handling. |
| `weird_count.py` | Separate experimental script that repeatedly runs Bubble Sort while displaying a themed progress counter. |

## Testing

The project uses `pytest` to run its test suite. From the repository root, run:

```bash
pytest
```

The equivalent Python module invocation is:

```bash
python3 -m pytest
```

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
