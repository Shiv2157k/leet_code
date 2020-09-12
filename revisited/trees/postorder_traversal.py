from typing import List


class TreeNode:

    def __init__(self, val:int, left:int=None, right:int=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def post_order(self, root: "TreeNode") -> List[int]:
        """
        Approach: Iterative
        Time Complexity: O(N)
        Space Complexity: O(H)
        :param root:
        :return:
        """

        if not root:
            return []

        output, stack = [], [root, ]
        while stack:
            root = stack.pop()
            output.append(root.val)

            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
        return output[::-1]

    def post_order_(self, root: "TreeNode") -> List[int]:
        """
        Approach: Recursion
        Time Complexity: O(N)
        Space Complexity: O(H)
        :param root:
        :return:
        """
        if not root:
            return []

        return self.post_order(root.left) + self.post_order(root.right) + [root.val]