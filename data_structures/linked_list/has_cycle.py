
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:

    def has_cycle(self, head: ListNode) -> bool:
        """
        Approach: Two Pointers.
        Time Complexity: O(n)
        Space Complexity: O(1)
        :param head:
        :return:
        """
        if not head or not head.next:
            return False

        slow, fast = head, head.next

        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True

    def detect_cycle(self, head: ListNode) -> ListNode:
        """
        Approach: Using HashSet
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param head:
        :return:
        """
        if not head:
            return None
        visited, node = set(), head
        while node:
            if node in visited:
                return node
            else:
                visited.add(node)
                node = node.next
        return None

    def get_intersection(self, head: ListNode) -> ListNode:
        hare = tortoise = head
        while hare and hare.next:
            if tortoise == hare:
                return tortoise
            tortoise = tortoise.next
            hare = hare.next.next
        return None

    def detect_cycle_(self, head: ListNode) -> ListNode:
        """
        Approach: Floyd's tortoise and hare.
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param head:
        :return:
        """
        if not head:
            return None

        meeting_point = self.get_intersection(head)

        if not meeting_point:
            return None

        pointer1, pointer2 = head, meeting_point
        while pointer1 != pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        return pointer1