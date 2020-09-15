class ListNode:
    def __init__(self, val: int, next: int=None):
        self.val = val
        self.next =next


class Partition:

    def get_linked_list(self, head: "ListNode", x: int) -> ListNode:
        """
        Approach: Two Pointer Approach
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param head:
        :param x:
        :return:
        """

        left = left_head = ListNode(0)
        right = right_head = ListNode(0)

        while head:
            if head.val < x:
                left.next = head
                left = left.next
            else:
                right.next = head
                right = right.next
            head = head.next

        right.next = None
        left.next = right_head.next
        return left_head.next