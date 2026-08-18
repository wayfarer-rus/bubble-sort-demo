def split_sort(values: list[int]) -> list[int]:
    """Return a sorted copy of values using split sort (merge sort)."""

    if len(values) <= 1:
        return values.copy()

    mid_index = len(values) // 2
    left_sorted = split_sort(values[:mid_index])
    right_sorted = split_sort(values[mid_index:])
    return _merge(left_sorted, right_sorted)


def _merge(left: list[int], right: list[int]) -> list[int]:
    result: list[int] = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result


def split_sort_steps(values: list[int]) -> list[list[int]]:
    """Return list states after each split-sort merge step."""

    if not values:
        return []

    if len(values) == 1:
        return [values.copy()]

    work_values = values.copy()
    steps: list[list[int]] = []

    def merge_sort_in_place(left: int, right: int) -> None:
        if right - left <= 1:
            return

        mid = (left + right) // 2
        merge_sort_in_place(left, mid)
        merge_sort_in_place(mid, right)

        left_values = work_values[left:mid]
        right_values = work_values[mid:right]

        merged_index = left
        left_index = 0
        right_index = 0

        while left_index < len(left_values) and right_index < len(right_values):
            if left_values[left_index] <= right_values[right_index]:
                work_values[merged_index] = left_values[left_index]
                left_index += 1
            else:
                work_values[merged_index] = right_values[right_index]
                right_index += 1
            merged_index += 1

        while left_index < len(left_values):
            work_values[merged_index] = left_values[left_index]
            left_index += 1
            merged_index += 1

        while right_index < len(right_values):
            work_values[merged_index] = right_values[right_index]
            right_index += 1
            merged_index += 1

        steps.append(work_values.copy())

    merge_sort_in_place(0, len(work_values))
    return steps
