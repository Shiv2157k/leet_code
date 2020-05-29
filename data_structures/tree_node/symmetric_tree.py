class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class SymmetricTree:

    def helper(self, node1: TreeNode, node2: TreeNode):
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        return (node1.val == node1.val) \
               and self.helper(node1.left, node2.right) \
               and self.helper(node2.left, node1.right)

    def is_symmetric_(self, tree: TreeNode) -> bool:
        """
        Approach: Recursion
        :param tree:
        :return:
        """
        if not tree:
            return True
        return self.helper(tree.left, tree.right)

    def is_symmetric(self, tree: TreeNode) -> bool:
        """
        Approach: Iterative
        :param tree:
        :return:
        """
        if not tree:
            return True
        from collections import deque
        deq = deque([(tree.left, tree.right), ])
        while deq:
            node_1, node_2 = deq.popleft()
            if not node_1 and not node_2:
                continue
            if not node_1 or not node_2:
                return False
            if node_1.val != node_2.val:
                return False
            deq.append((node_1.left, node_2.right))
            deq.append((node_2.left, node_1.right))
        return True

