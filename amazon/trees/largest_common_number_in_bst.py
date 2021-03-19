class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class CommonNumber:
    gci = -1
    seen = set()

    def largest_in_two_bst(self, t1: "TreeNode", t2: "TreeNode") -> int:
        self._dfs(t1)
        self._dfs(t2)
        return self.gci

    def _dfs(self, node: "TreeNode"):
        if not node:
            return
        if node.val in self.seen:
            self.gci = max(self.gci, node.val)
        else:
            self.seen.add(node.val)