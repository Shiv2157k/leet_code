class TreeNode:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:

    def has_path_sum_(self, root: "TreeNode", sum: int) -> bool:
        """
        Approach: Recursion
        Time Complexity: O(N)
        Space Complexity: O(log N)
        :param root:
        :return:
        """
        if not root:
            return False
        sum -= root.val
        if not root.left and not root.right:
            return sum == 0
        return (self.has_path_sum_(root.left, sum)) or (self.has_path_sum_(root.right, sum))

    def has_path_sum(self, root: "TreeNode", sum: int) -> bool:
        """
        Approach: Iteration
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param root:
        :param sum:
        :return:
        """
        if not root:
            return False
        else:
            stack = [(root, sum - root.val), ]
        while stack:
            node, curr_sum = stack.pop()
            if not node.left and not node.right and curr_sum == 0:
                return True
            if node.left:
                stack.append((root.left, sum - root.left.val))
            if node.right:
                stack.append((root.right, sum - root.right.val))
        return False