class ListNode:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class ListCycle:

    def get_intersection(self, head: "ListNode"):
        """
        Gets the intersection point of slow and fast.
        or hare and tortoise.
        :param head:
        :return:
        """
        tortoise = hare = head
        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next
            if tortoise == hare:
                return hare
        return None

    def get_node(self, head: "ListNode") -> "ListNode":
        """
        Approach: Floyd's tortoise and hare
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param head:
        :return:
        """
        if not head:
            return head

        meeting_point = self.get_intersection(head)
        if not meeting_point:
            return None

        pointer_1 = head
        pointer_2 = meeting_point
        while pointer_1 != pointer_2:
            pointer_1 = pointer_1.next
            pointer_2 = pointer_2.next
        return pointer_1

    def get_node_(self, head: "ListNode") -> "ListNode":
        """
        Approach: Using Hash Table
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param head:
        :return:
        """
        if not head:
            return head

        visited, node = set(), head
        while node:
            if node in visited:
                return node
            else:
                visited.add(node)
                node = node.next
        return None
