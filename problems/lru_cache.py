"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
Implement the LRUCache class:
LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise,
add the key-value pair to the cache. If the number of keys exceeds the capacity from this
operation, evict the least recently used key.
Follow up:
Could you do get and put in O(1) time complexity?
"""
from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._dict = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self._dict:
            return -1
        self._dict.move_to_end(key)
        return self._dict[key]

    def put(self, key: int, value: int) -> None:
        if key in self._dict:
            self._dict.move_to_end(key)
        self._dict[key] = value
        if len(self._dict) > self._capacity:
            self._dict.popitem(last=False)


"""
Runtime: 172 ms, faster than 84.70% of Python3 online submissions for LRU Cache.
Memory Usage: 23.5 MB, less than 73.94% of Python3 online submissions for LRU Cache.
"""
