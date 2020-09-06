class ListNode:
    def __init__(self,val: int, next: None or int):
        self.val = val
        self.next = next


class Node:

    def sorted(self, head: "ListNode") -> "ListNode":
        """
        Sorts the given linked list
        Time Complexity: O(N log N)
        Space Complexity: O(1)
        :param head:
        :return:
        """
        # base case
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head

        size = 0
        # find the size of the linked list
        while head:
            head = head.next
            size += 1
        step = 1

        # loop through until step is less than size
        while step < size:
            curr, tail = dummy.next, dummy
            while curr:
                left = curr
                # get the right side of ll
                right = self.split(left, step)
                # current where it stays
                curr = self.split(right, step)
                # merge both the left and right
                tail = self.merge(left, right, tail)
            step <<= 1
        return dummy.next

    def merge(self, left: "ListNode", right: ListNode, head: "ListNode", ) -> "ListNode":
        """
        Merges the left and right after the comparision.
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

    def split(self, head: "ListNode", size: int) -> "ListNode":
        """
        Splits the give linked list into half and returns the right half.
        :param head:
        :param step:
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

