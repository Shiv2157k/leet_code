class TreeNode:
    def __init__(self, val: int, left: int=None, right: int=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def get_max_depth(self, root: "TreeNode") -> int:
        """
        Approach: Recursion
        Time Complexity: O (N)
        Space Complexity: O(log(N))
        :param root:
        :return:
        """
        if not root:
            return 0
        else:
            left_height = self.get_max_depth(root.left)
            right_height = self.get_max_depth(root.right)
        return max(left_height, right_height) + 1

    def get_max_depth_(self, root: "TreeNode") -> int:
        """
        Approach: Iterative
        Time Complexity: O(N)
        Space Complexity: O(log N)
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