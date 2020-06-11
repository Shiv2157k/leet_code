class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BalancedBinaryTree:

    def height(self, root: TreeNode) -> int:
        # Base case
        # an empty tree has height -1
        if not root:
            return -1
        return 1 + max(self.height(root.left), self.height(root.right))

    def is_balanced_1(self, root: TreeNode) -> bool:
        """
        Approach: Bottom - Up Recursion.
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        :param root:
        :return:
        """
        # empty binary tree satisfies the condition
        # of balanced binary tree.
        if not root:
            return True

        # check if sub-trees has height with in 1.
        # If they do check if sub-trees are balanced.
        return abs(self.height(root.left) - self.height(root.right)) < 2 and \
               self.is_balanced_1(root.left) and \
               self.is_balanced_1(root.right)

    def is_balanced_helper(self, root: TreeNode) -> (bool, int):

        # An empty tree is a balanced tree and has height -1.
        if not root:
            return True, -1
        # Check if the sub-trees are balanced
        is_left_balanced, left_height = self.is_balanced_helper(root.left)
        if not is_left_balanced:
            return False, 0
        is_right_balanced, right_height = self.is_balanced_helper(root.right)
        if not is_right_balanced:
            return False, 0
        # If sub-trees are balanced, check to see if the current
        # tree is balanced using their heights.
        return (abs(left_height - right_height) < 2,
                1 + max(left_height, right_height))

    def is_balanced(self, root: TreeNode) -> bool:
        """
        Approach: Top Down Recurssion
        Time Complexity: O(n)
        Space Complexity: O(n)
        :param root:
        :return:
        """
        return self.is_balanced_helper(root)[0]
