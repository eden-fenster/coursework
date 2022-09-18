from typing import List


def shortest_road(road1: List[int], road2: List[int]) -> int:
    start_road: int = int(input("road1 or road2 ? 1 for road 1 and 2 for road 2"))
    if start_road == 1:
        return calculated_shortest_road(road1, road2, 0, start_road, True, False, False)
    return calculated_shortest_road(road1, road2, 0, start_road, False, True, False)


def calculated_shortest_road\
                (road1: List[int], road2: List[int], i: int, start_road: int, on_road_1: bool, on_road_2: bool,
                 switched_yet: bool) -> int:
    if i == len(road1):
        return 0
    if start_road == 1 and switched_yet is False and road1[i + 1] > road2[i + 1]:
      return road1[i] + calculated_shortest_road(road1, road2, i + 1, 1, False, True, True)

    if start_road == 2 and switched_yet is False and road2[i + 1] > road1[i + 1]:
        return road2[i] + calculated_shortest_road(road1, road2, i + 1, 1, False, True, True)

    return min(road1[i] + calculated_shortest_road(road1, road2, i + 1),
               road2[i] + calculated_shortest_road(road1, road2, i + 1))
    