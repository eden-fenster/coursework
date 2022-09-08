from typing import List


def path_weights(m: List[int][int]):
    print_path_weights(m, 0, 0, 0)


def print_path_weights(m: List[int][int], i: int, j: int, sum_total: int):
    if i < 0 or i >= len(m) or j < 0 or j >= len(m):
        return
    if m[i][j] == -1:
        return
    if i == len(m) - 1 and j == len(m[0]) - 1:
        print(sum_total + m[len(m) - 1][len(m[0]) - 1])
    temp: int = m[i][j]
    m[i][j] = -1
    print_path_weights(m, i + 1, j, sum_total + temp)
    print_path_weights(m, i, j + 1, sum_total + temp)
    print_path_weights(m, i - 1, j, sum_total + temp)
    print_path_weights(m, i, j - 1, sum_total + temp)
    m[i][j] = temp
