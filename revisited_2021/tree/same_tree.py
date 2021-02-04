class TreeNode:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:

    def is_same(self, t1: "TreeNode", t2: "TreeNode") -> bool:
        """
        Approach: Iteration
        Time Complexity: O(N)
        Space Complexity: O(log N)
        :param t1:
        :param t2:
        :return:
        """
        def check(t1: "TreeNode", t2: "TreeNode") -> bool:
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            if t1.val != t2.val:
                return False
            return True

        from collections import deque
        deq = deque([(t1, t2), ])
        while deq:
            t1, t2 = deque.popleft()
            if not check(t1, t2):
                return False
            if t1:
                deq.append((t1.left, t2.left))
                deq.append((t1.right, t2.right))
        return True

    def is_same_(self, t1: "TreeNode", t2: "TreeNode") -> bool:
        """
        Approach: Recursion
        Time Complexity: O(N)
        Space Complexity: O(log N)
        :param t1:
        :param t2:
        :return:
        """

        # base cases
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        if t1.val != t2.val:
            return False
        return self.is_same_(t1.left, t2.left) and self.is_same_(t1.right, t2.right)
