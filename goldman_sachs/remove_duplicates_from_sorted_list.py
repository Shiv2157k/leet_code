class ListNode:

    def __init__(self, val: int = None, next=None):
        self.val = val
        self.next = next


class LinkedList:

    def remove_duplicates(self, head: "ListNode") -> "ListNode":
        """
        Approach: Iteration
        Time Complexity: O(N)
        Space Complexity: O(1)
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


if __name__ == "__main__":
    h = ListNode(val=1)
    h.next = ListNode(val=1)
    h.next.next = ListNode(val=2)
    h.next.next = ListNode(val=2)
    h.next.next.next = ListNode(val=3)

    linked_list = LinkedList()
    l1 = linked_list.remove_duplicates(h)
    while l1:
        print(l1.val)
        l1 = l1.next
