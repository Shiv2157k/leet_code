from typing import List


class ListNode:

    def __init__(self, val: int, next:int=None):
        self.val = val
        self.next =next


class TreeNode:

    def __init__(self, val: int, left:int=None, right:int=None):
        self.val = val
        self.left = left
        self.right = right


class Converter:

    def find_middle(self, head: "ListNode") -> "ListNode":
        """
        Finds the middle element and disconnect into two halves.
        :param head:
        :return:
        """
        prev = None
        slow = fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        if prev:
            prev.next = None
        return slow

    def to_bst_(self, head: "ListNode") -> "TreeNode":
        """
        Approach: Recursion
        Time Complexity: O(N log N)
        Space Complexity: O(log N)
        :param head:
        :return:
        """
        if not head:
            return None

        mid = self.find_middle(head)

        node = TreeNode(mid.val)

        if head == mid:
            return node

        node.left = self.to_bst_(head)
        node.right = self.to_bst_(mid.next)
        return node

    def list_converter(self, head: "ListNode") -> List[int]:
        """
        Converts given linked list to array.
        :param head:
        :return:
        """
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        return vals

    def to_bst_from_list(self, head: "ListNode") -> "TreeNode":
        """
        Approach: Conversion via list
        Time Complexity: O(N)
        Space Complexity: O(log N)
        :param head:
        :return:
        """
        if not head:
            return head

        values = self.list_converter(head)

        def convert(left, right):

            if left > right:
                return None

            mid = (left + right) // 2

            node = TreeNode(values[mid])

            if left == right:
                return node

            node.left = convert(left, mid - 1)
            node.right = convert(mid + 1, right)
            return node

        return convert(0, len(values) - 1)

    def find_size(self, head: "ListNode") -> int:
        """
        Finds the size of the given linked list.
        :param head:
        :return:
        """
        pointer, size = head, 0
        while pointer:
            pointer = pointer.next
            size += 1
        return size

    def to_bst(self, head: "ListNode") -> "TreeNode":
        """
        Approach: In-order Simulation.
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param head:
        :return:
        """

        size = self.find_size(head)

        def convert(left, right):
            nonlocal head

            if left > right:
                return None

            mid = (left + right) // 2

            left = convert(left, mid - 1)

            node = TreeNode(head.val)
            node.left = left

            head = head.next

            node.right = convert(mid + 1, right)
            return node

        return convert(0, size - 1)