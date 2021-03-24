"""
Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.
Follow up:
    * A straight forward solution using O(mn) space is probably a bad idea.
    * A simple improvement uses O(m + n) space, but still not the best solution.
    * Could you devise a constant space solution?
"""
from typing import List


def set_zeroes(matrix: List[List[int]]) -> None:
    """
    Explanation
    The key here is that a single 0 will invalidate the entire row AND column. This makes it a little difficult
    because we need to somehow keep track of a row and column at the same time. The strategy will be to set a flag
    at the beginning of a row and end of a column if we ever encounter a zero. We loop through the matrix, setting
    the values of beginning of row and end of column if a zero is encountered. WE then loop through, setting
    any value we can find to 0. We then need to check the first row and column again possible because we would have
    missed this on the previous traversal.
    """
    return_to_first = False
    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            return_to_first = True
        for j in range(1, len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    if matrix[0][0] == 0:
        for i in range(len(matrix[0])):
            matrix[0][i] = 0
    if return_to_first:
        for i in range(len(matrix)):
            matrix[i][0] = 0


"""
Run DETAILS
Runtime: 132 ms, faster than 56.02% of Python3 online submissions for Set Matrix Zeroes.
Memory Usage: 14.9 MB, less than 91.60% of Python3 online submissions for Set Matrix Zeroes.
"""