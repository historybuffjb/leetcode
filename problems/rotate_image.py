"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.
"""
from typing import List


def rotate(matrix: List[List[int]]) -> None:
    """
    Explanation
    Again one I didn't get. But i'm ok not knowing this one.
    """
    n = len(matrix[0])
    for i in range(n // 2 + n % 2):
        for j in range(n // 2):
            tmp = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
            matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 - i]
            matrix[j][n - 1 - i] = matrix[i][j]
            matrix[i][j] = tmp


"""
Run DETAILS
Runtime: 24 ms, faster than 99.08% of Python3 online submissions for Rotate Image.
Memory Usage: 14.2 MB, less than 86.54% of Python3 online submissions for Rotate Image.
"""
