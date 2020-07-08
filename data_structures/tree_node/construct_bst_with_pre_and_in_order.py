from typing import List


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class ConstructBST:

    def from_pre_order_and_in_order_values(self, pre_order: List[int], in_order: List[int]) -> TreeNode:
        """
        Approach: Recursion
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param pre_order:
        :param in_order:
        :return:
        """

        def helper(in_left=0, in_right=len(in_order)):

            # take the first pre_order element as root
            nonlocal pre_index
            # base case
            # if there is not left and right subtrees
            if in_left == in_right:
                return None

            # get the root value from pre_order
            root_val = pre_order[pre_index]
            # construct the tree
            root = TreeNode(root_val)

            # root splits in_order list
            # into left and right sub trees
            index = index_map[root_val]

            # do the recursion incrementing pre_index
            pre_index += 1

            # construct the left sub tree
            root.left = helper(in_left, index)
            # construct the right sub tree
            root.right = helper(index + 1, in_right)

            return root

        # root starts from pre_order first value
        pre_index = 0
        # build hash mapping for in_order values and index
        index_map = {val: idx for idx, val in enumerate(in_order)}
        return helper()