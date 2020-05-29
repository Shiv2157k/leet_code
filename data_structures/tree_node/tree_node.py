class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class SameTree:

    def is_same_(self, tree1: TreeNode, tree2: TreeNode) -> bool:
        """
        Approach: Recursion
        :param tree1:
        :param tree2:
        :return:
        """
        if not tree1 and not tree2:
            return True
        elif not tree1 or not tree2:
            return False
        elif tree1.val == tree2.val:
            return True
        return self.is_same_(tree1.left, tree2.left) and \
               self.is_same_(tree1.right, tree2.right)

    def is_same(self, tree1: TreeNode, tree2: TreeNode) -> bool:
        """
        Approach: Using dp with python deque.
        :param tree1:
        :param tree2:
        :return:
        """
        def check(tree1, tree2):
            if not tree1 and not tree2:
                return True
            if not tree1 or not tree2:
                return False
            if tree1.val != tree2.val:
                return False
            return True

        from collections import deque
        deq = deque[(tree1, tree2)]
        while deq:
            tree1, tree2 = deq.popleft()

            if not check((tree1, tree2)):
                return False

            if tree1:
                deq.append((tree1.left, tree2.left))
                deq.append((tree1.right, tree2.right))
        return True
