#!/usr/bin/env python3
from typing import List


def is_sum_of_num(a: List[int], num: int):
    return is_sum(a, num, 0, 0)


def is_sum(a: List[int], num: int, i: int, j: int) -> bool:
    if i == len(a) or j == len(a):
        return False
    if num == 0:
        return True
    if a[i] + a[j] == num:
        return True
    if a[i] + a[j] + a[j + 2] == num:
        return True
    if a[i] + a[j + 1] + a[j + 2] == num:
        return True

    return is_sum(a, num, i + 1, j + 1) or is_sum(a, num, i, j + 1)
