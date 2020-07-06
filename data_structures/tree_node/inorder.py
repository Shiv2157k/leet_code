from typing import List


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Inorder:

    def get_inorder_traversal(self, root: TreeNode) -> List[int]:
        """
        Approach: Iteration method using stack.
        Time Complexity: O(n)
        Space Complexity: O(n)
        :param root:
        :return:
        """
        order, stack = [], []

        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            order.append(root.val)
            root = root.right
        return order