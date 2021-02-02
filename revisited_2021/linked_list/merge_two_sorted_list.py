

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TwoSorted:

    def merge(self, l1: ListNode, l2: ListNode):
        """
        Approach: Iteration
        Time Complexity: O(N + M)
        Space Complexity: O(1)
        :param l1:
        :param l2:
        :return:
        """
        head = ListNode(0)
        dummy = head
        while l1 and l2:
            if l1.val <= l2.val:
                dummy.next = l1
                l1 = l1.next
            else:
                dummy.next = l2
                l2 = l2.next
            dummy = dummy.next
        dummy.next = l1 if l1 else l2
        return head.next

    def merge_(self, l1: ListNode, l2: ListNode):
        """
        Approach: Recursion
        Time Complexity: O(N + M)
        Space Complexity: O(N + M)
        :param l1:
        :param l2:
        :return:
        """
        # base cases
        if not l1:
            return l2
        elif not l2:
            return l1
        elif l1.val < l2.val:
            l1.next = self.merge_(l1.next, l2)
            return l1
        else:
            l2.next = self.merge_(l1, l2.next)
            return l2
