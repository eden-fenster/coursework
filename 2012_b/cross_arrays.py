#!/usr/bin/env python3
from typing import List


def cross_sort(arr: List[int]) -> List[int]:
    arr.sort(reverse=False)
    return arr


def cross_search(arr: List[int], x: int) -> int:
    for i in range(0, len(arr)):
        if arr[i] is not x:
            continue
        return i
    return -1
