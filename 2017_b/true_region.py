from typing import List


def cnt_rec(mat: List[bool][bool]):
    return cnt_records(mat, 0, 0, 0)


def cnt_records(mat: List[bool][bool], r: int, c: int, counter: int) -> int:
    if r == len(mat):
        return counter
    if c == len(mat):
        return cnt_records(mat=mat, r=r + 1, c=0, counter=counter)
    if mat[r][c]:
        counter += 1
        disable(mat, r, c)
    return cnt_records(mat=mat, r=r, c=c + 1, counter=counter)


def is_legal(mat: List[bool][bool], r: int, c: int) -> bool:
    return 0 <= r < len(mat) and 0 <= c < len(mat)


def disable(mat: List[bool][bool], r: int, c: int):
    if is_legal(mat=mat, r=r, c=c) is False or mat[r][c] is False:
        pass
    mat[r][c] = False
    disable(mat, r, c - 1)
    disable(mat, r, c + 1)
    disable(mat, r - 1, c)
    disable(mat, r + 1, c)
