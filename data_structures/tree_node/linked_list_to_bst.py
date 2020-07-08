from typing import List


class ListNode:

    def __init__(self, val, next=None):
        self.val = val
        self.next = None

class TreeNode:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Converter:

    def find_mid_node(self, head: TreeNode) -> TreeNode:
        """
        Finds the mid node of the linked list.
        :param head:
        :return:
        """
        # pointer used to disconnect left half from the mid node.
        prev_pointer = None
        slow_pointer = head
        fast_pointer = head

        # Iterate until fast pointer doesn't reach the end of linked list.
        while fast_pointer and fast_pointer.next:
            prev_pointer = slow_pointer
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

        # handling the case when slow pointer was equal to head.
        if prev_pointer:
            prev_pointer.next = None

        return slow_pointer

    def sorted_linked_list_to_height_balanced_bst(self, head: ListNode) -> TreeNode:
        """
        Approach: Recursion
        Time Complexity: O(N log N)
        Space Complexity: O(log N)
        :param head:
        :return:
        """
        # if head doesn't exist then linked list is empty.
        if not head:
            return None

        # find the middle element
        mid = self.find_mid_node(head)

        # mid becomes root of the bst.
        node = TreeNode(mid.val)

        # when there is one element in the linked list.
        if head == mid:
            return node

        # recursively build balanced bst using left and right halves of original linked list.
        node.left = self.sorted_linked_list_to_height_balanced_bst(head)
        node.right = self.sorted_linked_list_to_height_balanced_bst(mid.next)

        return node

    def list_converter(self, head: TreeNode) -> List[int]:
        """
        Converts linked list to list/ array.
        :param head:
        :return:
        """
        nodes = []
        while head:
            nodes.append(head.val)
            head = head.next
        return nodes

    def sorted_linked_list_to_height_balanced_bst_(self, head: ListNode) -> TreeNode:
        """
        Approach: Recursion + List Conversion.
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param head:
        :return:
        """
        nodes = self.list_converter(head)

        def bst_converter(left: int, right: int) -> TreeNode:

            if left > right:
                return None

            mid = (left + right) // 2
            tree = TreeNode(nodes[mid])

            if left == right:
                return tree

            tree.left = bst_converter(left, mid - 1)
            tree.right = bst_converter(mid + 1, right)

            return tree
        return bst_converter(0, len(nodes) - 1)

    def get_size(self, head: ListNode) -> int:
        """
        Gets the size of linked list.
        :param head:
        :return:
        """
        size = 0
        while head:
            head = head.next
            size += 1
        return size

    def sorted_linked_list_to_height_balanced_bst__(self, head: ListNode) -> TreeNode:
        """
        Approach: In-order Simulation.
        Time Complexity: O(N)
        Space Complexity: O(log N)
        :param head:
        :return:
        """
        if not head:
            return None
        size = self.get_size(head)

        def convert_to_bst(left: int, right: int) -> TreeNode:

            nonlocal head

            if left > right:
                return None

            mid = (left + right) // 2

            left_node = convert_to_bst(left, mid - 1)

            tree = TreeNode(head.val)
            tree.left = left_node

            head = head.next

            tree.right = convert_to_bst(mid + 1, right)
            return tree
        return convert_to_bst(0, size - 1)


