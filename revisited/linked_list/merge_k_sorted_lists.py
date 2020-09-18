from typing import List
from queue import PriorityQueue


class ListNode:
    def __init__(self, val: int, next:int=None):
        self.val = val
        self.next = next


class KSortedList:

    def merge_k(self, lists: List["ListNode"]) -> "ListNode":
        """
        Approach:
        Time Complexity: O(N log k)
        Space Complexity: O(1)
        :param lists:
        :return:
        """

        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge_2_lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else None

    def merge_2_lists(self, l1: "ListNode", l2: "ListNode"):

        head = point = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next

        if not l1:
            point.next = l1
        else:
            point.next = l2
        return head.next



    def merge_via_pq(self, lists: List["ListNode"]) -> "ListNode":
        """
        Approach: Using Priority Queue
        Time Complexity: O (N log k)
        Space Complexity: O(K)
        :param lists:
        :return:
        """

        head = point = ListNode(0)
        pq = PriorityQueue()
        idx = 0

        for ll in lists:
            if ll:
                pq.put((ll.val, idx, ll))
                idx += 1

        while not pq.empty():
            val, _, node = pq.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                pq.put((node.val, idx, node))
                idx += 1
        return head.next


    def merge_(self, lists: List["ListNode"]) -> "ListNode":
        """
        Approach: Brute Force
        Time Complexity: O(N log N)
        Space Complexity: O(N)
        :param lists:
        :return:
        """
        self.node = []
        for l in lists:
            while l:
                self.node.append(l.val)
                l = l.next
        head = point = ListNode(0)
        for i in sorted(self.node):
            point.next = ListNode(i)
            point = point.next
        return head.next



