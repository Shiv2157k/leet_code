from typing import List


class Words:

    def shortest_word_distance(self, words: List[str], word1: str, word2: str) -> int:
        """
        Approach: One Pass
        Time Complexity: O(N * M)
        Space Complexity: O(1)
        :param words:
        :param word1:
        :param word2:
        :return:
        """
        p1 = p2 = -1
        min_distance = len(words)

        for pointer, word in enumerate(words):
            if word == word1:
                p1 = pointer
            elif word == word2:
                p2 = pointer

            if p1 != -1 and p2 != -1:
                min_distance = min(min_distance, abs(p2 - p1))
        return min_distance


if __name__ == "__main__":
    w = Words()
    print(w.shortest_word_distance(
        ["practice", "makes", "perfect", "coding", "makes"], word1="coding", word2="practice"
    ))
    print(w.shortest_word_distance(
        ["practice", "makes", "perfect", "coding", "makes"], word1="makes", word2="coding"
    ))