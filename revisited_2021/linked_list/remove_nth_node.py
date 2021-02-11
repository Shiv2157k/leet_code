class ListNode:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:

    def remove_nth_node(self, head: "ListNode", n: int) -> "ListNode":
        """
        Approach: One Pass
        Time Complexity: O(L)
        Space Complexity: O(1)
        :param head:
        :param n:
        :return:
        """
        first = head
        second = first
        while n:
            n -= 1
            first = first.next

        if not first:
            return head.next

        while first.next:
            first = first.next
            second = second.next

        second.next = second.next.next
        return head

    def remove_nth_node_(self, head: "ListNode", n: int) -> "ListNode":
        """
        Approach: Two Pass
        Time Complexity: O(L)
        Space Complexity: O(1)
        :param head:
        :param n:
        :return:
        """
        length = 0
        dummy = ListNode(0)
        dummy.next = head
        first = head
        while first:
            first = first.next
            length += 1

        length -= n
        first = dummy
        while length:
            length -= 1
            first = first.next
        first.next = first.next.next
        return dummy.next




