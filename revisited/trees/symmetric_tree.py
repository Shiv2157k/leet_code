from collections import deque


class TreeNode:

    def __init__(self, val: int, left: int=None, right: int=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def is_symmetric(self, root: "TreeNode") -> bool:
        """
        Approach: Iterative
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param root:
        :return:
        """
        # base case
        if not root:
            return True

        queue = deque([(root.left, root.right)])
        while queue:
            node1, node2 = queue.popleft()
            if not node1 and not node2:
                continue
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            queue.popleft((node1.left, node2.right))
            queue.popleft((node1.right, node2.left))
        return True

    def depth_first_search(self, node1: "TreeNode", node2: "TreeNode") -> bool:
        """
        Depth First Search function.
        :param node1:
        :param node2:
        :return:
        """
        # base cases
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        return (node1.val == node2.val) and \
               self.depth_first_search(node1.left, node2.right) and \
               self.depth_first_search(node1.right, node2.left)

    def is_symmetric(self, root: "TreeNode") -> bool:
        """
        Approach: Depth First Search
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param root:
        :return:
        """

        # base case
        if not root:
            return True
        return self.depth_first_search(root.left, root.right)