class Node:

    def __init__(self, val: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(val)
        self.next = next
        self.random = random


class Clone:

    def __init__(self):
        self.visited = {}

    def list_with_random(self, head: 'Node') -> 'Node':
        """
        Approach: DFS
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param head:
        :return:
        """
        if not head:
            return None

        if head in self.visited:
            return self.visited[head]

        node = Node(head.val, None, None)
        self.visited[head] = node

        node.next = self.list_with_random(head.next)
        node.random = self.list_with_random(head.random)

        return node

    def get_cloned_list(self, node: 'Node') -> dict['Node']:
        if node:
            if node in self.visited:
                return self.visited[node]
            else:
                self.visited[node] = Node(node.val, None, None)
                return self.visited[node]
        return None

    def list_with_random_(self, head: 'Node') -> 'Node':
        """
        Approach: Iterative O(n) space
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param head:
        :return:
        """
        if not head:
            return None

        old_node = head
        new_node = Node(old_node.val, None, None)

        self.visited[old_node] = new_node

        while old_node:
            new_node.random = self.get_cloned_list(old_node.random)
            new_node.next = self.get_cloned_list(old_node.next)

            old_node = old_node.next
            new_node = new_node.next
        return self.visited[head]