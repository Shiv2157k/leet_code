class ListNode:

    def __init__(self, val: int, next: int):
        self.val = val
        self.next = next


class LinkedList:

    def reverse(self, head: ListNode) -> ListNode:
        """
        Approach: Iterative
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param head:
        :return:
        """
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev