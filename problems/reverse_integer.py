"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value
to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""


def reverse(x: int) -> int:
    """
    Explanation
        * The key here is to lop off the last digit repeatedly and add this to a result value increasing by a unit of 10
        * We need to keep track of the sign to do this and can lop off the last value using % 10
        * We then decrement x (floor x / 10) and store in result=result*10+poppedvalue
        * We need to insure this is in the bounds of a 32-bit signed integer before and after
        * Add back the sign at the end
    """
    int_max = 2 ** 31 - 1
    int_min = -(2 ** 31)
    if x >= int_max or x <= int_min:
        return 0
    result = 0
    int_sign = 1
    if x < 0:
        int_sign = -1
        x *= int_sign
    while x != 0:
        new_digit = x % 10
        x //= 10
        result = result * 10 + new_digit
    if result >= int_max or result <= int_min:
        return 0
    return result * int_sign


"""
Run DETAILS
Runtime: 32 ms, faster than 71.53% of Python3 online submissions for Reverse Integer.
Memory Usage: 14.3 MB, less than 47.36% of Python3 online submissions for Reverse Integer.
"""
