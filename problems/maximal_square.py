"""
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
"""
from typing import List


def maximal_square(matrix: List[List[str]]) -> int:
    if not matrix:
        return 0
    rows = len(matrix)
    columns = len(matrix[0])
    dp = [[0] * (columns + 1) for _ in range(rows + 1)]
    max_side = 0
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            if matrix[i - 1][j - 1] == "1":
                dp[i][j] = min(min(dp[i][j - 1], dp[i - 1][j]), dp[i - 1][j - 1]) + 1
                max_side = max(max_side, dp[i][j])
    return max_side ** 2


"""
Runtime: 200 ms, faster than 52.97% of Python3 online submissions for Maximal Square.
Memory Usage: 15.6 MB, less than 28.91% of Python3 online submissions for Maximal Square.
"""
