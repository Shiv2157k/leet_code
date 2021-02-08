class ListNode:

    def __init__(self, val:int, left:int=None, right:int=None):
        self.val = val
        self.left = left
        self.right = right


class LinkedList:

    def add_two_numbers(self, l1: "ListNode", l2: "ListNode") -> "ListNode":
        """
        Approach: SchoolBook Addition
        Time Complexity: O(max(m,n))
        Space Complexity: O(max(m,n))
        :param l1:
        :param l2:
        :return:
        """
        res = ListNode(None)
        res_tail = res
        carry = 0

        while l1 or l2 or carry:
            v1 = (l1.val if l1 else 0)
            v2 = (l2.val if l2 else 0)

            # val = v1 + v2 + carry
            # carry = val // 10
            carry, val = divmod(v1 + v2 + carry, 10)
            # res_tail.next = ListNode(val % 10)
            res_tail.next = ListNode(val)
            res_tail = res_tail.next

            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
        return res.next