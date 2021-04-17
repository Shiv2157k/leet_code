class TrieNode:

    def __init__(self):
        self.child_nodes = {}
        self.end = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        """
        Time Complexity: O(M)
        Space Complexity: O(M)
        :param word:
        :return:
        """
        curr_node = self.root
        for ch in word:
            node = curr_node.child_nodes.get(ch, TrieNode())
            curr_node.child_nodes[ch] = node
            curr_node = node
        curr_node.end = True

    def search_word(self, word: str) -> bool:
        """
        Time Complexity: O(M)
        Space Complexity: O(1)
        :param word:
        :return:
        """
        curr_node = self.root
        for ch in word:
            node = curr_node.child_nodes.get(ch, None)
            if not node:
                return False
            curr_node = node
        return curr_node.end

    def search_prefix(self, word: str) -> bool:
        """
        Time Complexity: O(M)
        Space Complexity: O(1)
        :param word:
        :return:
        """
        curr_node = self.root
        for ch in word:
            node = curr_node.child_nodes.get(ch)
            if not node:
                return False
            curr_node = node
        return True


if __name__ == "__main__":

    trie = Trie()
    trie.insert("apple")
    print(trie.search_word("apple"))
    print(trie.search_word("app"))
    print(trie.search_prefix("app"))
    trie.insert("app")
    print(trie.search_word("app"))