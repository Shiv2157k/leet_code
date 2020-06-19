class ListNode:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Nodes:

    def swap_adjacent_nodes(self, head: ListNode) -> ListNode:
        """
        Approach: Iterative
        Time Complexity: O(n)
        Space Complexity: O(1)
        :param head:
        :return:
        """

        dummy = ListNode(-1)
        dummy.next = head
        prev_node = dummy

        while head and head.next:

            # assign first and second node values
            first_node = head
            second_node = head.next

            # swap the second node to first node
            # and vice versa
            prev_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            prev_node = first_node
            head = first_node.next
        return dummy.next