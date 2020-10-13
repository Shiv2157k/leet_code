from collections import deque


class TreeNode:
    def __init__(self, val: int, left: int=None, right: int=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def get_min_depth(self, root: "TreeNode") -> int:
        """
        Approach: Iterative BFS
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param root:
        :return:
        """
        if not root:
            return 0
        else:
            queue = deque([(1, root)])

        while queue:
            depth, root = queue.popleft()
            nodes = [root.left, root.right]
            if not any(nodes):
                return depth
            for node in nodes:
                if node:
                    queue.append((depth + 1, node))

    def get_min_depth_(self, root: "TreeNode") -> int:
        """
        Approach: DFS Iteration
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param root:
        :return:
        """
        if not root:
            return 0

        stack, min_depth = [(1, root)], float("inf")

        while stack:
            curr_depth, root = stack.pop()
            nodes = [root.left, root.right]
            if not any(nodes):
                min_depth = min(min_depth, curr_depth)
            for node in nodes:
                if node:
                    stack.append((curr_depth + 1, node))
        return min_depth

    def get_min_depth__(self, root: "TreeNode") -> int:
        """
        Approach: Recursion
        Time Complexity: O(N)
        Space Complexity: O(log N)
        :param root:
        :return:
        """
        # base case
        if not root:
            return 0

        nodes = [root.left, root.right]
        # base case 1
        if not any(nodes):
            return 1
        min_depth = float("inf")
        for node in nodes:
            if node:
                min_depth = min(self.get_min_depth(node), min_depth)
        return min_depth + 1
