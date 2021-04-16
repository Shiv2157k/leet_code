from typing import List


class TrieNode:

    def __init__(self):
        self.children = {}
        self.end = False


class Dictionary:

    def longest_word(self, words: List[int]):
        """
        Approach: Trie Data Structure
        Time Complexity: O(Ewi)
        Space Complexity: O(Ewi)
        :param words: w
        :return:
        """
        self.root = TrieNode()
        words = sorted(words, key=lambda w: (-len(w), w))

        for word in words:
            curr = self.root
            for letter in word:
                if letter not in curr.children:
                    curr.children[letter] = TrieNode()
                curr = curr.children[letter]
            curr.end = True

        for word in words:
            flag = True
            curr = self.root
            for letter in word:
                if not curr.children[letter].end:
                    flag = False
                    break
                else:
                    curr = curr.children[letter]
            if flag:
                return word
        return ""


if __name__ == "__main__":
    dictionary = Dictionary()
    print(dictionary.longest_word(["w", "wo", "wor", "worl", "world"]))
    print(dictionary.longest_word(["a", "banana", "app", "appl", "ap", "apply", "apple"]))
