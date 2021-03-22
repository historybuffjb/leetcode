from typing import List, Any


class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node

    def __eq__(self, node):
        if isinstance(node, self.__class__):
            return self.val == node.val
        return False


def compare_list_nodes(expected: ListNode, actual: ListNode, debug=False):
    while expected is not None and actual is not None:
        if debug:
            print(f"Expected val: {expected.val}\tActual val: {actual.val}")
        if expected != actual:
            return False
        expected = expected.next
        actual = actual.next
    return expected is None and actual is None


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def compare_lists(exp: List[Any], act: List[Any], debug=False) -> bool:
    if debug:
        print(f"Exp: {exp}\tActual: {act}")
    if len(exp) != len(act):
        return False
    return len([val for val in exp if val in act]) == len(act)


def compare_tree_nodes(expected: TreeNode, actual: TreeNode, debug=False) -> bool:

    def _check_nodes(a: TreeNode, b: TreeNode) -> bool:
        nonlocal debug
        if debug:
            print(f"Exp: {a.val if a else None}\tAct: {b.val if b else None}")
        if not a and not b:
            return True
        if not a or not b:
            return False
        if a.val != b.val:
            return False
        return True

    queue = [(expected, actual)]
    while queue:
        exp, act = queue.pop(0)
        if not _check_nodes(exp, act):
            return False
        # We now know these are equal so WLOG choose p
        if exp:
            queue.append((exp.left, act.left))
            queue.append((exp.right, act.right))
    return True
