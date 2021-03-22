from typing import List

from problems.range_sum_query_immutable import NumArray


def run_actions(actions: List[str], inputs: List[List[int]]) -> List[int]:
    driver: NumArray
    action_counter = 0
    result = []
    for action in actions:
        if action == "NumArray":
            driver = NumArray(inputs[action_counter])
            result.append(None)
        elif action == "sumRange":
            result.append(driver.sum_range(inputs[action_counter][0], inputs[action_counter][1]))
        action_counter += 1
    return result


def test_range_sum_query_immutable_1():
    actions = ["NumArray", "sumRange", "sumRange", "sumRange"]
    inputs = [[-2, 0, 3, -5, 2, -1], [0, 2], [2, 5], [0, 5]]
    expected = [None, 1, -1, -3]
    actual = run_actions(actions, inputs)
    assert actual == expected
