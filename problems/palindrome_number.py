"""
Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.
"""


def is_palindrome(x: int) -> bool:
    result = 0
    temp = x
    while temp > 0:
        new_digit = temp % 10
        print(new_digit)
        result = result * 10 + new_digit
        print(result)
        temp //= 10
        print(temp)
    return result == x


"""
Run DETAILS
Runtime: 60 ms, faster than 66.61% of Python3 online submissions for Palindrome Number.
Memory Usage: 14.2 MB, less than 50.22% of Python3 online submissions for Palindrome Number.
"""
