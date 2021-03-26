"""
Given an m x n board of characters and a list of strings words, return all words on the board.
Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are
horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
"""
from typing import List


def find_words(board: List[List[str]], words: List[str]) -> List[str]:
    """
    Explanation
    Solution taken from leetcode solutions.
    """
    word_delim = "$"
    result = []
    trie = {}
    for word in words:
        node = trie
        for letter in word:
            node = node.setdefault(letter, {})
        node[word_delim] = word

    def backtracking(row, col, parent):

        letter = board[row][col]
        node = parent[letter]

        # check if we find a match of word
        word_match = node.pop(word_delim, False)
        if word_match:
            # also we removed the matched word to avoid duplicates,
            #   as well as avoiding using set() for results.
            result.append(word_match)

        # Before the EXPLORATION, mark the cell as visited
        board[row][col] = "#"

        # Explore the neighbors in 4 directions, i.e. up, right, down, left
        for (rowOffset, colOffset) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            temp_row, temp_col = row + rowOffset, col + colOffset
            if (
                temp_row < 0
                or temp_row >= len(board)
                or temp_col < 0
                or temp_col >= len(board[0])
            ):
                continue
            if not board[temp_row][temp_col] in node:
                continue
            backtracking(temp_row, temp_col, node)

        # End of EXPLORATION, we restore the cell
        board[row][col] = letter

        # Optimization: incrementally remove the matched leaf node in Trie.
        if not node:
            parent.pop(letter)

    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] in trie:
                backtracking(row, col, trie)
    return result


"""
Runtime: 356 ms, faster than 55.85% of Python3 online submissions for Word Search II.
Memory Usage: 14.4 MB, less than 72.59% of Python3 online submissions for Word Search II.
"""
