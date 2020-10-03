class TreeNode:
    def __init__(self, val: int, left: int = None, right: int = None):
        self.val = val
        self.left = left
        self.right = right


class Tree:

    def get_max_path_sum(self, root: "TreeNode") -> int:
        """
        Approach: Recursion
        Time Complexity: O(N)
        Space Complexity: O(H)
        :param root:
        :return:
        """

        def node_gain(node: "TreeNode") -> int:
            nonlocal max_sum

            # base case
            if not node:
                return 0

            # to calculate all left sub trees
            left_gain = max(node_gain(node.left), 0)
            # to calculate all right sub trees
            right_gain = max(node_gain(node.right), 0)

            # check the new max_sum
            updated_max_sum = node.val + left_gain + right_gain
            # if it is greater than current max sum update the max sum
            max_sum = max(max_sum, updated_max_sum)
            # for recursion return max_gain if we are continuing the same path.
            return node.val + max(left_gain, right_gain)

        max_sum = float("-inf")
        node_gain(root)
        return max_sum