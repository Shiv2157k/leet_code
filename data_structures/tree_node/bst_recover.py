from typing import List


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class RecoverBST:

    def recover_bst(self, root: TreeNode):
        """
        Approach: Morris
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param root:
        :return:
        """
        x = y = predecessor = pred = None
        while root:
            if root.left:
                predecessor = root.left
                while predecessor.right and predecessor.right != root:
                    predecessor = predecessor.right
                if not predecessor.right:
                    predecessor.right = root
                    root = root.left
                else:
                    if pred and root.val < pred.val:
                        y = root
                        if not x:
                            x = pred
                    pred = root
                    predecessor.right = None
                    root = root.right
            else:
                if pred and root.val < pred.val:
                    y = root
                    if not x:
                        x = pred
                pred = root
                root = root.right
        x.val, y.val = y.val, x.val

    def recover_bst__(self, root: TreeNode):
        """
        Approach: Recursive in-order with two_swapped with-in
        Time Complexity: O(N)
        Space Complexity: O(H)
        :param root:
        :return:
        """
        def find_two_swapped(root: TreeNode):
            nonlocal x, y, pred
            if not root:
                return
            find_two_swapped(root.left)
            if pred and root.val < pred.val:
                y = root
                if not x:
                    x = pred
                else:
                    return
            pred = root
            find_two_swapped(root.right)
        x = y = pred = None
        find_two_swapped(root)
        x.val, y.val = y.val, x.val

    def recover_bst___(self, root: TreeNode):
        """
        Approach: Iterative in-order with stack
        Time Complexity: O(N)
        Space Complexity: O(H)
        :param root:
        :return:
        """
        stack = []
        x = y = pred = None
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if pred and root.val < pred.val:
                y = root
                if not x:
                    x = pred
            pred = root
            root = root.right
        x.val, y.val = y.val, x.val

    def recover_bst_____(self, root: TreeNode):
        """
        Approach: Recursion with in-order traversal
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param root:
        :return:
        """
        def in_order(r: TreeNode) -> List[int]:
            return in_order(r.left) + [r.val] + in_order(r.right) if r else []

        def find_two_swapped(nums: List[int]):
            n = len(nums)
            x = y = -1
            for i in range(n - 1):
                if nums[i + 1] < nums[i]:
                    y = nums[i + 1]
                    if x == -1:
                        x = nums[i]
            return x, y

        def recover(r: TreeNode, count: int):
            if r:
                if r.val == x or r.val == y:
                    r.val = y if r.val == x else x
                    count -= 1
                recover(r.left, count)
                recover(r.right, count)

        nums = in_order(root)
        x, y = find_two_swapped(nums)
        recover(root, 2)