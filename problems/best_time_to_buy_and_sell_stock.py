"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day
in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""
from sys import maxsize
from typing import List


def max_profit(prices: List[int]) -> int:
    """
    Explanation
    """
    cur_min = maxsize
    result = 0
    for val in prices:
        if val < cur_min:
            cur_min = val
        elif val - cur_min > result:
            result = val - cur_min
    return result


"""
Runtime: 944 ms, faster than 59.13% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 25.2 MB, less than 35.68% of Python3 online submissions for Best Time to Buy and Sell Stock.
"""
