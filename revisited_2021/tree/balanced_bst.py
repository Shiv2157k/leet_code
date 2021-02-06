class TreeNode:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:

    def height(self, node: "TreeNode") -> int:
        if not node:
            return -1
        return 1 + max(self.height(node.left), self.height(node.right))

    def is_balanced(self, root: "TreeNode") -> bool:
        """
        Approach: Top Down
        Time Complexity: O(N log N)
        Space Complexity: O(N)
        :param root:
        :return:
        """
        if not root:
            return True
        return (abs(self.height(root.left) - self.height(root.right)) < 2) and self.is_balanced(
            root.left) and self.is_balanced(root.right)

    def helper(self, node: "TreeNode") -> (bool, int):
        """
        :param node:
        :return:
        """
        if not node:
            return True, -1

        is_left_balanced, left_height = self.helper(node.left)
        if not is_left_balanced:
            return False, 0
        is_right_balanced, right_height = self.helper(node.right)
        if not is_right_balanced:
            return False, 0
        return (abs(left_height - right_height) < 2), 1 + max(left_height, right_height)

    def is_balanced_(self, root: "TreeNode") -> bool:
        """
        Approach: Bottom Up
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param root:
        :return:
        """
        return self.helper(root)[0]
