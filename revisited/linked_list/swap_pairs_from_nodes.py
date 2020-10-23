class ListNode:

    def __init__(self, val: int, next: int = None):
        self.val = val
        self.next = next


class LinkedList:

    def swap_all_pairs(self, head: "ListNode") -> "ListNode":
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
            # pick the pairs
            first_node = head
            second_node = head.next

            # swap and build link
            prev_node.next = second_node  # link
            first_node.next = second_node.next
            second_node.next = first_node

            # re-initialize head and prev node
            prev_node = first_node
            head = first_node.next
        return dummy.next

    def swap_pairs(self, head: "ListNode") -> "ListNode":
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

        # nodes that needs to be swapped
        first_node = head
        second_node = head.next

        # perform the swaps recursively
        first_node.next = self.swap_pairs(second_node.next)
        second_node.next = first_node

        return second_node