class ListNode:

    def __init__(self, val: int, next: int = None):
        self.val = val
        self.next = next


class LinkedList:

    def reverse_(self, head: "ListNode") -> "ListNode":
        """
        Approach: Recursion
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param head:
        :return:
        """

        if not head or head.next:
            return head

        new_head = self.reverse_(head.next)
        head.next.next = new_head
        head.next = None
        return new_head

    def reverse(self, head: "ListNode") -> "ListNode":
        """
        Approach: Iterative
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param head:
        :return:
        """

        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev


if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(3)
    l1.next = ListNode(5)

    l2 = ListNode(9)
    l2.next = ListNode(10)
    l2.next = ListNode(11)

    linked_list = LinkedList()
    h = linked_list.reverse(l1)
    while h:
        print(h.val)
        h = h.next