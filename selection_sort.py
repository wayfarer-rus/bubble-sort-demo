def selection_sort(values: list[int]) -> list[int]:
    """Return a sorted copy of values using selection sort."""
    sorted_values = values.copy()

    for pass_index in range(len(sorted_values)):
        minimum_index = pass_index
        for index in range(pass_index + 1, len(sorted_values)):
            if sorted_values[index] < sorted_values[minimum_index]:
                minimum_index = index

        sorted_values[pass_index], sorted_values[minimum_index] = (
            sorted_values[minimum_index],
            sorted_values[pass_index],
        )

    return sorted_values


def selection_sort_steps(values: list[int]) -> list[list[int]]:
    """Return list states after each selection-sort pass."""
    sorted_values = values.copy()
    steps: list[list[int]] = []

    for pass_index in range(len(sorted_values)):
        minimum_index = pass_index
        for index in range(pass_index + 1, len(sorted_values)):
            if sorted_values[index] < sorted_values[minimum_index]:
                minimum_index = index

        sorted_values[pass_index], sorted_values[minimum_index] = (
            sorted_values[minimum_index],
            sorted_values[pass_index],
        )
        steps.append(sorted_values.copy())

    return steps