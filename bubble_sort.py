def bubble_sort(values: list[int]) -> list[int]:
    """Return a sorted copy of values using bubble sort."""
    sorted_values = values.copy()

    for pass_index in range(len(sorted_values)):
        swapped = False

        for index in range(0, len(sorted_values) - pass_index - 1):
            if sorted_values[index] > sorted_values[index + 1]:
                sorted_values[index], sorted_values[index + 1] = (
                    sorted_values[index + 1],
                    sorted_values[index],
                )
                swapped = True

        if not swapped:
            break

    return sorted_values


def bubble_sort_steps(values: list[int]) -> list[list[int]]:
    """Return list states after each bubble-sort pass."""
    sorted_values = values.copy()
    steps: list[list[int]] = []

    for pass_index in range(len(sorted_values)):
        swapped = False

        for index in range(0, len(sorted_values) - pass_index - 1):
            if sorted_values[index] > sorted_values[index + 1]:
                sorted_values[index], sorted_values[index + 1] = (
                    sorted_values[index + 1],
                    sorted_values[index],
                )
                swapped = True

        steps.append(sorted_values.copy())

        if not swapped:
            break

    return steps