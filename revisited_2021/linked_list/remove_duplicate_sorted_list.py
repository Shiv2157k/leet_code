class ListNode:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:

    def remove_duplicates(self, head: "ListNode") -> "ListNode":
        """
        Approach: Iteration
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param head:
        :return:
        """
        curr_node = head

        while curr_node and curr_node.next:
            if curr_node.val == curr_node.next.val:
                curr_node.next = curr_node.next.next
            else:
                curr_node = curr_node.next
        return head

