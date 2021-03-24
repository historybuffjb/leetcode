"""
Given an m x n matrix, return all elements of the matrix in spiral order.
"""
from typing import List


def spiral_order(matrix: List[List[int]]) -> List[int]:
    """
    Explanation
    I just took the answer here. I could not figure this out at all.
    """
    def spiral_coords(r1, c1, r2, c2):
        for c in range(c1, c2 + 1):
            yield r1, c
        for r in range(r1 + 1, r2 + 1):
            yield r, c2
        if r1 < r2 and c1 < c2:
            for c in range(c2 - 1, c1, -1):
                yield r2, c
            for r in range(r2, r1, -1):
                yield r, c1

    if not matrix:
        return []
    ans = []
    r1, r2 = 0, len(matrix) - 1
    c1, c2 = 0, len(matrix[0]) - 1
    while r1 <= r2 and c1 <= c2:
        for r, c in spiral_coords(r1, c1, r2, c2):
            ans.append(matrix[r][c])
        r1 += 1
        r2 -= 1
        c1 += 1
        c2 -= 1
    return ans


"""
Run DETAILS
Runtime: 32 ms, faster than 63.03% of Python3 online submissions for Spiral Matrix.
Memory Usage: 14.2 MB, less than 62.93% of Python3 online submissions for Spiral Matrix.
"""