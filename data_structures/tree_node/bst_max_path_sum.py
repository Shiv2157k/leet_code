class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BST:

    def get_max_path_sum(self, root: TreeNode) -> int:
        """
        Approach: Recursion
        Time Complexity: O(N)
        Space Complexity: O(H)
        :param root:
        :return:
        """
        def max_gain(node: TreeNode) -> int:
            nonlocal max_sum

            if not node:
                return 0

            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)

            price_new_path_sum = node.val + left_gain + right_gain
            max_sum = max(max_sum, price_new_path_sum)

            return node.val + max(left_gain, right_gain)

        max_sum = float("-inf")
        max_gain(root)
        return max_sum