from typing import List


class TreeNode:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTree:

    def convert(self, nums: List[int]) -> "TreeNode":
        """
        Approach: Recursion with right mid elem as root node
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param nums:
        :return:
        """
        from random import randint

        def helper(left: int, right: int) -> "TreeNode":
            if left > right:
                return None
            pivot = left + (left + right) // 2
            if (left + right) % 2:
                pivot += randint(0, 1)
            root = TreeNode(nums[pivot])
            root.left = helper(left, pivot - 1)
            root.right = helper(pivot + 1, right)
            return root
        return helper(0, len(nums) - 1)

    def convert_(self, nums: List[int]) -> "TreeNode":
        """
        Approach: Recursion with right mid elem as root node
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param nums:
        :return:
        """

        def helper(left: int, right: int) -> "TreeNode":
            if left > right:
                return None
            pivot = left + (right - left) // 2
            if (left + right) % 2:
                pivot += 1
            root = TreeNode(nums[pivot])
            root.left = helper(left, pivot - 1)
            root.right = helper(pivot + 1, right)
            return root
        return helper(0, len(nums) - 1)

    def convert__(self, nums: List[int]) -> "TreeNode":
        """
        Approach: Recursion with mid elem as root node
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param nums:
        :return:
        """
        def helper(left: int, right: int) -> "TreeNode":
            if left > right:
                return None

            pivot = left + (right - left) // 2
            root = TreeNode(nums[pivot])
            root.left = helper(left, pivot - 1)
            root.right = helper(pivot + 1, right)
            return root
        return helper(0, len(nums) - 1)