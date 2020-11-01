class ListNode:

    def __init__(self, val: int, next: int=None):
        self.val = val
        self.next = next



class LinkedList:

    def rotate_list(self, head: "ListNode", k: int) -> "ListNode":
        """
        Approach:
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param head:
        :param k:
        :return:
        """
        # base cases
        if not head or not head.next or not k:
            return head

        old_tail = head
        length = 1
        # traverse through the end of the list
        while old_tail.next:
            old_tail = old_tail.next
            length += 1

        # build a ring
        old_tail.next = head
        new_tail = head

        # iterate to find the new tail and head
        for _ in range((length - k) % length - 1):
            new_tail = new_tail.next

        # start a new head
        new_head = new_tail.next
        # break the ring
        new_tail.next = None
        return new_head

