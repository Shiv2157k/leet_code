from typing import List


class TreeNode:
    def __init__(self, val, left:int=None, right:int=None):
        self.val = val
        self.left = left
        self.right = right


class BST:

    def recover(self, root: "TreeNode") -> "TreeNode":
        """
        Approach: Morris Traversal
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param root:
        :return:
        """
        x = y = post = predecessor = None

        # iterate all the nodes
        while root:
            # if there is a left child
            if root.left:
                # go one step left
                predecessor = root.left
                # keep going right until you reach the dead end
                # when there is no link built.
                while predecessor.right and predecessor.right != root:
                    predecessor = predecessor.right

                # if there is no link build between predecessor and root
                # build a link
                if not predecessor.right:
                    # link built
                    predecessor.right = root
                    # move to left child
                    root = root.left
                else: # break the link and go to right child.
                    # start swapping when there is post value
                    # and is less than current root value
                    if post and root.val < post.val:
                        y = root
                        if not x:
                            x = post
                    post = root
                    # unlink the bridge to root.
                    predecessor.right = None
                    root = root.right
            else:  # go to the right child
                if post and root.val < post.val:
                    y = root
                    if not x:
                        x = post
                post = root
                root = root.right
        x.val, y.val = y.val, x.val

    def recover_(self, root: "TreeNode") -> "TreeNode":
        """
        Approach: Recursion.
        Time Complexity: O(1) best case and O(N) worst case
        Space Complexity: O(H)
        :param root:
        :return:
        """
        def find_two_swapped(root: "TreeNode"):
            nonlocal x, y, predecessor

            if not root:
                return

            find_two_swapped(root.left)
            if predecessor and root.val < predecessor.val:
                y = root
                if not x:
                    x = predecessor
            predecessor = root
            find_two_swapped(root.right)

        x = y = predecessor = None
        find_two_swapped(root)
        x.val, y.val = y.val, x.val

    def recover__(self, root: "TreeNode") -> "TreeNode":
        """
        Approach: Iterative
        Time Complexity: O(1) best case and O(N) worst case
        Space Complexity: O(H)
        :param root:
        :return:
        """
        stack = []
        x = y = predecessor = None

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if predecessor and root.val < predecessor.val:
                y = root
                if not x:
                    x = predecessor
                else:
                    break
            predecessor = root
            root = root.right
        x.val, y.val = y.val, x.val

    def recover___(self, root: "TreeNode") -> "TreeNode":
        """
        Approach: Sort an Almost Sorted Array Where Two Elements Are Swapped.
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param root:
        :return:
        """

        def in_order(r: "TreeNode") -> List[int]:
            """
            Converts the given tree into in order traversal list.
            :param r:
            :return:
            """
            return in_order(r.left) + [r.val] + in_order(r.right) if r else []

        def find_two_swapped(nums: List[int]) -> (int, int):
            """
            Gets the values that need to be swapped
            :param nums:
            :return:
            """
            n = len(nums)
            x = y = -1
            for i in range(n - 1):
                if nums[i + 1] < nums[i]:
                    y = nums[i + 1]
                    if x == -1:
                        x = nums[i]
                    else:
                        break
            return x, y

        def recover_tree(r: "TreeNode", count: int):
            """
            Recovers the binary tree.
            :param r:
            :param count:
            :return:
            """
            if r:
                if r.val == x or r.val == y:
                    r.val = y if r.val == x else x
                    count -= 1
                    if count == 0:
                        return
                recover_tree(r.left, count)
                recover_tree(r.right, count)

        nums = in_order(root)
        x, y = find_two_swapped(nums)
        recover_tree(root, 2)
