from collections import deque


class TreeNode:
    def __init__(self, val: int, left: int=None, right: int=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def is_same_tree_(self, t1: "TreeNode", t2: "TreeNode") -> bool:
        """
        Approach: Recursion
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param t1:
        :param t2:
        :return:
        """

        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        if t1.val != t2.val:
            return False
        return self.is_same_tree_(t1.left, t2.left) and self.is_same_tree_(t1.right, t2.right)

    def is_same_tree_(self, t1: "TreeNode", t2: "TreeNode") -> bool:
        """
        Approach: Iteration
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param t1:
        :param t2:
        :return:
        """

        def check(tree_1: "TreeNode", tree_2: "TreeNode") -> bool:

            if not tree_1 and not tree_2:
                return True
            if not tree_1 or not tree_2:
                return False
            if tree_1.val != tree_2.val:
                return False
            return True

        queue = deque([(t1, t2)])
        while queue:
            p, q = queue.popleft()
            if not check(p, q):
                return False
            if p:
                queue.append((p.left, q.left))
                queue.append((p.right, q.right))
        return True




