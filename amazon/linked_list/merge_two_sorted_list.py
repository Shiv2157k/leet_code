class ListNode:

    def __init__(self, val: int, next: int):
        self.val = val
        self.next = next


class LinkedList:

    def merge_(self, l1: "ListNode", l2: "ListNode"):
        """
        Approach: Iterative
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param l1:
        :param l2:
        :return:
        """
        pre_head = ListNode(-1)
        prev = pre_head

        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        prev.next = l1 if l1 else l2
        return pre_head.next

    def merge(self, l1: "ListNode", l2: "ListNode"):
        """
        Approach: Recursion
        Time Complexity: O(M + N)
        Space Complexity: O(N)
        :param l1:
        :param l2:
        :return:
        """
        if not l1:
            return l2
        elif not l2:
            return l1
        elif l1.val < l2.val:
            l1.next = self.merge(l1.next, l2)
            return l1
        else:
            l2.next = self.merge(l1, l2.next)
            return l2