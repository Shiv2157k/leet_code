class RandomListNode:

    def __init__(self, val: int, next: int, random: int):
        self.val = val
        self.next = next
        self.random = random


class Tree:

    def __init__(self):
        self.visited = dict()

    def copy_random_list(self, head: "RandomListNode"):
        """
        Approach: Recursive
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param head:
        :return:
        """
        # base case
        if not head:
            return

        if head in self.visited:
            return self.visited[head]

        node = RandomListNode(head.val, None, None)

        self.visited[head] = node

        node.next = self.copy_random_list(head.next)
        node.random = self.copy_random_list(head.random)

        return node

    def get_cloned_node(self, node: "RandomListNode"):
        if node:
            if node in self.visited:
                return self.visited[node]
            else:
                self.visited[node] = RandomListNode(node.val, None, None)
                return self.visited[node]
        return None

    def cop_random_list_iterative(self, head: "RandomListNode"):
        """
        Approach: Iterative
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param head:
        :return:
        """
        if not head:
            return head

        old_node = head
        new_node = RandomListNode(old_node.val, None, None)
        self.visited[old_node] = new_node

        while old_node:

            new_node.random = self.get_cloned_node(old_node.random)
            new_node.next = self.get_cloned_node(old_node.next)

            old_node = old_node.next
            new_node = new_node.next
        return self.visited[head]

    def copy_node_iterative_optimized(self, head: "RandomListNode"):
        """
        Approach: Iterative Optimized
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param head:
        :return:
        """
        # validation
        if not head:
            return head

        ptr = head
        # weaving
        while ptr:
            # Clone Node
            new_node = RandomListNode(ptr.val, None, None)

            new_node.next = ptr.next
            ptr.next = new_node
            ptr = new_node.next
        ptr = head

        # link random pointer
        while ptr:
            ptr.next.random = ptr.random.next if ptr.random else None
            ptr = ptr.next.next

        # un-weaving
        ptr_old_list = head
        ptr_new_list = head.next
        head_new = head.next
        while ptr_old_list:
            ptr_old_list.next = ptr_old_list.next.next
            ptr_new_list.next = ptr_new_list.next.next if ptr_new_list.next else None
            ptr_old_list = ptr_old_list.next
            ptr_new_list - ptr_new_list.next
        return head_new