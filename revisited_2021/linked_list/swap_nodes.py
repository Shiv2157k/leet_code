class ListNode:

    def __init__(self, val: int, next: int = None):
        self.val = val
        self.next = next


class LinkedList:

    def swap_nodes(self, head: "ListNode") -> "ListNode":
        """
        Approach: Iterative
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param head:
        :return:
        """
        dummy = ListNode(-1)
        dummy.next = head

        prev_node = dummy

        while head and head.next:
            # nodes to be swapped
            first_node = head
            second_node = head.next

            # swap
            prev_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            # re-initialize head and prev_node
            prev_node = first_node
            head = first_node.next
        return dummy.next

    def swap_nodes_(self, head: "ListNode") -> "ListNode":
        """
        Approach: Recursion
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param head:
        :return:
        """

        # base case
        if not head or not head.next:
            return head

        first_node = head
        second_node = head.next

        first_node.next = self.swap_nodes_(second_node.next)
        second_node.next = first_node

        return second_node
