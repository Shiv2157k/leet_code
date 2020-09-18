class ListNode:

    def __init__(self, val: int = None, next: int = None):
        self.val = val
        self.next = next


class LinkedList:

    def reverse_list(self, head:"ListNode", k: int) -> "ListNode":
        # Reverse k nodes of given linked list.
        # This function assumes that list contains at-least k nodes.
        pointer, new_head = head, None

        while k:

            # to keep track of next node to process in original list
            next_node = pointer.next

            # Insert node pointed to by "ptr at beginning of
            # reversed list.
            pointer.next = new_head
            new_head = pointer

            # Move on to the next node.
            pointer = next_node

            # Decrement count of nodes to be reversed by 1
            k -= 1
        # Return head of reversed list.
        return new_head

    def reverse_node_in_k_group(self, head: "ListNode", k: int) -> "ListNode":
        """
        Approach: Iterative
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param head:
        :param k:
        :return:
        """
        ptr, k_tail, new_head = head, None, None

        # keep going until there are nodes in the list.
        while ptr:

            count = 0
            ptr = head

            # Find the head of next k nodes
            while count < k and ptr:
                ptr = ptr.next
                count += 1

            # if we counted k nodes, reverse them
            if count == k:
                # Reverse k nodes and get the new head.
                rev_head = self.reverse_list(head, k)

                # new_head is head of final linked list
                if not new_head:
                    new_head = rev_head

                # k_tail is tail of previous block of reversed k nodes.
                if k_tail:
                    k_tail.next = rev_head

                k_tail = head
                head = ptr

        # attach the final, possibly un-reversed portion
        if k_tail:
            k_tail.next = head

        return new_head if new_head else head

    def reverse_node_in_k_group_(self, head: "ListNode", k: int) -> "ListNode":
        """
        Approach: Recursion
        Time Complexity: O(N)
        Space Complexity: O(N | K)
        :param head:
        :param k:
        :return:
        """
        pointer, count = head, 0

        # First, see if there are atleast k nodes
        # left in linked list.
        while count < k and pointer:
            pointer = pointer.next
            count += 1

        # if we have k nodes, then we reverse them
        if count == k:

            # Reverse the first k nodes of the list and
            # get reversed list's head.
            reversed_head = self.reverse_list(head, k)

            # Now recurse on remaining linked list.
            # Since our recursion returns head of overall processed list,
            # we use that and the original head of k nodes to re-wire connections.
            head.next = self.reverse_node_in_k_group_(pointer, k)

            return reversed_head
        return head
