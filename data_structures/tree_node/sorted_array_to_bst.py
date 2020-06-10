from typing import List

class TreeNode:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class ListToBST:

    def converter_(self, nums: List) -> TreeNode:
        """
            In-order traversal
            Time Complexity: O(N)
            Space Complexity: O(N)
            :param nums:
            :return:
        """
        def helper(left, right):

            # Base Case
            if left > right:
                return None

            mid = (left + right) // 2

            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)

            return root

        return helper(0, len(nums) - 1)

    def converter_2(self, nums: List[int]) -> TreeNode:
        """
        In-order traversal with mid element to be always right.
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param nums:
        :return:
        """

        def helper(left, right):
            # Base Case
            if left > right:
                return None

            mid = (left + right) // 2
            # to always pick the right element
            if (left + right) % 2:
                mid += 1

            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root
        return helper(0, len(nums) - 1)

    def convert_3(self, nums: List[int]) -> TreeNode:
        """
        In-order traversal with a random mid element.
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param nums:
        :return:
        """

        def helper(left, right):
            # Base Case
            if left > right:
                return None

            mid = (left + right) // 2
            from random import randint as r
            if (left + right) % 2:
                mid += r(0, 1)

            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root
        return helper(0, len(nums) - 1)