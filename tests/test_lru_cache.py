from problems.lru_cache import LRUCache


def run_test_loop(operations, values):
    result = [None]
    cache = LRUCache(values[0][0])
    for i, operation in enumerate(operations[1:], 1):
        if operation == "put":
            cache.put(values[i][0], values[i][1])
            result.append(None)
        elif operation == "get":
            result.append(cache.get(values[i][0]))
    return result


def test_lru_cache_1():
    operations = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    values = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    expected = [None, None, None, 1, None, -1, None, -1, 3, 4]
    actual = run_test_loop(operations, values)
    assert actual == expected
