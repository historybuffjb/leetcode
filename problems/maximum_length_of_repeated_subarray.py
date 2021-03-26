"""
Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.
"""
from typing import List


def find_length(a: List[int], b: List[int]) -> int:
    """
    Explanation
    We are asked to find the maximum length of a subarray in both arrays. Since we are maximizing, we get a hint
    that Dynamic Programming will help here. We can define the recurrence relation as follows:
        * If an element is the same in both, we take dp[i][j]=dp[i + 1][j + 1] + 1, else dp[i][j]=0
        * Anytime we have an equality, check for a new maximum
    """
    maximum = 0
    dp = [[0] * (len(b) + 1) for i in range(len(a) + 1)]
    for i in range(len(a) - 1, -1, -1):
        for j in range(len(b) - 1, -1, -1):
            if a[i] == b[j]:
                dp[i][j] = dp[i + 1][j + 1] + 1
                if dp[i][j] > maximum:
                    maximum = dp[i][j]
            else:
                dp[i][j] = 0
    return maximum


"""
Run DETAILS
Runtime: 3200 ms, faster than 69.94% of Python3 online submissions for Maximum Length of Repeated Subarray.
Memory Usage: 39.6 MB, less than 38.08% of Python3 online submissions for Maximum Length of Repeated Subarray.
"""
