class ListNode:

    def __init__(self, val: int, next: int = None):
        self.val = val
        self.next = next


class LinkedList:

    def remove_nth_node(self, head: "ListNode", n: int) -> "ListNode":
        """
        Approach: Single Pass
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param head:
        :return:
        """
        first = head
        second = first

        while n:
            n -= 1
            first = first.next

        while not first:
            return head.next

        while first.next:
            first = first.next
            second = second.next
        second.next = second.next.next
        return head


if __name__ == "__main__":

    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(4)

    linked_list = LinkedList()
    l2 = linked_list.remove_nth_node(l1, 2)
    while l2:
        print(l2.val)
        l2 = l2.next
