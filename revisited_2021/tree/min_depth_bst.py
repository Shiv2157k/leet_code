class TreeNode:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:

    def min_depth(self, root: "TreeNode") -> int:
        """
        Approach: Iterative BFS
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param root:
        :return:
        """
        from collections import deque
        if not root:
            return 0
        else:
            q = deque([(1, root)])

        while q:
            depth, root = q.popleft()
            children = [root.left, root.right]
            if not any(children):
                return depth
            for child in children:
                if child:
                    q.append((depth + 1, child))

    def min_depth_(self, root: "TreeNode") -> int:
        """
        Approach: Iterative DFS
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param root:
        :return:
        """
        if not root:
            return 0
        else:
            stack, min_depth = [(1, root), ], float("inf")

        while stack:
            depth, root = stack.pop()
            children = [root.left, root.right]

            if not any(children):
                min_depth = min(min_depth, depth)
            for child in children:
                if child:
                    stack.append((depth + 1, child))
        return min_depth

    def min_depth__(self, root: "TreeNode") -> int:
        """
        Approach: Recursion DFS
        Time Complexity: O(N)
        Space Complexity: O(log(N))
        :param root:
        :return:
        """
        if not root:
            return 0

        children = [root.left, root.right]

        # if you have reached leaf node
        if not any(children):
            return 1
        min_depth = float("inf")
        for child in children:
            if child:
                min_depth = min(self.min_depth__(child), min_depth)
        return min_depth + 1
