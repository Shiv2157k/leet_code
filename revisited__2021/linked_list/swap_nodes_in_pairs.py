class ListNode:

    def __init__(self, val: int, next: int = None):
        self.val = val
        self.next = next


class LinkedList:

    def swap_nodes_in_pairs_(self, head: "ListNode"):
        """
        Approach: Iterative
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param head:
        :return:
        """
        new_head = ListNode(-1)
        new_head.next = head

        prev = new_head

        while head and head.next:

            # nodes to be swapped
            first = head
            second = head.next

            # swapping
            prev.next = second
            first.next = second.next
            second.next = first

            prev = first
            head = first.next
        return new_head.next

    def swap_nodes_in_pairs(self, head: "ListNode"):
        """
        Approach: Recursion
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param head:
        :return:
        """

        if not head or not head.next:
            return head

        # nodes to be swapped
        first = head
        second = head.next

        # swap
        first.next = self.swap_nodes_in_pairs(second.next)
        second.next = first

        return second


if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(4)

    linked_list = LinkedList()
    l2 = linked_list.swap_nodes_in_pairs(l1)
    while l2:
        print(l2.val)
        l2 = l2.next
    print("---------------------------------")
    ll = ListNode(1)
    ll.next = ListNode(2)
    ll.next.next = ListNode(3)
    ll.next.next.next = ListNode(4)
    linked_list1 = LinkedList()
    l3 = linked_list1.swap_nodes_in_pairs_(ll)
    while l3:
        print(l3.val)
        l3 = l3.next
