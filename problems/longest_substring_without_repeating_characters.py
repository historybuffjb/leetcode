"""
Given a string s, find the length of the longest substring without repeating characters.
"""


def length_of_longest_substring(s: str) -> int:
    """
    EXPLANATION:
        * Create a dictionary to store letter indexes
        * create an index to start at
        * As you traverse the list if you encounter a letter in the dictionary change the index value and compute max
        * at the end you should have a longest substring max
    """
    letter_dict = {}
    start_index = 0
    longest_substring = 0
    for i, letter in enumerate(s):
        if letter in letter_dict:
            start_index = max(letter_dict[letter], start_index)
        longest_substring = max(longest_substring, i - start_index + 1)
        letter_dict[letter] = i + 1
    return longest_substring


"""
RUN DETAILS
Runtime: 52 ms, faster than 92.84% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 14.1 MB, less than 94.27% of Python3 online submissions for Longest Substring Without Repeating Characters.
"""
