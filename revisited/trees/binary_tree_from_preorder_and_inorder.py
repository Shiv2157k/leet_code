from typing import List


class TreeNode:

    def __init__(self, val: int, left: int = None, right: int = None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def convert_from_pre_and_in_order(self, pre_order: List[int], in_order: List[int]) -> "TreeNode":
        """
        Approach: Recursion
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param pre_order:
        :param in_order:
        :return:
        """

        def helper(left_in=0, right_in=len(in_order)):
            nonlocal pre_index

            if left_in == right_in:
                return None

            val = pre_order[pre_index]
            node = TreeNode(val)

            index = index_map[val]

            pre_index += 1
            node.left = helper(left_in, index)
            node.right = helper(index + 1, right_in)
            return node

        pre_index = 0
        index_map = {val: idx for idx, val in enumerate(in_order)}
        return helper()
