class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class PathSum:

    def is_path_sum(self, root: TreeNode, target: int) -> bool:
        """
        Approach: Recursion
        Time Complexity: O(N)
        Space Complexity: O(log N)
        :param root:
        :param target:
        :return:
        """

        # Base Cases
        if not root:
            return False

        target -= root.val

        if not root.left and not root.right:
            return target == 0
        return self.is_path_sum(root.left, target) or \
            self.is_path_sum(root.right, target)

    def is_path_sum_(self, root: TreeNode, target: int) -> bool:
        """
        Approach: Iteration using stack.
        Time Complexity: O(N)
        Space Complexity: O(log N)
        :param root:
        :param target:
        :return:
        """

        if not root:
            return False
        else:
            stack = [(root, target - root.val), ]

        while stack:
            curr_sum, root = stack.pop()

            if not root.left and not root.right and curr_sum == 0:
                return True
            if root.left:
                stack.append((root.left, curr_sum - root.left.val))
            if root.right:
                stack.append((root.right, curr_sum - root.right.val))
        return False