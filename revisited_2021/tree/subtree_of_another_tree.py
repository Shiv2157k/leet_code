class TreeNode:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:

    def equals(self, s: "TreeNode", t: "TreeNode"):
        # base cases
        if not s and not t:
            return True
        if not s or not t:
            return False
        return s.val == t.val and self.equals(s.left, t.left) and self.equals(s.right, t.right)

    def traverse(self, s: "TreeNode", t: "TreeNode"):
        return not s and (self.equals(s, t) or self.traverse(s.left, t) or self.traverse(s.right, t))

    def is_sub_tree(self, s: "TreeNode", t: "TreeNode") -> bool:
        """
        Approach: By Comparision of Nodes
        Time Complexity: O(M * N)
        Space Complexity: O(N)
        :param s:
        :param t:
        :return:
        """
        return self.traverse(s, t)