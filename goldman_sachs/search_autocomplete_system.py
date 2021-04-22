from typing import List


class TrieNode:

    def __init__(self, count=0, end=False):
        self.children = {}
        self.count = count
        self.end = end


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, sentence, time):
        curr_node = self.root
        for char in sentence:
            curr_node.children[char] = curr_node.children.get(char, TrieNode())
            curr_node = curr_node.children[char]
        curr_node.end = True
        curr_node.count -= time


class AutoCompleteSystem:
    """
    AutoCompleteSystem - O(k * l)
    l - sentences
    k - average length
    """

    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = Trie()
        self.search_term = ""
        self.last_node = self.trie.root
        self.no_match = False
        # builds the trie with current sentences and freq
        self.build_trie(sentences, times)
        self.reset_search()

    def build_trie(self, sentences: List[str], times: List[int]):
        self.trie = Trie()
        for sentence, time in zip(sentences, times):
            self.trie.insert(sentence, time)

    def reset_search(self):
        """
        Resets the trie
        :return:
        """
        self.search_term = ""
        self.last_node = self.trie.root
        self.no_match = False

    def input(self, c: str) -> List[str]:
        """
        Time Complexity: O(p + q + m log m)
        Searches the input.
        :param c:
        :return:
        """
        # resets the trie
        if c == "#":
            self.trie.insert(self.search_term, 1)
            self.reset_search()
        else: # searches the input
            # appends to the current search term
            self.search_term += c

            # if it is not there returns empty list
            if c not in self.last_node.children or self.no_match:
                self.no_match = True
                return []
            # picks the last node and checks if it exits
            self.last_node = self.last_node.children[c]
            result = []
            # traverse through the children and gets the top 3.
            self.dfs(self.last_node, self.search_term, result)
            return [sentence[1] for sentence in sorted(result)[:3]]

    def dfs(self, node, path, result):
        if node.end:
            result.append((node.count, path))
        for char in node.children:
            self.dfs(node.children[char], path + char, result)


if __name__ == "__main__":
    auto_complete_system = AutoCompleteSystem(
        ["i love you", "island", "ironman", "i love leetcode"],
        [5, 3, 2, 2]
    )
    print(auto_complete_system.input("i"))
    print(auto_complete_system.input(" "))
    print(auto_complete_system.input("a"))
    print(auto_complete_system.input("#"))
