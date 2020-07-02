class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Partition:

    def get_partition_list(self, head: ListNode, x: int) -> ListNode:
        """
        Approach: Two Pointers
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param head:
        :param x:
        :return:
        """

        # build two pointers for left and right side of x
        left = left_head = ListNode(0)
        right = right_head = ListNode(0)

        while head:
            # if it is less than move the node to left list node
            if head.val < x:
                left.next = head
                left = left.next
            # if greater move node to right list node
            else:
                right.next = head
                right = right.next
            head = head.next

        # right node is the ending list node
        right.next = None
        # combine the left and right nodes
        left.next = right_head.next
        return left_head.next