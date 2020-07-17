class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Reorder:

    def get_linked_list(self, head: ListNode) -> ListNode:
        """
        Approach: Reverse the Second Part and merge the two half.
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param head:
        :return:
        """
        if not head:
            return None

        # find the mid node
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse from the mid node
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        # merge the first half and reversed mid node
        left, right = head, prev
        while right.next:
            left.next, left = right, left.next
            right.next, right = left, right.next
        return head
