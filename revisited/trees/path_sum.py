class TreeNode:
    def __init__(self, val: int, left: int=None, right: int=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def is_path_sum(self, root: "TreeNode", target: int) -> bool:
        """
        Approach: Iterative
        Time Complexity: O(N)
        Space Complexity: O(log N)
        :param root:
        :param target:
        :return:
        """
        # base case
        if not root:
            return False

        stack = [(root, target - root.val)]

        while stack:
            root, curr_sum = stack.pop()
            if not root.left and not root.right and curr_sum == 0:
                return True
            if root.left:
                stack.append((root.left, curr_sum - root.left.val))
            if root.right:
                stack.append((root.right, curr_sum - root.right.val))
        return False

    def is_path_sum_(self, root: "TreeNode", target: int) -> bool:
        """
        Approach: Recursion
        Time Complexity: O(N)
        Space Complexity: O(log N)
        :param root:
        :param target:
        :return:
        """
        # base case
        if not root:
            return False

        sum -= root.val

        # check if we have reached the leaf
        if not root.left and not root.right:
            return target == 0
        # do the recursion
        return self.is_path_sum_(root.left, sum) or self.is_path_sum_(root.right, sum)
