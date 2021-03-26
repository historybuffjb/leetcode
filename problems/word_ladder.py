"""
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of
words such that:
    * The first word in the sequence is beginWord.
    * The last word in the sequence is endWord.
    * Only one letter is different between each adjacent pair of words in the sequence.
    * Every word in the sequence is in wordList.
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest
transformation sequence from beginWord to endWord, or 0 if no such sequence exists.
"""
from collections import defaultdict, deque
from typing import List


def ladder_length(begin_word: str, end_word: str, word_list: List[str]) -> int:
    """
    Explanation
    This is a simple depth first search. The trick is to make vertices be a word minus one letter (all perms)
    """
    graph = defaultdict(list)
    for word in word_list:
        for i in range(len(word)):
            graph["".join([word[:i], "_", word[i + 1 :]])].append(word)
    visited = set()
    queue = deque([(begin_word, 1)])
    while queue:
        word, level = queue.popleft()
        if word == end_word:
            return level
        if word not in visited:
            visited.add(word)
            for i in range(len(word)):
                for neighbor in graph["".join([word[:i], "_", word[i + 1 :]])]:
                    queue.append((neighbor, level + 1))
    return 0


"""
Run DETAILS
Runtime: 164 ms, faster than 59.44% of Python3 online submissions for Word Ladder.
Memory Usage: 18.2 MB, less than 17.32% of Python3 online submissions for Word Ladder.
"""
