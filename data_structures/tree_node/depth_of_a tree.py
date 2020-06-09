class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class MaxTreeDepth:

    def max_depth_(self, tree: TreeNode) -> int:
        """
        Approach: Recursion
        :param tree:
        :return:
        """
        if not tree:
            return 0
        else:
            left_height = self.max_depth_(tree.left)
            right_height = self.max_depth_(tree.right)
            return max(left_height, right_height) + 1

    def max_depth(self, tree: TreeNode) -> int:
        """
        Approach: Iterative
        :param self:
        :param tree:
        :return:
        """
        stack = []
        if tree is not None:
            stack.append((1, tree))

        depth = 0
        while stack:
            curr_depth, tree = stack.pop()

            if tree:
                depth = max(curr_depth, depth)
                stack.append((curr_depth + 1, tree.left))
                stack.append((curr_depth + 1, tree.right))
        return depth
