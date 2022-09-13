from typing import List


def shortest_road(road1: List[int], road2: List[int]) -> int:
    return calculated_shortest_road(road1, road2, 0)


def calculated_shortest_road(road1: List[int], road2: List[int], i: int) -> int:
    if i == len(road1):
        return 0
    return min(road1[i] + calculated_shortest_road(road1, road2, i + 1),
               road2[i] + calculated_shortest_road(road1, road2, i + 1))
    