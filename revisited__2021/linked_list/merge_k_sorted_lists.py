from typing import List
from queue import PriorityQueue


class ListNode:

    def __init__(self, val: int, next: int = None):
        self.val = val
        self.next = next


class LinkedList:

    def helper(self, lists: List["ListNode"], left: int, right: int) -> "ListNode":
        # base case
        if left == right:
            return lists[left]
        pivot = left + (right - left) // 2
        l = self.helper(lists, left, pivot)
        r = self.helper(lists, pivot + 1, right)
        return self.merge(l, r)

    def merge(self, l1: "ListNode", l2: "ListNode") -> "ListNode":
        head = ListNode(-1)
        curr = head
        while l1 or l2:
            if not l1:
                curr.next = l2
                l2 = l2.next
            elif not l2:
                curr.next = l1
                l1 = l1.next
            elif l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        return head.next

    def merge_k_sorted_list(self, lists: List["ListNode"]) -> "ListNode":
        """
        Approach: Divide and Conquer
        Time Complexity: O(N log K)
        Space Complexity: O(1)
        :param lists:
        :return:
        """
        # validation
        if not lists:
            return
        return self.helper(lists, 0, len(lists) - 1)

    def merge_k_sorted(self, lists: List["ListNode"]) -> "ListNode":
        """
        Approach: Priority Queue
        Time Complexity:
        Space Complexity:
        :param lists:
        :return:
        """

        head = point = ListNode(-1)
        counter = 0
        q = PriorityQueue()

        for l in lists:
            if l:
                q.put((l.val, counter, l))
                counter += 1

        while not q.empty():
            val, _, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val, counter, node))
                counter += 1
        return head.next


if __name__ == "__main__":
    array = []
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(4)

    l2 = ListNode(2)
    l2.next = ListNode(3)
    l2.next.next = ListNode(5)

    l3 = ListNode(1)
    l3.next = ListNode(3)
    l3.next.next = ListNode(5)

    array.extend([l1, l2, l3])

    linked_list = LinkedList()
    list_node = linked_list.merge_k_sorted(array)
    while list_node:
        print(list_node.val)
        list_node = list_node.next
    print("-------------------------------------------")
    list_node1 = linked_list.merge_k_sorted_list(array)
    while list_node1:
        print(list_node1.val)
        list_node1 = list_node1.next