from typing import List
from random import randint


class TreeNode:

    def __init__(self, val: int, left: int=None, right: int=None):
        self.val = val
        self.left = left
        self.right = right


class Array:

    def convert_to_bst__(self, nums: List[int]) -> "TreeNode":
        """
        Approach: Recursion: Pre-order: choose rand int from 0 to 1
        Time Complexity: O(N)
        Space Complexity: O(N) to store and O(log N) for recursion stack.
        :param nums:
        :return:
        """
        def helper(left: int, right: int) -> "TreeNode":
            # base case
            if left > right:
                return None

            pivot = (left + right) // 2
            if (left + right) % 2:
                pivot += randint(0, 1)

            root = TreeNode(nums[pivot])
            root.left = helper(left, pivot - 1)
            root.right = helper(pivot + 1, right)
            return root
        return helper(0, len(nums) - 1)

    def convert_to_bst_(self, nums: List[int]) -> "TreeNode":
        """
        Approach: Recursion: Pre-order always choose right as root.
        Time Complexity: O(N)
        Space Complexity: O(N) to store output
                          O(log N) for recursive stack
        :param nums:
        :return:
        """

        def helper(left: int, right: int) -> "TreeNode":
            # base case
            if left > right:
                return None
            # always choose right as root
            pivot = (left + right) // 2
            # if the left + right is odd
            # increment the pivot by 1
            if (left + right) % 2 == 1:
                pivot = pivot + 1

            # pre-order traversal
            root = TreeNode(nums[pivot])
            root.left = helper(left, pivot - 1)
            root.right = helper(pivot + 1, right)
            return root
        return helper(0, len(nums) - 1)

    def convert_to_bst(self, nums: List[int]) -> "TreeNode":
        """
        Approach: Recursion with binary search - Pre-Order, always choose left as root.
        Time Complexity: O(N)
        Space Complexity: O(N) to keep O/P.
                          O(log N) for recursive stack
        :param nums:
        :return:
        """

        def helper(left: int, right: int) -> "TreeNode":

            # base case
            if left > right:
                return None

            # always choose left middle node as root
            pivot = (left + right) // 2

            # initiate root
            # preorder traversal root -> left -> right
            root = TreeNode(nums[pivot])
            # pick the left half
            root.left = helper(left, pivot - 1)
            # pick the right half
            root.right = helper(pivot + 1, right)
            return root
        return helper(0, len(nums) - 1)