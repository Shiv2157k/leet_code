from typing import List


class Words:

    def shortest_distance(self, words: List[str], word1: str, word2:str) -> int:
        """
        Approach: One Pass
        Time Complexity: O(N * M)
        Space Complexity: O(1)
        :param words:
        :param word1:
        :param word2:
        :return:
        """
        index1 = index2 = -1
        min_distance = len(words)
        for idx in range(len(words)):
            if words[idx] == word1:
                index1 = idx
            elif words[idx] == word2:
                index2 = idx
            if index1 != -1 and index2 != -1:
                min_distance = min(min_distance, abs(index1 - index2))
        return min_distance

    def shortest_distance_(self, words: List[str], word1: str, word2: str) -> int:
        """
        Approach: Brute Force
        Time Complexity: O(N^2)
        Space Complexity: O(1)
        :param words:
        :param word1:
        :param word2:
        :return:
        """
        min_distance = len(words)
        for i in range(len(words)):
            if words[i] == word1:
                for j in range(len(words)):
                    if words[j] == word2:
                        min_distance = min(min_distance, abs(i - j))
        return min_distance


if __name__ == "__main__":
    w = Words()
    print(w.shortest_distance(
        ["practice", "makes", "perfect", "coding", "makes"], "coding", "practice"
    ))
    print(w.shortest_distance_(
        ["practice", "makes", "perfect", "coding", "makes"], "coding", "practice"
    ))