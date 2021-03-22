"""
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a
backspace character.
Note that after backspacing an empty text, the text will continue empty.
"""


def _generate_text(s: str) -> str:
    stack = []
    for letter in s:
        if letter != "#":
            stack.append(letter)
        elif stack:
            stack.pop(-1)
    return ''.join(stack)


def backspace_compare(s: str, t: str) -> bool:
    """
    Explanation
    The idea here is to keep track of all the characters already seen. If at any point we encounter a #, we want
    to remove the last seen element, if possible. At the end we can just return our stack for each string and
    compare if they are equal.
    """
    return _generate_text(s) == _generate_text(t)


"""
Run DETAILS
Runtime: 32 ms, faster than 64.35% of Python3 online submissions for Backspace String Compare.
Memory Usage: 14 MB, less than 94.44% of Python3 online submissions for Backspace String Compare.
"""