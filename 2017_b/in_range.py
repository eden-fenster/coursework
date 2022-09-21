from typing import List


class Range:
    def __init__(self, center: int, radius: int):
        self._center = center
        self._radius = radius

    def get_center(self):
        return self._center

    def get_radius(self):
        return self._radius


def in_range(a: List[Range], num: int):
    left: int = 0
    right: int = len(a) - 1
    mid: int
    left_bound: int
    right_bound: int

    while left <= right:
        mid = int((left + right) / 2)
        left_bound = a[mid].get_center() - a[mid].get_radius()
        right_bound = a[mid].get_center() + a[mid].get_radius()

        if left_bound <= num <= right_bound:
            return mid
        if num < left_bound:
            right = mid - 1
        else:
            left = mid + 1

    return -1
