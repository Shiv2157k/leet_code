from typing import List


class TreeNode:
    def __init__(self, val: int, left: int = None, right: int = None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def convert_from_post_and_in_order(self, in_order: List[int], post_order: List[int]):
        """
        PostOrder: Left -> Right -> Node
        InOrder: Left -> Node -> Right
        Approach: Recursion
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param in_order:
        :param post_order:
        :return:
        """

        def helper(in_order_left=0, in_order_right=len(in_order) - 1):
            # base case
            if in_order_left > in_order_right:
                return None

            val = post_order.pop()
            node = TreeNode(val)

            index = index_map[val]

            node.right = helper(index + 1, in_order_right)
            node.left = helper(in_order_left, index - 1)

            return node

        index_map = {val: idx for idx, val in enumerate(in_order)}
        return helper()
