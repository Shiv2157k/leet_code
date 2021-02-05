class TreeNode:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:

    def max_depth_(self, root: "TreeNode") -> int:
        """
        Approach: Recursion
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param root:
        :return:
        """
        if not root:
            return 0

        left_height = self.max_depth_(root.left)
        right_height = self.max_depth_(root.right)

        return max(left_height, right_height) + 1

    def max_depth(self, root: "TreeNode") -> int:
        """
        Approach: Iteration / BST
        :param root:
        :return:
        """
        stack = []
        if root:
            stack.append((1, root))

        depth = 0
        while stack:
            curr_depth, root = stack.pop()
            if root:
                depth = max(curr_depth, depth)
                stack.append((curr_depth + 1, root.left))
                stack.append((curr_depth + 1, root.right))
        return depth