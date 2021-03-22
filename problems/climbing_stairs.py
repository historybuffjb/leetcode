"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""


def climb_stairs(n: int) -> int:
    """
    Explanation
    At each step of climbing the stairs we have a choice (either 1 or 2 steps)
    """
    if n == 1:
        return 1
    dp_table = [0 for i in range(n + 1)]
    dp_table[1] = 1
    dp_table[2] = 2
    for i in range(3, n + 1):
        dp_table[i] = dp_table[i - 1] + dp_table[i - 2]
    return dp_table[n]


"""
Run DETAILS
Runtime: 36 ms, faster than 18.26% of Python3 online submissions for Climbing Stairs.
Memory Usage: 14.3 MB, less than 13.58% of Python3 online submissions for Climbing Stairs.
"""