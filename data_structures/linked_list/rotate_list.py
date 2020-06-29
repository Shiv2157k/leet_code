class ListNode:

    def __init__(self, val, next=None):
        self.val = val
        self.next = None


class Rotate:

    def get_rotated_list(self, head: ListNode, k: int) -> ListNode:
        """
        Approach: Iteration
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param head:
        :param k:
        :return:
        """

        # base cases.
        if not head:
            return None
        if not head.next:
            return head

        # to find the length and tail.
        old_tail, length = head, 1
        while old_tail.next:
            old_tail = old_tail.next
            length += 1

        # create a ring
        old_tail.next = head

        # to find new head and new_tail
        new_tail = head
        for _ in range(length - k % length - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        # break the ring
        new_tail.next = None
        return new_head
