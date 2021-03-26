"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number
of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.
"""
from typing import List


def num_islands(grid: List[List[str]]) -> int:
    result = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                result += 1
                grid[i][j] = "0"
                queue = [(i, j)]
                while queue:
                    left, right = queue.pop(0)
                    if left - 1 >= 0 and grid[left - 1][right] == "1":
                        queue.append((left - 1, right))
                        grid[left - 1][right] = "0"
                    if left + 1 < len(grid) and grid[left + 1][right] == "1":
                        queue.append((left + 1, right))
                        grid[left + 1][right] = "0"
                    if right - 1 >= 0 and grid[left][right - 1] == "1":
                        queue.append((left, right - 1))
                        grid[left][right - 1] = "0"
                    if right + 1 < len(grid[0]) and grid[left][right + 1] == "1":
                        queue.append((left, right + 1))
                        grid[left][right + 1] = "0"
    return result


"""
Runtime: 120 ms, faster than 98.13% of Python3 online submissions for Number of Islands.
Memory Usage: 15.2 MB, less than 94.92% of Python3 online submissions for Number of Islands.
"""
