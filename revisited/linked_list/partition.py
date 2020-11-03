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

        # dummy nodes reverse engineering and break downing
        # input ll to left and right
        left = left_head = ListNode(0)
        right = right_head = ListNode(0)

        while head:
            # if the node value is less than x
            # assign it to the left dummy
            if x < head.val:
                left.next = head
                # keep moving to next node of left
                left = left.next
            # if it is greater than or equal to x
            # assign it to the right
            else:
                right.next = head
                # keep moving to next node of right
                right = right.next
            # traverse through the nodes in the given ll
            head = head.next

        # close the right node
        right.next = None
        # join both left and right
        left.next = right_head.next
        return left_head.next

