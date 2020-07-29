class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class SortList:

    def get_sorted_list(self, head: ListNode) -> ListNode:
        """
        Gets the sorted list.
        Time Complexity: O(log n)
        Space Complexity: O(1)
        :param head:
        :return:
        """
        # validation
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head
        size = 0
        while head:
            head = head.next
            size += 1
        step = 1
        while step < size:
            curr, tail = dummy.next, dummy
            while curr:
                left = curr
                right = self.split_list(left, step)
                curr = self.split_list(right, step)
                tail = self.merge_lists(left, right, tail)
            step <<= 1
        return dummy.next

    def merge_lists(self, left: ListNode, right: ListNode, head: ListNode) -> ListNode:
        """
        Merges left and right given list.
        :param left:
        :param right:
        :param head:
        :return:
        """
        dummy = node = ListNode(0)
        while left and right:
            if left.val <= right.val:
                node.next = left
                left, node = left.next, node.next
            else:
                node.next = right
                right, node = right.next, node.next

        node.next = left or right
        head.next = dummy.next
        while node.next:
            node = node.next
        return node

    def split_list(self, head: ListNode, size: int) -> ListNode:
        """
        Splits the list based on the size and returns the right list.
        :param head:
        :param size:
        :return:
        """
        for _ in range(size - 1):
            if head:
                head = head.next
        if not head:
            return None
        right = head.next
        head.next = None
        return right