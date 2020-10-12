

class TreeNode:
    def __init__(self, val: int, left: int=None, right: int=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def height(self, node: "TreeNode") -> int:
        """
        Gives the height of the tree
        :param node:
        :return:
        """
        if not node:
            return -1
        return 1 + max(self.height(node.left), self.height(node.right))

    def is_balanced(self, root: "TreeNode") -> bool:
        """
        Approach: Top Down Recursion
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        :param root:
        :return:
        """
        if not root:
            return True

        return (abs(self.height(root.left) - self.height(root.right)) < 2) and \
               self.is_balanced(root.left) and \
               self.is_balanced(root.right)

    def check_balance(self, node: "TreeNode") -> (bool, int):

        if not node:
            return True, -1

        left_balanced, left_height = self.check_balance(node.left)
        if not left_balanced:
            return False, 0
        right_balanced, right_height = self.check_balance(node.right)
        if not right_balanced:
            return False, 0

        return (abs(left_height - right_height) < 2), 1 + max(left_height, right_height)

    def is_balanced_(self, root: "TreeNode") -> bool:
        """
        Approach: Recursion - Bottom Up Approach
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param root:
        :return:
        """
        if not root:
            return True
        return self.check_balance(root)[0]