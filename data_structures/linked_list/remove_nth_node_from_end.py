
class ListNode:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Node:

    def remove_nth(self, head: ListNode, n: int) -> ListNode:
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

        for _ in range(n):
            first = first.next

        if first is None:
            return second

        while first.next:
            first = first.next
            second = second.next
        second.next = second.next.next
        return head